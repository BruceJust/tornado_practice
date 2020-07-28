# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 22:17
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test7.py
# @Software: PyCharm


from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop



# writeerror
# .send_error()用于发送HTTP错误页(状态码). 该操作会调用.clear() .set_status()
# .write_error()用于清除headers, 设置状态码, 发送错误页. 重写.write_error()可以自定义错误页.

class IndexHandler(RequestHandler):

    def get(self):
        self.write('hello bruce.com')
        self.send_error(404, msg='页面丢失', info='家里服务请搞对象去了')
    def write_error(self, status_code, **kwargs):
        self.write('<h1>出错啦，工程师mm正在路上</h1>')
        self.write('<p>错误信息：%s</p>' % kwargs['msg'])
        self.write('<p>错误描述：%s</p>' % kwargs['info'])



if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8888)
    IOLoop.current().start()