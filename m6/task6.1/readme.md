**Firstly, we need to configure our virtual machines settings in virtual box. VM1 with NAT adapted and Internal. VM2 only with Internal adapter. Also I configure port forwarding for SSH.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/VM1_settings1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/VM1_settings2.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/VM2_settings.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/SSH_TO_VM1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/SSH_TO_VM1_done.jpg)

------------

**Then we must allow forwarding, to do this we need to uncomment string `net.ipv4.ip_forward=1` in `/etc/sysctl.conf file`**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/uncomment_forwarding.jpg)

------------

**Now we need to configure iptables. So, I created few rules to allow forwarding and masquerade. Masquerading is the substitution of some parameters in the headers of IP packets, which allows machines that do not have real IP addresses to fully work on the Internet.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/iptables_settings.jpg)

------------

**Since the release of Ubuntu 17.10, the `netplan` utility is used to manage network configurations. Previously, for these purposes, the ifupdown script was used, the configuration files of which were located in the `/etc/network/interfaces` folder. So, we need to configure netplan on our virtual machines, for this i ran next command `sudo nano /etc/netplan/00-installer-config.yaml` **

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/netplan_VM1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/netplan_VM2.jpg)

------------

**Now test connection between VM2 and VM1.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/connection_between_VM2_to_VM1.jpg)

------------

**Ping google.com from VM2**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/ping_google_com_from_VM2.jpg)

------------

**Route to host from VM2**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/route_to_host_from_VM2.jpg)

------------

**To determine which resource has an IP address 8.8.8.8 we can use `nslookup` or `dig`**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/8_8_8_8_address.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/8_8_8_8_address_dig.jpg)

------------

**To determine which address belongs to epam.com we can use the same commands.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/epam_com.jpg)

------------

**Here you can see default gateway and routing table of my host machine**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/def_gw_host.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/route_host.jpg)

------------

**And here you can see traceroute to google.com from VM1 and VM2.**

------------


![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m6/task6.1/traceroute_google_from_VM2_and_VM1.jpg)

------------

