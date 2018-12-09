#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import logging.handlers


log_root = "/home/ubuntu/web/log/%s.log"

class Logger(object):
	def __init__(self):
		self.logger = logging.getLogger("Web")
		self.logger.setLevel(logging.INFO)
		# add a handler, every midnight refresh the log files
		# reserve 10 files each time
		handler = logging.handlers.TimedRotatingFileHandler(log_root % "debug", when='midnight', interval=1, backupCount=4)
		# old files's name will be changes as this
		handler.suffix = "%Y-%m-%d"
		formatter = logging.Formatter("[%(asctime)s %(filename)s:%(lineno)d] -%(levelname)s- %(message)s")
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
	
	def Info(self, msg):
		self.logger.info(msg)

	def Error(self, msg):
		self.logger.error(msg)

logger = Logger()

