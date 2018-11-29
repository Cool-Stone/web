#!/usr/bin/python
# -*- coding: UTF8 -*-

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
		args = self.request.arguments
		if "user" in args:
			self.write("Welcome to my website %s\n" % self.get_argument("user"))
		else:
			self.write("Sorry I don't know who you are\n")
		return 0
