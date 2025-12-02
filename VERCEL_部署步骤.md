# 🚀 Vercel 部署详细步骤

## ✅ 准备工作（已完成）

- ✅ 代码已提交到 GitHub
- ✅ 仓库地址：https://github.com/sxc-conan/index-dashboard
- ✅ 所有必需文件已准备好

## 📝 部署步骤（5-10分钟）

### 第1步：访问 Vercel 官网

在浏览器中打开：
```
https://vercel.com
```

### 第2步：使用 GitHub 登录

1. 点击页面右上角 **"Sign Up"** 或 **"Log In"** 按钮
2. 选择 **"Continue with GitHub"**（推荐）
3. 如果是第一次使用：
   - 输入你的 GitHub 账号密码
   - 授权 Vercel 访问你的 GitHub 仓库
4. 登录成功后会进入 Vercel Dashboard

### 第3步：创建新项目

1. 在 Dashboard 页面，点击 **"Add New..."** 按钮
2. 选择 **"Project"**
3. 看到 "Import Git Repository" 页面

### 第4步：导入 GitHub 仓库

1. 在仓库列表中找到 **"index-dashboard"**
2. 如果没看到，点击 **"Import Git Repository"** 或 **"Adjust GitHub App Permissions"**
3. 选择你的仓库后，点击 **"Import"** 按钮

### 第5步：配置项目

进入配置页面后：

**Project Name**（项目名称）：
```
index-dashboard
```
或者你喜欢的其他名称，这将成为你的访问域名的一部分

**Framework Preset**（框架预设）：
```
Other
```

**Root Directory**（根目录）：
```
./
```
（保持默认即可）

**Build and Output Settings**：
```
保持默认，无需修改
```

**Environment Variables**（环境变量）：
```
无需添加
```

### 第6步：开始部署

1. 确认所有设置正确
2. 点击 **"Deploy"** 按钮
3. 等待2-3分钟，Vercel会自动：
   - 克隆你的代码
   - 构建静态文件
   - 部署 Serverless 函数
   - 分配全球CDN

### 第7步：获取访问地址

部署成功后，你会看到：

**🎉 Congratulations!**

页面会显示你的项目地址，格式类似：
```
https://index-dashboard-xxxx.vercel.app
```

或者
```
https://index-dashboard.vercel.app
```

### 第8步：访问移动端页面

在手机浏览器中输入：
```
https://你的域名.vercel.app/mobile.html
```

例如：
```
https://index-dashboard.vercel.app/mobile.html
```

## 📱 手机访问方式

### 方法1：直接输入网址
在手机浏览器地址栏输入完整地址

### 方法2：生成二维码（推荐）
1. 复制你的移动端地址
2. 访问 https://cli.im/ （草料二维码）
3. 粘贴地址，生成二维码
4. 保存二维码图片到手机相册
5. 随时扫码访问

### 方法3：添加到主屏幕
1. 在手机浏览器打开移动端页面
2. iOS：点击底部分享按钮 → "添加到主屏幕"
3. Android：点击菜单 → "添加到主屏幕"
4. 像APP一样使用！

## 🔧 部署后配置

### 查看项目信息
1. 登录 Vercel Dashboard
2. 选择你的项目
3. 可以看到：
   - 访问域名
   - 部署历史
   - 函数日志
   - 访问统计

### 自定义域名（可选）
1. 在项目设置中，选择 "Domains"
2. 添加你的域名（如 index.yourdomain.com）
3. 按提示配置DNS记录
4. 等待生效（通常几分钟）

### 自动更新
- 每次你向GitHub推送代码时
- Vercel会自动重新部署
- 无需手动操作！

## ✅ 验证部署

部署成功后，确认以下功能正常：

- [ ] 打开移动端地址能正常访问
- [ ] 数据能正常加载（显示价格和图表）
- [ ] 枢轴点参考线正确显示
- [ ] 图表能正常交互
- [ ] 市场筛选功能正常
- [ ] 刷新按钮有效

## ❓ 常见问题

**Q: 部署失败怎么办？**
A: 
1. 检查 Vercel Dashboard 的部署日志
2. 确认 vercel.json 文件格式正确
3. 确认 api/ 文件夹中的 Python 文件没有语法错误

**Q: 数据显示"加载失败"？**
A: 
- 等待3-5分钟，Serverless 函数首次启动需要时间
- 刷新页面重试
- 检查 Vercel Functions 日志

**Q: 想更新代码怎么办？**
A: 
```bash
git add .
git commit -m "更新说明"
git push origin main
```
推送后 Vercel 会自动重新部署！

## 🎊 完成！

部署成功后，你就可以：
- ✅ 随时随地在手机上查看指数数据
- ✅ 不需要电脑运行服务器
- ✅ 完全免费使用
- ✅ 全球访问速度快（CDN加速）

---

**你的项目 GitHub 地址**：
https://github.com/sxc-conan/index-dashboard

**需要帮助？**
- 查看 [DEPLOY.md](DEPLOY.md)
- 查看 [MOBILE_GUIDE.md](MOBILE_GUIDE.md)

