#!/bin/bash

backup(){

rsync --archive --delete --out-format="%t %o %n" $1 $2 >> ~/log_backup.txt 2>>~/error_log_backup.txt

}

if [ "$#" -ne "2" ]
then
	echo "Please, specify source dir and destination dir"
else
	backup "$1" "$2"
fi
