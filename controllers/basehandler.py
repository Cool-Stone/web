#!/usr/bin/python
# -*- conding: UTF8 -*-

from tornado.web import RequestHandler
from log import logger

class BaseHandler(RequestHandler):

	def initialize(self):
		self.handler_actions = []
		self.action = None
		
	def AddActions(self, sub_actions):
		for action in sub_actions:
			if action not in self.handler_actions:
				self.handler_actions.append(action)

	def CheckAction(self):
		if self.action not in self.handler_actions:
			#todo
			return False

		if getattr(self, self.action, None) is None:
			#todo
			return False

	def WriteResponse(self):
		if type(self.action_result) is dict:
			resp_buffer = "Action Result is Dict"
		else:
			resp_buffer = "Action Result is String"

		self.write(resp_buffer)

	def get(self, action):
		print "Call get(), action is [%s]" % action
		self.action = action
		logger.Info("action is %s" % action)

		if self.CheckAction():
			func_result = getattr(self, self.action, None)()

			if not func_result:
				return
			elif isinstance(func_result, dict):
				#todo
				pass
			elif isinstance(func_result, str):
				self.acction_result = func_result
			else:
			 	return

		self.WriteResponse()

	post = get
