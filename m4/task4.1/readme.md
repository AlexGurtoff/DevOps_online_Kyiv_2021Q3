**Топология №1. 
4 ПК и ХАБ. Здесь мы можем увидеть, что пакеты передаются на все подключенные ПК.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/ICMP_Sent.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Packet_info.jpg)

------------

**Тополия №2.
6 ПК, 2 ХАБА и сервер. Здесь суть работы такая же. Хаб принимает пакеты и рассылает его между всемя возможными соеденениями. Пакеты успешно передаются через 2 ХАБа и доходят до цели.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project2_test.jpg)

------------

**Тополия №3.
4 ПК и switch(коммутатор). Отличия топологии 1 и 3 заключатся в алгоритме работы коммутатора(switch) и концентратора(hub). Концентратор рассылает пакеты всем устройствам которые соединены с ним. Коммутатор в свою же очередь запоминает MAC адрес каждого устройста и передает пакет тому устройству, для которого он изначально и был выслан. Концентратор работает на первом уровне OSI (Physical), коммутатор работает на втором уровне OSI (Data Link)**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project3_test.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/packet_info_project3.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/test_with_no_ip.jpg)

------------

**Топология №4.
8ПК и 2 коммутатора. Для подключения второго коммутатора нам нужно было добавить дополнительный Fast-Ethernet порт. После этого можем подключать коммутатор и тестировать топологию. Пакеты передаются успешно.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project4_test.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/packet_info_project4.jpg)

------------

Топология №5.
8 ПК, 2 коммутатора и 1 маршрутизатор(Router).