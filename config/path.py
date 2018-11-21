#!/usr/bin/python
# -*- coding: UTF8 -*-

import os
import sys

conf_dir = os.path.dirname( os.path.realpath( __file__ ) )
app_root = os.path.dirname( conf_dir )

app_sub_dir_names = ( "controllers", "logics", "libraries", "models", "config" )
for sub_dir_name in app_sub_dir_names:
	app_sub_dir = os.path.join( app_root, sub_dir_name )
	sys.path.insert( 0, app_sub_dir )

settings = {
	"static_path"	: os.path.join( app_root, "static" ),
	"template_path"	: os.path.join( app_root, "views" ),
}
