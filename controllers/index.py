#!/usr/bin/python
# -*- coding: UTF8 -*-

from config.path import *
from basehandler import BaseHandler

class IndexHandler(BaseHandler):

	def initialize(self):
		super(IndexHandler, self).initialize()
		self.AddAction([
			"Welcome",
		])

	def Welcome(self):
		self.write("Hello world!\n")
		return 0
