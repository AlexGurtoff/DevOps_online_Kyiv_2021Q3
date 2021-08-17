# A.
```
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
```

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/A_sh.jpg)

------------

# B.
```
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
```

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/B_sh.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/B_sh2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/B_sh3.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/B_sh4.jpg)

------------

# C.
```
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
```

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/C_sh.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/crontab.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/log_backup.jpg)

------------

.sh files:
[A.sh](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/A.sh "A.sh")
[B.sh](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/B.sh "B.sh")
[C.sh](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m7/task7.1/C.sh "C.sh")