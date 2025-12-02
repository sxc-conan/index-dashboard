#!/usr/bin/env python3
"""
简单的 CORS 代理服务器
用于解决浏览器访问 Yahoo Finance API 的 CORS 问题
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.parse
import ssl
import json

class CORSProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析查询参数
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        # 获取目标 URL
        if 'url' not in query_params:
            self.send_error(400, 'Missing url parameter')
            return

        target_url = query_params['url'][0]

        try:
            # 请求目标 URL
            print(f'📡 代理请求: {target_url}')

            req = urllib.request.Request(target_url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')

            # 创建不验证SSL证书的上下文
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, timeout=30, context=ssl_context) as response:
                data = response.read()

                # 发送响应
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()

                self.wfile.write(data)
                print(f'✅ 成功代理: {len(data)} 字节')

        except Exception as e:
            print(f'❌ 代理错误: {e}')
            self.send_error(500, f'Proxy error: {str(e)}')

    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f'{self.address_string()} - {format % args}')

def run_server(port=8889):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSProxyHandler)
    print(f'🚀 CORS代理服务器启动在端口 {port}')
    print(f'📡 使用方式: http://localhost:{port}/?url=YOUR_TARGET_URL')
    print(f'⏹️  按 Ctrl+C 停止服务器\n')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server(8890)
