#!/bin/bash

all() {
	all_subnets=`ip -4 a |grep inet|cut -f6 -d ' '|tail -n +2|cut -f 1-3 -d .`
	counter=0
	if [ -z "$all_subnets" ]
	then
		echo "There are no interfaces."
		exit
	fi
	echo Loading...
	for var in $all_subnets
	do
	let counter+=1
	nmap -sn ${var}.0/24|grep "scan report"
	done
	echo "There are $counter subnets"
}

target() {
	echo "Type IP or domain of the target: "
	read
	nmap -sT $REPLY | tail -n +4
}

if [ "$#" == "0" ]
then
	echo -e "Please, enter an argument.\nType --all to displays the IP addresses and symbolic names of all hosts in the current subnet."
	echo "Type --target to displays a list of open system TCP ports."
elif [ "$1" = "--all" ]
then
	all
elif [ "$1" = "--target" ]
then
	target
else
	echo "Wrong argument."
fi
