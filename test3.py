# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 22:07
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test3.py
# @Software: PyCharm


from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options


# 定义变量
tornado.options.define('port', default=8000, type=int, help='this is the port')

class IndexHandler(RequestHandler):
    def get(self):
        self.write('这是第三个tornado测试，测试端口参数设置')

if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    tornado.options.parse_command_line()
    # tornado.options.parse_config_file('./config')  # 从本地读取配置

    http_server = HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    IOLoop.current().start()