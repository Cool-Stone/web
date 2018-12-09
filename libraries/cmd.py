#!/usr/bin/env python
# -*- coding:utf-8 -*-

import commands

class Cmd(object):
	def __init__(self):
		pass

	def CmdRet(self, command):
		output = commands.getoutput(command)
		return output

	def CmdRetMsg(self, command):
		(ret, output) = commands.getstatusoutput(command);
		return (ret, output)

commander = Cmd()
