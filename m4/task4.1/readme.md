**Топология №1. 
4 ПК и ХАБ. Здесь мы можем увидеть, что пакеты передаются на все подключенные ПК.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/ICMP_Sent.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Packet_info.jpg)

------------

**Топология №2.
6 ПК, 2 ХАБА и сервер. Здесь суть работы такая же. Хаб принимает пакеты и рассылает его между всемя возможными соеденениями. Пакеты успешно передаются через 2 ХАБа и доходят до цели.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project2_test.jpg)

------------

**Топология №3.
4 ПК и switch(коммутатор). Отличия топологии 1 и 3 заключатся в алгоритме работы коммутатора(switch) и концентратора(hub). Концентратор рассылает пакеты всем устройствам которые соединены с ним. Коммутатор в свою же очередь запоминает MAC адрес каждого устройста и передает пакет тому устройству, для которого он изначально и был выслан. Концентратор работает на первом уровне OSI (Physical), коммутатор работает на втором уровне OSI (Data Link)**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project3_test.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/packet_info_project3.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/test_with_no_ip.jpg)

------------

**Топология №4.
8ПК и 2 коммутатора. Для подключения второго коммутатора нам нужно было добавить дополнительный Fast-Ethernet порт. После этого можем подключать коммутатор и тестировать топологию. Пакеты передаются успешно.**

------------
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Add_aditional_port.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project4_test.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/packet_info_project4.jpg)

------------

**Топология №5.
8 ПК, 2 коммутатора и 1 маршрутизатор(Router) с двумя подсетями (192.168.0.5 и 192.168.1.5). Прописываем IP 192.168.1.Х для второй подсети (PC4-PC7). После чего в IP Configuration прописываем шлюз для каждого ПК. Для 1 подсети это будет 192.168.0.5, а для второй - 192.168.1.5. Соединяем маршрутизатор с коммутаторами и эти же самые адреса указываем на портах роутера, проверяем работоспособность топологии.**

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/IP_config_project5.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Router_settings.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project5_test.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Packet_info_project5.jpg)

------------

**Пакеты передались успешно. Маршрутизатор работает на 3 уровне OSI и использует IP адреса для передачи информации. С помощью него можно соединять разные подсети.**

**Ссылки на .pkt файлы с проектами:**
[Топология-1](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project-1.pkt "Топология-1")
[Топология-2](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project-2.pkt "Топология-2")
[Топология-4](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project_3.pkt "Топология-4")
[Топология-5](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.1/Project_4.pkt "Топология-5")