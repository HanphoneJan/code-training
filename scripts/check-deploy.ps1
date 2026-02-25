# 部署前检查脚本

Write-Host "🔍 开始部署前检查..." -ForegroundColor Cyan

# 检查 Node.js
Write-Host "`n1. 检查 Node.js..." -ForegroundColor Yellow
if (Get-Command node -ErrorAction SilentlyContinue) {
    $nodeVersion = node --version
    Write-Host "✅ Node.js 版本: $nodeVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Node.js 未安装" -ForegroundColor Red
    exit 1
}

# 检查 pnpm
Write-Host "`n2. 检查 pnpm..." -ForegroundColor Yellow
if (Get-Command pnpm -ErrorAction SilentlyContinue) {
    $pnpmVersion = pnpm --version
    Write-Host "✅ pnpm 版本: $pnpmVersion" -ForegroundColor Green
} else {
    Write-Host "❌ pnpm 未安装，请运行: npm install -g pnpm" -ForegroundColor Red
    exit 1
}

# 检查依赖
Write-Host "`n3. 检查依赖..." -ForegroundColor Yellow
if (Test-Path "node_modules") {
    Write-Host "✅ 依赖已安装" -ForegroundColor Green
} else {
    Write-Host "⚠️  依赖未安装，正在安装..." -ForegroundColor Yellow
    pnpm install
}

# 运行类型检查
Write-Host "`n4. 运行类型检查..." -ForegroundColor Yellow
pnpm typecheck
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 类型检查通过" -ForegroundColor Green
} else {
    Write-Host "❌ 类型检查失败" -ForegroundColor Red
    exit 1
}

# 尝试构建
Write-Host "`n5. 尝试构建..." -ForegroundColor Yellow
pnpm build
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 构建成功" -ForegroundColor Green
} else {
    Write-Host "❌ 构建失败" -ForegroundColor Red
    exit 1
}

# 检查关键文件
Write-Host "`n6. 检查关键文件..." -ForegroundColor Yellow
$files = @(
    "docusaurus.config.ts",
    "sidebars.ts",
    "static/.nojekyll",
    ".github/workflows/deploy.yml"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✅ $file 存在" -ForegroundColor Green
    } else {
        Write-Host "❌ $file 不存在" -ForegroundColor Red
    }
}

# 检查 Git 状态
Write-Host "`n7. 检查 Git 状态..." -ForegroundColor Yellow
$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "⚠️  有未提交的更改:" -ForegroundColor Yellow
    git status --short
} else {
    Write-Host "✅ 工作目录干净" -ForegroundColor Green
}

Write-Host "`n✨ 检查完成！" -ForegroundColor Cyan
Write-Host "`n下一步:" -ForegroundColor Yellow
Write-Host "  1. git add ." -ForegroundColor White
Write-Host "  2. git commit -m 'your message'" -ForegroundColor White
Write-Host "  3. git push origin main" -ForegroundColor White
Write-Host "`n访问 GitHub Actions 查看部署状态" -ForegroundColor Cyan
