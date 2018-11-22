#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This website is written for Xu Shaona's birthday at 2018/12/15
# @author: Chen Zhilei
# @date: 2018/11/16

from config.path import *

import tornado
import tornado.ioloop
import tornado.web

sys.path.append("/home/ubuntu/web")
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
		#self.render("index.html")
		self.render("tutorial.html")
 
application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)
 
if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

