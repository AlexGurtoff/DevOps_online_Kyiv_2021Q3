**First of all, I created an AWS account and studied the basic manuals for working with AWS. Also, I created budget alerts so that I don't accidentally use more than a 1$**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Budget_allerts.jpg)

**Then, I reviewed the 10-minute example how to launch a Linux VM with Amazon Lightsail and repeated it. **

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Create_an_instance.jpg)

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/create_an_instance2.jpg)

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Connect_to_VM.jpg)

**And connected via SSH using my private key.**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Connect_to_VM_via_MobaXterm.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Connect_to_VM_via_MobaXterm2.jpg)

**Then I launched another VM using the EC2. I used a t2.micro instance and CentOS operating system. Here you are able to see the created instance and connection to it via SSH**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/CentOS_t2micro_created.jpg)

**Then I created a snapshot of my instance and as well as AMI of instance. For a backup of the entire system, it is better to use AMI. Because we can restore the entire instance. In the case of snapshots, we can only recover the volume. **
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Creating_a_snapshot.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/AMI_create.jpg)

**Thereafter, I created, attached and mounted a disk(volume) to my second instance and created some data inside it.**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Disk_attach.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Mount_disk_and_create_file.jpg)

**Then I launched a 3rd instance from my AMIs**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Launch_instance_from_backup.jpg)

**So, I detached the disk from the 2nd instance and attached it to the 3rd. Also I checked data inside this volume. All has been succesfully saved.**
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.2/Disk_D_attached_to_3rd_instance.jpg)