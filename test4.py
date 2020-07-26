# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 22:34
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test4.py
# @Software: PyCharm

from tornado.web import RequestHandler, Application, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

# application 配置
# debug
# 自动重启 + 取消缓存模块+取消缓存静态文件+提供追踪信息
# tornado.web.Application([(...)], debug=True)
# 开发之初可以设置debug=True方便调试，开发完毕改为False
# 原文件是否被改变/缓存模板是否要消除/静态文件的hash是否消除/和异常捕获，
# 对应:autoreload/compiled_template_cache/static_hash_cache/serve_traceback


# 路由信息初始化参数设置
# tornado.web.Application([r'', Handler, {k:v}])
# def initialize(self, k)

# 路由名称设置及反解析
# 名称设置
# tornado.web.Application([url(r'', Handler, {k:v}, name='')])
# 反解析操作
# reverse_url(name)

class IndexHandler(RequestHandler):
    def get(self):
        self.write("<a href='"+self.reverse_url("login")+"'>用户登录</a>")

class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title
    def get(self):
        self.write("注册业务处理:" + str(self.title))

class LoginHandler(RequestHandler):
    def get(self):
        self.write("用户登录页面展示")
    def post(self):
        self.write("用户登录功能处理")

if __name__ == '__main__':
    app = Application(
        [
            (r'/', IndexHandler),
            (r'/regist', RegistHandler, {'title': '会员注册'}),
            url(r'/login', LoginHandler, name='login')
        ]
    )
    http_server = HTTPServer(app)
    http_server.listen(8888)
    IOLoop.current().start()