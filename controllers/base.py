#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
from log import logger
import json

class BaseHandler(RequestHandler):

	def initialize(self):
		self.handler_actions = []
		self.action = None
		self.action_result = None
		
	def AddActions(self, sub_actions):
		for action in sub_actions:
			if action not in self.handler_actions:
				self.handler_actions.append(action)

	def CheckAction(self):
		if self.action not in self.handler_actions:
			self.action_result = "Action %s undefined" % self.action
			return False

		if getattr(self, self.action, None) is None:
			self.action_result = "Action %s handler function lost" % self.action
			return False

		return True

	def WriteResponse(self):
		if type(self.action_result) is dict:
			resp_buffer = "Get Result: %s" % json.dumps(self.action_result)
		elif type(self.action_result) is str:
			resp_buffer = "Get Result: %s" % self.action_result
		else:
		 	logger.Error("Get Unexpected Result Type: %s" % type(self.action_result))
		 	try:
				logger.Debug("Result is: %s" % str(self.action_result))
			except:
				logger.Error("Translate Result to String Failed")
		 	resp_buffer = "Sorry, please input valid url."

		self.write(resp_buffer)

	def get(self, action):
		self.action = action
		logger.Info("action is %s" % action)

		if self.CheckAction():
			func_result = getattr(self, self.action, None)()

			if not func_result:
				self.action_result = "Result is None"
			else:
				self.action_result = func_result

		self.WriteResponse()

	post = get
