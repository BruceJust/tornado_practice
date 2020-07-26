# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 23:26
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test5.py.py
# @Software: PyCharm


# 参数传递
# get方式传递参数
# get_query_arguments(name, default=_ARG_DEFAULT, strip=True)
# get_query_argument(name,  strip=True)
# name: 字段名
# default： 设置默认值，如果没有参数传递过来，那么就使用默认值
# strip：去除左右空格

# post方式传递参数
# get_body_arguments(name, default=_ARG_DEFAULT,strip=True)
# get_body_argument(name ,strip=True)

# 不区分post/get传递方式
# get_argument()/ get_arguments()

# 值得注意的是：
# 使用以上方法获取参数只能够获取headers报头为"application/x-www-form-urlencoded"
# 或者"multipart/form-data"的数据,如果想获取json或者xml方式传递的数据需要使用self.request方式获取

# -*- coding:utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import json


# class IndexHandler(RequestHandler):
#
#     def get(self):
#         # 获取get方式传递的参数
#         username = self.get_query_argument("username")
#         usernames = self.get_query_arguments("username")
#
#         print (username)
#         print (usernames)
#
#     def post(self):
#         # 获取post方式传递的参数
#         username = self.get_body_argument("username")
#         usernames = self.get_body_arguments("username")
#
#         print (username)
#         print (usernames)


# request
class IndexHandler(RequestHandler):
    def get(self):
        print(self.request)
        json_str = {"user_name": "admin", "password": "1234556"}
        self.write(json.dumps(json_str))



if __name__ == "__main__":
    app = Application([(r"/",IndexHandler)])

    app.listen(8888)

    IOLoop.current().start()

#网页运行时需要传入参数
#192.168.11.79:8000/?username=123
