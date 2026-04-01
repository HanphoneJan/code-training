import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import fs from 'fs';
import path from 'path';


// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...

// 加载 GitHub Pages 项目列表
function loadProjects() {
  try {
    const dataPath = path.join(__dirname, 'data', 'projects.json');
    if (fs.existsSync(dataPath)) {
      const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
      return data.projects || [];
    }
  } catch (e) {
    console.warn('Failed to load projects:', e.message);
  }
  return [];
}

async function createConfig(): Promise<Config> {
  const projects = loadProjects();

  return {
    title: 'HanphoneJan 的开荒地',
    tagline: '系统化算法学习与知识积累',
    favicon: 'img/favicon.ico',

    // SEO 元信息
    customFields: {
      keywords: ['算法', '数据结构', 'LeetCode', '算法训练', '编程', '面试准备'],
    },

    // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
    future: {
      v4: true,
    },

    // Set the production url of your site here
    url: 'https://www.hanphone.top',
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: '/code-training/',

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: 'hanphonejan', // Usually your GitHub org/user name.
    projectName: 'code-training', // Usually your repo name.
    deploymentBranch: 'gh-pages',
    trailingSlash: false,

    onBrokenLinks: 'warn',
    onDuplicateRoutes: 'warn',


    // Even if you don't use internationalization, you can use this field to set
    // useful metadata like html lang. For example, if your site is Chinese, you
    // may want to replace "en" with "zh-Hans".
    i18n: {
      defaultLocale: 'zh-CN',
      locales: ['zh-CN'],
    },


    markdown: {
      mermaid: true,
      format: 'detect',
      hooks: {
        onBrokenMarkdownLinks: 'warn',
      },
    },


    themes: [
      '@docusaurus/theme-mermaid',
      [
        require.resolve('@easyops-cn/docusaurus-search-local'),
        {
          hashed: true,
          language: ['en', 'zh'],
          searchBarPosition: 'right',
        },
      ],
    ],


    presets: [
      [
        'classic',
        {
          docs: {
            path: './docs', // 使用 docs 目录
            routeBasePath: '/', // 文档作为站点根路径
            editUrl: 'https://github.com/hanphonejan/code-training/edit/main/',
            showLastUpdateTime: false,
            sidebarPath: './sidebars.ts',
            exclude: [
              '**/_*.{js,jsx,ts,tsx,md,mdx}',
              '**/_*/**',
              '**/*.test.{js,jsx,ts,tsx}',
              '**/__tests__/**',
              '**/node_modules/**',
              '**/.docusaurus/**',
              '**/build/**',
              '**/dist/**',
              '**/.git/**',
              '**/.github/**',
              '**/scripts/**',
              '**/src/**',
              '**/static/**',
              '**/blog/**',
              '*.config.*',
              '*.json',
              '*.lock',
              '*.yml',
              '*.yaml',
              '.gitignore',
              '.gitattributes',
            ],
          },
          blog: false, // 禁用 blog 功能
          theme: {
            customCss: ["./src/css/fonts.css", "./src/css/custom.css"],
          },
        } satisfies Preset.Options,
      ],
    ],


    themeConfig: {
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'HanphoneJan',
        hideOnScroll: false,
        items: [
          {href: 'https://www.hanphone.top/', label: '首页', position: 'left', target: '_self'},
          {href: 'https://www.hanphone.top/docs/intro', label: '文档', position: 'left', target: '_self'},
          {href: 'https://www.hanphone.top/blog', label: '博客', position: 'left', target: '_self'},
          {href: 'https://www.hanphone.top/stars', label: 'Stars', position: 'left', target: '_self'},
          {
            type: 'dropdown',
            label: '代码训练',
            position: 'left',
            items: [
              {to: '/category/-%E9%A2%98%E7%9B%AE%E5%BA%93', label: '编程题库'},
              {to: '/category/-%E7%9F%A5%E8%AF%86%E7%82%B9', label: '知识点'},
              {to: '/category/-%E7%AE%97%E6%B3%95%E6%A8%A1%E5%BC%8F', label: '算法模式'},
              {to: '/category/-%E4%BB%A3%E7%A0%81%E6%A8%A1%E6%9D%BF', label: '代码模板'},
              {to: '/category/-%E5%A4%8D%E4%B9%A0%E7%B3%BB%E7%BB%9F', label: '总结盘点'},
            ],
          },
          // 动态项目下拉菜单（仅当有项目时显示）
          ...(projects.length > 0 ? [{
            type: 'dropdown' as const,
            label: '项目',
            position: 'left' as const,
            items: projects.map((p: {name: string, url: string}) => ({
              label: p.name,
              href: p.url,
            })),
          }] : []),
          {
            href: 'https://github.com/hanphonejan/code-training',
            label: 'GitHub',
            position: 'right',
            className: 'navbar-github-icon',
          },
          {
            href: 'https://hanphone.cn',
            label: '个人主页',
            position: 'right',
            className: 'navbar-blog-icon',
          },
        ],
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.oneDark,
        additionalLanguages: ['bash', 'python', 'java', 'typescript', 'javascript', 'go', 'rust', 'sql', 'json', 'verilog'],
        magicComments: [
          {
            className: 'theme-code-block-highlighted-line',
            line: 'highlight-next-line',
            block: {start: 'highlight-start', end: 'highlight-end'},
          },
        ],
      },
      mermaid: {
        theme: {light: 'default', dark: 'dark'},
      },
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
    } satisfies Preset.ThemeConfig,
  };
}


export default createConfig;
