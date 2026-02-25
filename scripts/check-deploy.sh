#!/bin/bash

# 部署前检查脚本 (Unix/Linux/Mac)

echo "🔍 开始部署前检查..."

# 检查 Node.js
echo -e "\n1. 检查 Node.js..."
if command -v node &> /dev/null; then
    echo "✅ Node.js 版本: $(node --version)"
else
    echo "❌ Node.js 未安装"
    exit 1
fi

# 检查 pnpm
echo -e "\n2. 检查 pnpm..."
if command -v pnpm &> /dev/null; then
    echo "✅ pnpm 版本: $(pnpm --version)"
else
    echo "❌ pnpm 未安装，请运行: npm install -g pnpm"
    exit 1
fi

# 检查依赖
echo -e "\n3. 检查依赖..."
if [ -d "node_modules" ]; then
    echo "✅ 依赖已安装"
else
    echo "⚠️  依赖未安装，正在安装..."
    pnpm install
fi

# 运行类型检查
echo -e "\n4. 运行类型检查..."
if pnpm typecheck; then
    echo "✅ 类型检查通过"
else
    echo "❌ 类型检查失败"
    exit 1
fi

# 尝试构建
echo -e "\n5. 尝试构建..."
if pnpm build; then
    echo "✅ 构建成功"
else
    echo "❌ 构建失败"
    exit 1
fi

# 检查关键文件
echo -e "\n6. 检查关键文件..."
files=(
    "docusaurus.config.ts"
    "sidebars.ts"
    "static/.nojekyll"
    ".github/workflows/deploy.yml"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file 存在"
    else
        echo "❌ $file 不存在"
    fi
done

# 检查 Git 状态
echo -e "\n7. 检查 Git 状态..."
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ 工作目录干净"
else
    echo "⚠️  有未提交的更改:"
    git status --short
fi

echo -e "\n✨ 检查完成！"
echo -e "\n下一步:"
echo "  1. git add ."
echo "  2. git commit -m 'your message'"
echo "  3. git push origin main"
echo -e "\n访问 GitHub Actions 查看部署状态"
