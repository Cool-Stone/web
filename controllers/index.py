#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config.path import *
from base import BaseHandler
from json import *
from log import logger

class IndexHandler(BaseHandler):

	def initialize(self):
		super(IndexHandler, self).initialize()
		self.AddActions([
			"Welcome",
		])

	def Welcome(self):
		page = int(self.get_argument("page", "1"))
		if page is 1:
			self.render("tutorial.html")
		else:
			self.render("index.html")
		return 0
		args = self.request.arguments
		if "user" in args:
			self.write("Welcome to my website %s\n" % self.get_argument("user"))
		else:
			self.write("Sorry I don't know who you are\n")
		return 0
