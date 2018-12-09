#!/bin/sh

# Project: web
#
# This is a simple web server written in Python
# It is used to celebrate for XuShaona's birthday
# So DO NOT apply it to other scene because it is
# designed just for fun
#
#
# Author: ChenZhilei
# Company: Tencent
# Date: 2018/12/1
#
#
# Run this script and the whole server will be intalled
# Have fun ^_^


function printHelp() {
	echo -e "\e[1;33m
		Welcome to my web project
		Now the server should have been installed successfully
		So just start it now such like this
		>>> nginxConsole start
		>>> webConsole start
		
		oh, \e[1;31mDO NOT FORGET\e[1;33m to set your mysql right
		If you forget your password, maybe you can reset it following to guidence below:
		>>> sudo cat /etc/mysql/debian.cnf
		then login with its username and password
		>>> update mysql.user set plugin = \"mysql_native_password\", authentication_string = \"password('root')\" where user = \"root\";
		>>> flush privileges;
		OK, All done.
		\e[0m"
}

function getHome() {
	script_path=`readlink -f ${0}`
	bin_path=`dirname ${script_path}`
	root=`dirname ${bin_path}`
	echo -e "[ \e[32mDetecting\e[0m ] web project will be installed in \e[33m${root}\e[0m"
}

function installPackage() {
	# install nginx
	echo -e "[ \e[32m1 \e[0m/\e[32m 6\e[0m ] installing \e[33mnginx\e[0m"
	sudo apt install nginx

	# install pip
	echo -e "[ \e[32m2 \e[0m/\e[32m 6\e[0m ] installing \e[33mpip\e[0m"
	sudo apt install python pip

	# install tornado
	echo -e "[ \e[32m3 \e[0m/\e[32m 6\e[0m ] installing \e[33mtornado\e[0m"
	sudo pip install tornado

	# install torndb
	echo -e "[ \e[32m4 \e[0m/\e[32m 6\e[0m ] installing \e[33mtorndb\e[0m"
	sudo pip install torndb

	# install mysql
	echo -e "[ \e[32m5 \e[0m/\e[32m 6\e[0m ] installing \e[33mmysql\e[0m"
	sudo apt install mysql-server
	sudo apt install mysql-client
	sudo apt install libmysqlclient-dev
	
	# install mysql-python
	echo -e "[ \e[32m6 \e[0m/\e[32m 6\e[0m ] installing \e[33mmysql-python\e[0m"
	sudo pip install mysql-python

	echo -e "[ \e[35mWARNING\e[0m ] please mannually set mysql"
}

function createLinking() {
	echo -e "[ \e[36mnginxConsole\e[0m ] link \e[33m${bin_path}/nginxConsole\e[0m to \e[33m/usr/bin/nginxConsole\e[0m"
	if [[ -h "/usr/bin/nginxConsole" ]]; then
		sudo unlink /usr/bin/nginxConsole
		sudo ln -s ${bin_path}/nginxConsole /usr/bin/nginxConsole
		echo -e "[ \e[32mRESET\e[0m ] nginxConsole exists, reset it"
	else
		sudo ln -s ${bin_path}/nginxConsole /usr/bin/nginxConsole
		echo -e "[ \e[32mOK\e[0m ] link success"
	fi
	
	echo -e "[ \e[36mwebConsole\e[0m ] link \e[33m${bin_path}/webConsole\e[0m to \e[33m/usr/bin/webConsole\e[0m"
	if [[ -h "/usr/bin/webConsole" ]]; then
		sudo unlink /usr/bin/webConsole
		sudo ln -s ${bin_path}/webConsole /usr/bin/webConsole
		echo -e "[ \e[32mRESET\e[0m ] webConsole exists, reset it"
	else
		sudo ln -s ${bin_path}/webConsole /usr/bin/webConsole
		echo -e "[ \e[32mOK\e[0m ] link success"
	fi
}


function main() {
	echo -e "================ \e[32mInitializing\e[0m ================"
	getHome

	echo ""
	echo -e "============= \e[32mInstalling Package\e[0m ============="
	installPackage

	echo ""
	echo -e "============== \e[32mCreating Linking\e[0m =============="
	createLinking

	printHelp
}

main
