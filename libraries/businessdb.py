#!/bin/python
# -*- coding:utf-8 -*-

import sys
import torndb
import database

class BusinessDB(object):
	def initialize(self):
		self.conn = torndb.Connection( **database.DATABASE["web"] )

