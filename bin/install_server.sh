#!/bin/sh

# kill old server
function Stop() {
	local current=`ps aux | grep main | grep -v 'grep' | awk '{ print $2 }'`
	for id in $current; do
		echo "Killing Process ID: ${id}";
		sudo kill -9 ${id};
	done
}

# restart
function Start() {
	sudo nohup python /home/ubuntu/web/main.py &
}

# helper
function Helper() {
	echo "Usage: $1 <start | stop | restart>"
}

if [[ $# != 1 ]]; then
	Helper
	exit 1
else
	case "$1" in
		"start")
			Start
			;;
		"stop")
			Stop
			;;
		"restart")
			Stop
			Start
			;;
		*)
			Helper
			;;
	esac
fi
	
