I created 3 VMs. One with NAT + Internal adapters and two only with Internal Network.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/Ubuntu-ServerVM1%20-%20Settings.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/Ubuntu-ServerVM1%20-%20Settings2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/Ubuntu-ServerVM2%20-%20Settings.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/Ubuntu-ServerVM3%20-%20Settings.jpg)

------------

I have such settings in netplan for VM2 and VM3

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/VM2-VM3_netplan.jpg)

------------

Firstly, I chose VBoxManage to install DHCP server

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/DHCP_Server_Create_VBoxManage.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/VM1_VM2-Ipa.jpg)

------------

The second option is to install dnsmasq. So I installed it on VM1 and configure in `/etc/dnsmasq.conf` file 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/dnsmasq-dhcp-settings.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/dnsmasq.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/dnsmasq_ips.jpg)

------------

To configute dnsmasq as a dns-server we need to set iptables rules

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/iptables_rules.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/iptables_rules2.jpg)

------------

And also edit `/etc/resolv.conf` file. By the way, we need to stop systemd-resolved service because it uses 53 port too and conflicts with the dnsmasq service 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/resolv_conf.jpg)

------------

So, lets check how it works 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.2/test_dns_dig.jpg)

------------

