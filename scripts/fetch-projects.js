#!/usr/bin/env node
/**
 * 扫描 hanphonejan 的所有仓库，检测哪些启用了 GitHub Pages
 * 生成 data/projects.json 供 Docusaurus 导航使用
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const OWNER = 'hanphonejan';
const DATA_FILE = path.join(__dirname, '..', 'data', 'projects.json');

// 简单的 HTTPS 请求封装
function request(url, options = {}) {
  return new Promise((resolve, reject) => {
    const req = https.request(url, {
      method: options.method || 'GET',
      headers: {
        'User-Agent': 'hanphonejan-projects-scanner',
        'Accept': 'application/vnd.github+json',
        ...(options.token && { 'Authorization': `Bearer ${options.token}` }),
        ...options.headers
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({
            status: res.statusCode,
            data: data ? JSON.parse(data) : null
          });
        } catch (e) {
          reject(new Error(`Failed to parse response: ${e.message}`));
        }
      });
    });
    req.on('error', reject);
    req.setTimeout(30000, () => {
      req.destroy();
      reject(new Error('Request timeout'));
    });
    req.end();
  });
}

// 获取所有仓库
async function fetchRepositories(token) {
  const repos = [];
  let page = 1;
  const perPage = 100;

  while (true) {
    const url = `https://api.github.com/users/${OWNER}/repos?per_page=${perPage}&page=${page}&sort=updated`;
    console.log(`Fetching repos page ${page}...`);

    try {
      const { status, data } = await request(url, { token });

      if (status === 403) {
        console.error('Rate limit exceeded. Consider setting GITHUB_TOKEN.');
        break;
      }

      if (status !== 200) {
        console.error(`Failed to fetch repos: HTTP ${status}`);
        break;
      }

      if (!Array.isArray(data)) {
        console.error('Unexpected response format');
        break;
      }

      repos.push(...data);

      if (data.length < perPage) break;
      page++;

      // 简单限流，避免请求过快
      await new Promise(r => setTimeout(r, 100));
    } catch (error) {
      console.error(`Error fetching page ${page}:`, error.message);
      break;
    }
  }

  return repos;
}

// 检查仓库是否启用 Pages
async function checkPages(repoName, token) {
  const url = `https://api.github.com/repos/${OWNER}/${repoName}/pages`;
  try {
    const { status, data } = await request(url, { token });
    if (status === 200 && data.html_url) {
      return {
        enabled: true,
        url: data.html_url,
        source: data.source?.branch || 'unknown'
      };
    }
  } catch (error) {
    // 404 表示未启用 Pages，这是正常的
    if (error.status === 404) {
      return { enabled: false };
    }
    // 其他错误（如 403 限流）需要处理
    if (error.status === 403) {
      console.error(`Rate limit when checking ${repoName}`);
    }
  }
  return { enabled: false };
}

// 主函数
async function main() {
  console.log(`🔍 Scanning repositories for ${OWNER}...`);

  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.warn('⚠️  GITHUB_TOKEN not set, may hit rate limits (60 requests/hour)');
  } else {
    console.log('✅ Using GITHUB_TOKEN for authentication');
  }

  try {
    // 1. 获取所有仓库
    const repos = await fetchRepositories(token);
    console.log(`📦 Found ${repos.length} repositories`);

    if (repos.length === 0) {
      console.warn('No repositories found, skipping...');
      return;
    }

    // 2. 检查每个仓库的 Pages 状态（控制并发）
    const projects = [];
    const batchSize = 3; // 控制并发数，避免限流

    for (let i = 0; i < repos.length; i += batchSize) {
      const batch = repos.slice(i, i + batchSize);
      const batchNum = Math.floor(i / batchSize) + 1;
      const totalBatches = Math.ceil(repos.length / batchSize);

      console.log(`Checking batch ${batchNum}/${totalBatches}: ${batch.map(r => r.name).join(', ')}`);

      const results = await Promise.all(
        batch.map(async (repo) => {
          try {
            const pages = await checkPages(repo.name, token);
            if (pages.enabled) {
              return {
                name: repo.name,
                url: pages.url,
                source: pages.source
              };
            }
          } catch (error) {
            console.error(`Error checking ${repo.name}:`, error.message);
          }
          return null;
        })
      );

      projects.push(...results.filter(Boolean));

      // 批次间延迟，避免限流
      if (i + batchSize < repos.length) {
        await new Promise(r => setTimeout(r, 500));
      }
    }

    // 3. 按名称排序
    projects.sort((a, b) => a.name.localeCompare(b.name));

    // 4. 生成输出
    const output = {
      lastUpdated: new Date().toISOString(),
      count: projects.length,
      projects
    };

    // 5. 检查是否有变化
    let hasChanged = true;
    if (fs.existsSync(DATA_FILE)) {
      try {
        const existing = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
        const existingProjects = existing.projects || [];
        hasChanged = JSON.stringify(existingProjects.map(p => p.name).sort()) !==
                     JSON.stringify(projects.map(p => p.name).sort());
      } catch (e) {
        console.warn('Could not compare with existing file:', e.message);
      }
    }

    // 6. 写入文件
    fs.writeFileSync(DATA_FILE, JSON.stringify(output, null, 2) + '\n');
    console.log(`✅ Written ${projects.length} projects to ${DATA_FILE}`);

    // 7. 输出供 GitHub Actions 使用的变更标记
    if (process.env.GITHUB_OUTPUT) {
      fs.appendFileSync(process.env.GITHUB_OUTPUT, `changed=${hasChanged}\n`);
    }
    console.log(`Changed: ${hasChanged}`);

    // 8. 列出找到的 projects
    if (projects.length > 0) {
      console.log('\n📋 Projects with GitHub Pages:');
      projects.forEach(p => console.log(`  - ${p.name}: ${p.url}`));
    } else {
      console.log('\n⚠️  No projects with GitHub Pages found');
    }

  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

main();
