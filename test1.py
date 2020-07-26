# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 21:44
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test1.py
# @Software: PyCharm


import tornado.web
import tornado.ioloop

class IndexHandeler(tornado.web.RequestHandler):
    def get(self):
        self.write('这是第一个tornado测试。')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandeler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()