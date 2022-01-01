#!/usr/bin/bash

for i in [ Ubuntu Debian ]
do
	if [ $(lsb_release -is) = $i ]
	then
		sudo apt install build-essential nasm
	fi
done

for i in [ CentOS Fedora ]
do
	if [ $(lsb_release -is) = $i ]
	then
		sudo yum install gcc nasm
	fi
done
