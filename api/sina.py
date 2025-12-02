"""
Vercel Serverless Function - 新浪财经 API 代理
解决 CORS 跨域问题
"""

from http.server import BaseHTTPRequestHandler
import urllib.request
import urllib.parse
import json
import ssl


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # 解析查询参数
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            
            symbol = params.get('symbol', [''])[0]
            
            if not symbol:
                self.send_error(400, 'Missing symbol parameter')
                return
            
            # 构建新浪财经 API URL
            url = f'https://hq.sinajs.cn/list={symbol}'
            
            # 发起代理请求
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
            req.add_header('Referer', 'https://finance.sina.com.cn/')
            
            # 创建不验证SSL的上下文
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            with urllib.request.urlopen(req, timeout=10, context=ssl_context) as response:
                data = response.read()
                
            # 返回成功响应
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=gb2312')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(data)
            
        except Exception as e:
            # 返回错误响应
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_msg = json.dumps({'error': str(e)}).encode()
            self.wfile.write(error_msg)
    
    def do_OPTIONS(self):
        # 处理 CORS 预检请求
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

