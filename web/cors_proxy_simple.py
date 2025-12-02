#!/usr/bin/env python3
"""
简单的 CORS 代理服务器
支持 Yahoo Finance 和新浪财经的数据请求
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.parse
import ssl
import json

class CORSProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)

        try:
            # Yahoo Finance API
            if path.startswith('/api/yahoo'):
                symbol = query_params.get('symbol', [''])[0]
                period = query_params.get('period', ['86400'])[0]
                interval = query_params.get('interval', ['5m'])[0]
                
                period1 = int(int(period) * 1000 - int(period))  # 计算起始时间戳
                period2 = int(int(period) * 1000)  # 当前时间戳
                
                import time
                period2 = int(time.time())
                period1 = period2 - int(period)
                
                target_url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={period1}&period2={period2}&interval={interval}'
                self.proxy_request(target_url, 'application/json')
                
            # 新浪财经 API
            elif path.startswith('/api/sina'):
                symbol = query_params.get('symbol', [''])[0]
                target_url = f'https://hq.sinajs.cn/list={symbol}'
                self.proxy_request(target_url, 'text/plain')
                
            else:
                self.send_error(404, 'Not Found')
                
        except Exception as e:
            print(f'❌ 错误: {e}')
            self.send_error(500, f'Error: {str(e)}')

    def proxy_request(self, target_url, content_type):
        try:
            print(f'📡 代理请求: {target_url}')
            
            req = urllib.request.Request(target_url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')
            req.add_header('Referer', 'http://localhost:8902/')
            
            # 创建不验证SSL证书的上下文
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            with urllib.request.urlopen(req, timeout=10, context=ssl_context) as response:
                data = response.read()
                
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                
                self.wfile.write(data)
                print(f'✅ 成功: {len(data)} 字节')
                
        except Exception as e:
            print(f'❌ 代理错误: {e}')
            raise

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        pass  # 静默日志

def run_server(port=8903):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSProxyHandler)
    print('=' * 60)
    print('🌐 CORS 代理服务器已启动')
    print('=' * 60)
    print(f'📡 监听端口: {port}')
    print(f'🔗 Yahoo API: http://localhost:{port}/api/yahoo?symbol=XXX&period=86400&interval=5m')
    print(f'🔗 新浪 API: http://localhost:{port}/api/sina?symbol=XXX')
    print('=' * 60)
    print('⏹️  按 Ctrl+C 停止服务器')
    print('=' * 60)
    print()
    httpd.serve_forever()

if __name__ == '__main__':
    run_server(8903)

