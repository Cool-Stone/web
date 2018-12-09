#!/usr/bin/env python
# -*- coding:utf-8 -*-

# This website is written for Xu Shaona's birthday at 2018/12/15
# @author: Chen Zhilei
# @date: 2018/11/16


import tornado
import tornado.web
import tornado.httpserver
import multiprocessing
from tornado.options import define, options

from config.path import *
from config.routes import GetRoutes

def _ReadConfig( config_file_path ):
	define( "app_ip", 			type = str, default = "127.0.0.1", 	help = "The IP this app listen", 	metavar = "IP" )
	define( "app_port", 		type = int, default = 80, 			help = "The port this app listen", 	metavar = "Port" )
	define( "app_name", 		type = str, default = "web", 		help = "The app name" )
	define( "max_proc_count", 	type = int, default = 3, 			help = "Max process count" )

	tornado.options.parse_config_file( config_file_path )

_ReadConfig( "/home/ubuntu/web/etc/web.conf" )


def Main():
	application = tornado.web.Application( GetRoutes(), **settings )
	http_server = tornado.httpserver.HTTPServer( application )
	http_server.bind( options.app_port, options.app_ip )
	http_server.start( num_processes = options.max_proc_count )
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	Main()
