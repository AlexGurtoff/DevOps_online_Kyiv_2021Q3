# Task 4.2
## Задание 1:
Я построил корпоративную сеть, которая состоит из двух зданий по 2 этажа в каждом. Каждая подсеть состоит из 5-ти компьютеров и коммутатора. Для соединения зданий я использовал 2 роутера и настроил RIP маршрутизацию. Данное решение можно использовать даже если здания находятся далеко друг от друга. 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/task4_2_1_scheme.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/router_settings.jpg)

**Здесь можно увидеть успешную передачу пакетов в рамках одного здания, но разных этажей**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/PC3-PC6_in_one_building_successful.jpg)

**А здесь можно увидеть успешную передачу пакетов между двумя разными зданиями**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/PC3-PC11_between_2_buildings_successful.jpg)

**Ping через CMD между двумя зданиями. Потерь пакетов нет.**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/CMD_ipconfig_and_ping1.jpg)

------------


## Задание 2:

Я построил корпоративную сеть, которая находится в одном 4-ех этажном здании. Каждый этаж состоит из двух рабочих груп, который разделены на подсети. Для соединения этажей я использовал 1 маршрутизатор и топологию Router on a stick (маршрутизатор на палочке) - где роутер физически подключен к сети только одним проводом, при этом обслуживает несколько подсетей. Топология реализуется благодаря тому, что единственный имеющийся провод является trunk-ом(служит для передачи трафика нескольких VLAN через один канал и обеспечивают им доступ ко всей сети.) и может различать фреймы из разных vlan, таким образом для каждого vlan создается свой подинтерфейс.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/task4_2_2_scheme.jpg)

**В каждом коммутаторе были созданы VLANы. В каждый из VLAN были добавлены соответствующие PC.**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/Configure_switches_VLANS.jpg)

**Используя CLI маршрутизатора я создал и настроил subinterfaces. Подинтерфейсы рассматриваются роутером как отдельные, самостоятельные интерфейсы и не смотря на то что они виртуальные, настраиваются они аналогично физическим интерфейсам:**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/Route_interface_conf.jpg)

**Проверяем работу сети:**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/PC24-PC31_successful.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/Packet_info_24.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m4/task4.2/PC1-PC28_successful.jpg)

------------
## Задание 3:
