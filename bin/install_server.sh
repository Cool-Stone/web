#!/bin/sh

# kill old server
current=`ps aux | grep main | grep -v 'grep' | awk '{ print $2 }'`
for id in $current; do
	echo "Killing Process ID: ${id}";
	sudo kill -9 ${id};
done

# restart
sudo nohup python /home/ubuntu/web/main.py &

