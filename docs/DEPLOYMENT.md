# GitHub Pages 部署指南

本文档说明如何将此 Docusaurus 站点部署到 GitHub Pages。

## 🚀 自动部署

项目已配置 GitHub Actions 自动部署工作流。

### 部署流程

1. **推送代码到 main 分支**
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```

2. **GitHub Actions 自动构建**
   - 工作流文件：`.github/workflows/deploy.yml`
   - 自动安装依赖、构建站点
   - 部署到 `gh-pages` 分支

3. **访问站点**
   - URL: https://hanphonejan.github.io/code-training/
   - 通常 2-3 分钟后生效

### 查看部署状态

- 访问仓库的 **Actions** 标签页
- 查看最新的工作流运行状态
- 绿色 ✅ 表示部署成功

## ⚙️ GitHub Pages 设置

首次部署需要配置 GitHub Pages 设置：

1. 进入仓库 **Settings**
2. 点击左侧 **Pages**
3. 配置如下：

   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages` / `root`
   - 点击 **Save**

4. 等待部署完成

## 🔧 本地部署测试

### 方法一：使用 Docusaurus CLI

```bash
# 构建生产版本
pnpm build

# 本地预览构建结果
pnpm serve
```

访问 http://localhost:3001

### 方法二：使用 Docusaurus 部署命令

```bash
# 需要先配置 GIT_USER 环境变量
GIT_USER=<你的GitHub用户名> pnpm deploy
```

此命令会：
1. 构建站点
2. 推送到 `gh-pages` 分支
3. 触发 GitHub Pages 部署

## 📝 配置说明

### docusaurus.config.ts

```typescript
{
  url: 'https://hanphonejan.github.io',
  baseUrl: '/code-training/',
  organizationName: 'hanphonejan',
  projectName: 'code-training',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,
}
```

### 关键配置项

- **url**: GitHub Pages 的主域名
- **baseUrl**: 项目路径（仓库名）
- **organizationName**: GitHub 用户名或组织名
- **projectName**: 仓库名称
- **deploymentBranch**: 部署分支

## 🔍 故障排查

### 问题 1: 404 错误

**症状**: 访问站点显示 404

**解决方案**:
1. 检查 GitHub Pages 设置中的分支是否为 `gh-pages`
2. 确认 `baseUrl` 配置正确（应为 `/code-training/`）
3. 等待 3-5 分钟让 GitHub Pages 更新

### 问题 2: CSS/JS 文件加载失败

**症状**: 页面样式错乱或功能异常

**解决方案**:
1. 检查 `baseUrl` 是否正确
2. 清除浏览器缓存
3. 确认 `.nojekyll` 文件存在于 `static/` 目录

### 问题 3: GitHub Actions 失败

**症状**: Actions 标签显示红色 ❌

**解决方案**:
1. 查看具体错误日志
2. 常见原因：
   - 依赖安装失败 → 检查 `pnpm-lock.yaml`
   - 构建失败 → 检查 Markdown 文件语法
   - 权限问题 → 检查仓库 Settings > Actions > Permissions

### 问题 4: pnpm 相关错误

**症状**: GitHub Actions 中 pnpm 命令失败

**解决方案**:
```yaml
# .github/workflows/deploy.yml 中确保有
- name: Setup pnpm
  uses: pnpm/action-setup@v3
  with:
    version: 8
```

## 🌐 自定义域名（可选）

如果你有自定义域名：

1. **添加 CNAME 文件**
   ```bash
   # 在 static/ 目录下创建 CNAME 文件
   echo 'code-training.your-domain.com' > static/CNAME
   ```

2. **配置 DNS**
   - 添加 CNAME 记录指向 `<username>.github.io`

3. **更新配置**
   ```typescript
   // docusaurus.config.ts
   url: 'https://code-training.your-domain.com',
   baseUrl: '/',
   ```

4. **GitHub 设置**
   - Settings > Pages > Custom domain
   - 输入域名并保存
   - 等待 DNS 检查通过

## 📦 部署前检查清单

- [ ] 本地构建成功 (`pnpm build`)
- [ ] 预览效果正常 (`pnpm serve`)
- [ ] 所有链接正确
- [ ] 图片资源可访问
- [ ] `.nojekyll` 文件存在
- [ ] GitHub Actions 工作流正确
- [ ] docusaurus.config.ts 配置正确

## 🔄 更新部署

日常更新流程：

```bash
# 1. 修改内容
vim docs/some-file.md

# 2. 本地预览
pnpm start

# 3. 提交推送
git add .
git commit -m "Update: 添加新内容"
git push origin main

# 4. 等待自动部署
# 访问 GitHub Actions 查看进度
```

## 📚 相关资源

- [Docusaurus 部署文档](https://docusaurus.io/docs/deployment)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
- [GitHub Actions 文档](https://docs.github.com/en/actions)

---

**Happy Deploying! 🎉**
