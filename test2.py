# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 21:56
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test2.py
# @Software: PyCharm


from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


# tornado.web：tornado的基础web框架
#
# RequestHandler：封装对请求处理的所有信息和处理方法
# get/post/..：封装对应的请求方式
# write()：封装响应信息，写响应信息的一个方法

# tornado.ioloop：核心io循环模块，封装linux的epoll和BSD的kqueue， tornado高性能处理的核心。
#
# current()返回当前线程的IOLoop实例对象
# start()启动IOLoop实力对象的IO循环，开启监听


class IndexHander(RequestHandler):
    def get(self):
        self.write('这是第二个tornado测试')

myapplication = [
    (r'/', IndexHander)
]

if __name__ == '__main__':
    app = Application(myapplication)
    http_server = HTTPServer(app)
    # 最原始的方式
    http_server.bind(8888)
    http_server.start(1)

    # 启动IOLoop轮循监听
    IOLoop.current().start()