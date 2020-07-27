# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 21:59
# @Author  : Bruce
# @Email   : daishaobing@outlook.com
# @File    : test6.py
# @Software: PyCharm



from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop



# header 设置
# .set_header()  .set_header()  .set_defualt_headers()
# 设置相应http头，前两者的不同点在于多次设置同一个项时， .add_header()会叠加参数，而
# .set_header() 则以最后一次为准
# .set_default_headers()比较特殊, 是一个空方法, 可根据需要重写,
# 作用是在每次请求初始化RequestHandler时设置默认headers.

# .clear_header() .clear()
# .clear_header()清除指定的headers, 而.clear()清除.set_default_headers()以外所有的headers设置.

class IndexHandler(RequestHandler):
    def set_default_headers(self) -> None:
        print('--------> 响应头set_default_headers()执行')
        self.set_header("Content-type", "application/json; charset=utf-8")
        self.set_header('bruce', 'bruce酷')

    def get(self):
        print("--------> get方法执行")
        self.write("{'name': 'jerry'}")
        self.set_header('bruce', 'bruce')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8888)
    IOLoop.current().start()

