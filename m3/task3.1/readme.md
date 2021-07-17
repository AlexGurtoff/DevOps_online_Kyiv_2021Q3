## Part 1
**First of all, I created an ubuntu-server virtual machine, then I installed and configured the  mysql server for this OS. Also I opened a ssh connection to my server and 3306 port for mysql database, as a result of which I was able to connect to the database by Navicat via ssh tunnel from my Host OS.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/setup-ubuntu-server-and-install-mysql-via-ssh.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Navicat-connect-to-mysql.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/random-table-from-mysql-via-navicat.jpg)

------------


**I chose travel as my subject for the database schema. So, I created database "Travel" and tables for it. Also you are able to see the database model on the screenshot. For fill in tables I used http://www.generatedata.com/**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Create-database.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Database-Model.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Fill-tables.jpg)

------------
** There are some queries with SELECT operator and WHERE,GROUP BY,ORDER BY.**
 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Query1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Query2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Query3.jpg)

------------

**And also some DDL DML DCL queries**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Some-DML-Queries.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Some-DDL-Queries.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Some-DCL-Query-and-create-user.jpg)

------------

**Then I tested the connection to my database with a new user "reader" and tried to change the data, it was unsuccessful because this user can only SELECT the database. Also I created one more user and tested him too.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Test-connection-for-reader-and-try-to-change-data.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Create-another-user.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Test-connection-for-DROPER.jpg)


------------

**There is a selection from main table DB**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/SELECT-from-main-db.jpg)

------------

## Part 2

**Then I made the backup of my database using console and also using Navicat GUI. After that I deleted some data and restore it from my backup.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dump-Base.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dump-console-and-restore1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dump-console-and-restore2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dump-Restore.jpg)

------------

**Then I transfered my local database to RDS AWS. To do this, I first created an empty database, connected to it and restored the backup. Also I executed the same queries. And at the end I dumped the database. By the way, to restore my database I used EC2 instance which was created  in the same AWS Region as RDS. I connected to this instance via SSH, then I executed command to connect to RDS
`mysql -h host_name -P 3306 -u db_master_user -p`
And at the mysql prompt, I run the `source` command and passed it the name of my database dump file to load the data into the Amazon RDS DB instance
`mysql> source DumpTravel.sql;`**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/RDS-Mysql.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/AWS-Connect.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Execute-sql-queries-aws.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/restore_via_EC2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/restore_via_EC2_2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dump-AWS.jpg)

------------

## Part 3
**In this part I created an Amazon DynamoDB Table, then I entered some data into this table and tested Query and Scan options.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Dynamo-DB-Table.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Our-Dynamo-Table.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Scan-query.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Scan-query2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m3/task3.1/Query-DynamoDB.jpg)