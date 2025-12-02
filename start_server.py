#!/usr/bin/env python3
"""
指数狂飙 - Web服务器启动脚本
启动一个本地HTTP服务器来运行指数看板
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# 配置
PORT = 8902
WEB_DIR = Path(__file__).parent / 'web'

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)
    
    def end_headers(self):
        # 添加CORS头，允许跨域请求
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def start_server():
    """启动Web服务器"""
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            url = f"http://localhost:{PORT}"
            print("=" * 60)
            print("🚀 指数狂飙 Web服务器已启动！")
            print("=" * 60)
            print(f"📊 桌面版看板: {url}/index.html")
            print(f"📱 移动版看板: {url}/mobile.html")
            print(f"📈 简单仪表板: {url}/dashboard-simple.html")
            print("=" * 60)
            print(f"🌐 服务器运行在端口 {PORT}")
            print("⚠️  按 Ctrl+C 停止服务器")
            print("=" * 60)
            
            # 自动打开浏览器
            # try:
            #     webbrowser.open(f"{url}/index.html")
            #     print("✅ 已自动打开浏览器")
            # except:
            #     print("ℹ️  请手动在浏览器中打开上述地址")
            
            print()
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 错误: 端口 {PORT} 已被占用")
            print(f"💡 提示: 请关闭占用端口的程序，或修改 PORT 变量")
        else:
            print(f"❌ 启动失败: {e}")

if __name__ == "__main__":
    start_server()

