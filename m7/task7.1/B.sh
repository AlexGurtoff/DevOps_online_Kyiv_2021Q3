#!/bin/bash

popular_ip(){
echo "The most requests from ip: "
awk '{print $1}' $1 | sort |uniq -c | sort -rh | head -n 1

}

popular_page(){

echo "The most popular page is: "
awk '{print $7}' $1 | sort | uniq -c| sort -rh | head -n 1 | cut -f 7 -d ' '

}


requests_from_each_ip(){

echo "Requests from each IP: "
awk '{print $1}' $1 | sort |uniq -c | sort -rh

}


wrong_page(){

echo "Non-existent pages: "
grep 404 $1 | awk '{print $7}' | uniq

}


popular_time(){

echo "Time when site got the most requests: "
awk '{print $4}' $1|cut -f 1-3 -d ":"| cut -f2 -d "[" | uniq -c | sort -gr

}

bots(){

echo "These bots have visited the site"
grep -i bot $1 | awk '{print $1 " - " $12,$13,$14,$15,$16}'

}

if [ "$#" == "0" ]
then
	echo "Please, specify a log file as an argument"
else
	popular_ip $1
	popular_page $1
	requests_from_each_ip $1
	wrong_page $1
	popular_time $1
	bots $1
fi
