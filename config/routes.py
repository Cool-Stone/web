#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from controllers.index import IndexHandler
from controllers.index import BaseHandler

def GetRoutes():
	routes = [
		( r"/(\w+)", IndexHandler ),
	]

	return routes
