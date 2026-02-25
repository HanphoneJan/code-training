# Git 提交说明

请遵循以下提交规范，保持提交历史清晰。

## 提交格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（必填）

- **feat**: 新功能
- **fix**: 修复 bug
- **docs**: 文档更新
- **style**: 代码格式调整（不影响代码运行）
- **refactor**: 重构代码
- **test**: 测试相关
- **chore**: 构建过程或辅助工具的变动
- **perf**: 性能优化

### Scope（可选）

影响范围，如：problems, topics, patterns, templates, config

### Subject（必填）

简短描述，不超过 50 字符。

### 示例

```bash
# 添加新题目
git commit -m "feat(problems): 添加两数之和题目"

# 更新知识点
git commit -m "docs(topics): 完善数组知识点说明"

# 修复链接
git commit -m "fix(patterns): 修复双指针模式的文档链接"

# 配置更新
git commit -m "chore(config): 更新 GitHub Pages 部署配置"
```

## 常用命令

```bash
# 查看状态
git status

# 添加所有更改
git add .

# 提交
git commit -m "type(scope): message"

# 推送到远程
git push origin main

# 查看提交历史
git log --oneline
```
