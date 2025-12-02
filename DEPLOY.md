# 指数狂飙 - Vercel 云部署指南

本指南将帮助你将"指数狂飙"应用部署到 Vercel，实现随时随地通过手机访问。

## 📋 部署准备

### 1. 注册 Vercel 账号
- 访问 [Vercel官网](https://vercel.com)
- 使用 GitHub 账号登录（推荐）
- 完全免费，无需信用卡

### 2. 准备 GitHub 仓库
确保你的代码已推送到 GitHub 仓库，包含以下文件：
- `web/` - 前端页面文件
  - `index.html` - PC端页面
  - `mobile.html` - 移动端页面
- `api/` - Serverless API 函数
  - `yahoo.py` - Yahoo Finance 数据代理
  - `sina.py` - 新浪财经数据代理
- `vercel.json` - Vercel 配置文件

## 🚀 部署步骤

### 方法一：通过 Vercel Dashboard 部署（推荐）

1. **连接 GitHub 仓库**
   - 登录 [Vercel Dashboard](https://vercel.com/dashboard)
   - 点击 "New Project"
   - 选择你的 GitHub 仓库

2. **配置项目**
   - Project Name: 输入项目名称（如 `index-monitor`）
   - Framework Preset: 选择 "Other"
   - Root Directory: 保持默认 `./`
   - Build and Output Settings: 保持默认

3. **部署**
   - 点击 "Deploy" 按钮
   - 等待 2-3 分钟，部署完成
   - 获得访问地址：`https://your-project.vercel.app`

### 方法二：使用 Vercel CLI 部署

1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录 Vercel**
   ```bash
   vercel login
   ```

3. **部署项目**
   ```bash
   cd /path/to/指数狂飙
   vercel
   ```

4. **生产部署**
   ```bash
   vercel --prod
   ```

## 📱 访问方式

部署完成后，你将获得两个访问地址：

### PC端访问
```
https://your-project.vercel.app/index.html
```

### 移动端访问（推荐）
```
https://your-project.vercel.app/mobile.html
```

### 生成二维码
1. 访问 [草料二维码](https://cli.im/)
2. 输入你的移动端地址
3. 生成二维码并保存到手机
4. 随时扫码访问

## ⚙️ 配置说明

### 自动 API 切换
移动端页面已配置自动切换 API 地址：
- **本地开发**: 使用 `http://localhost:8903/api/...`
- **生产环境**: 自动切换到 `/api/...` （使用 Vercel Serverless 函数）

无需手动配置，自动检测环境！

### 自定义域名（可选）
1. 在 Vercel Dashboard 进入项目设置
2. 选择 "Domains" 标签
3. 添加你的自定义域名
4. 按照提示配置 DNS 记录

## 🔧 更新部署

### 自动部署
- 每次向 GitHub 推送代码时，Vercel 会自动重新部署
- 主分支推送 → 生产环境更新
- 其他分支推送 → 预览环境更新

### 手动部署
```bash
vercel --prod
```

## 📊 监控和日志

### 查看访问统计
1. 进入 Vercel Dashboard
2. 选择你的项目
3. 查看 "Analytics" 标签

### 查看函数日志
1. 进入项目页面
2. 选择 "Functions" 标签
3. 查看 API 调用日志和错误信息

## 🐛 常见问题

### 1. 部署失败
**问题**: Build Error 或 Deployment Failed

**解决方案**:
- 检查 `vercel.json` 配置是否正确
- 确保 Python 文件语法正确
- 查看部署日志获取详细错误信息

### 2. API 请求失败
**问题**: 数据无法加载

**解决方案**:
- 检查 Vercel Dashboard 的 Functions 日志
- 确认 Yahoo Finance 和新浪财经 API 可访问
- 可能需要等待几分钟让函数完全初始化

### 3. 手机无法访问
**问题**: 移动端页面打不开

**解决方案**:
- 确认使用 HTTPS 地址（Vercel 自动提供）
- 检查手机网络连接
- 清除浏览器缓存后重试

### 4. 数据更新慢
**问题**: 价格数据不实时

**解决方案**:
- Vercel 免费版有冷启动时间（首次请求可能较慢）
- 后续请求会更快
- 可以点击"刷新"按钮手动更新

## 💡 使用技巧

### 添加到主屏幕（iOS/Android）
1. 在手机浏览器打开移动端页面
2. iOS: 点击分享按钮 → "添加到主屏幕"
3. Android: 菜单 → "添加到主屏幕"
4. 像原生 APP 一样使用！

### 离线缓存
浏览器会自动缓存静态资源，提升加载速度。

### 数据刷新
- 下拉页面 → 自动刷新数据
- 点击底部"🔄 刷新"按钮

## 📈 性能优化建议

### 1. 启用 Vercel Analytics（可选）
```bash
npm install @vercel/analytics
```

### 2. 配置缓存策略
已在 `vercel.json` 中配置，API 响应不缓存，确保数据实时性。

### 3. 压缩图表数据
移动端已自动优化，图表使用轻量级配置。

## 🆘 获取帮助

如果遇到问题：
1. 查看 [Vercel 文档](https://vercel.com/docs)
2. 检查项目 Issues
3. 联系项目维护者

## 🎉 完成！

现在你可以随时随地在手机上查看指数数据了！

- ✅ 实时数据更新
- ✅ 枢轴点参考线
- ✅ 完全免费
- ✅ HTTPS 安全访问
- ✅ 全球 CDN 加速

享受你的指数监控之旅！📊

