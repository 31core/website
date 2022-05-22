#!/usr/bin/bash

os_release=$(lsb_release -is)

for i in [ Ubuntu Debian ]
do
	if [ $os_release = $i ]
	then
	    sudo apt update
		sudo apt install build-essential nasm
	fi
done

for i in [ CentOS Fedora ]
do
	if [ $os_release = $i ]
	then
		sudo yum install gcc nasm make qemu
	fi
done

#macOS
if [ $(uname -a) = Darwin ]
then
	brew install nasm qemu
fi
