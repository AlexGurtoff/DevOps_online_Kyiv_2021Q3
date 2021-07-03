##  Part 1. HYPERVISORS
####   What are the most popular hypervisors for infrastructure virtualization?

------------

- The leader in the Tier-1 hypervisors is VMware with their vSphere/ESXi product - available in a free edition and 5 commercial editions.
- Microsoft Windows Server Hyper-V - Hyper-V is available in both a free edition (with no GUI and no virtualization rights) and 4 commercial editions – Foundations (OEM only), Essentials, Standard, and Datacenter. 
- Xen is a type-1 bare-metal hypervisor. Just as Red Hat Enterprise Virtualization uses KVM, Citrix uses Xen in the commercial XenServer. Xen supports the virtualization of x86 IA64, ARM, among other architectures. Xen has been used in the virtualization of a wide array of guest OS. A few of the OS supported by Xen are Windows, Solaris, and other versions of the BSD OS.
- Oracle VirtualBox This type hypervisor can run on any OS such as Solaris, Linux, Mac, and Windows. It is compatible with both x86 and x64 OS, and it is quite portable. It allows virtual machines to be imported or exported using the Open Virtualization Format (OVF), which is a standout feature of this product.

------------
#### Briefly describe the main differences of the most popular hypervisors.

------------
| Resourse |Hyper-V   |XenServer   |VSphere   |
| ------------ | ------------ | ------------ | ------------ |
|Virtual CPUs per VM   |64   |16   |8   |
|Memory per VM   |1TB   |128GB   |32GB   |
|Active VMs per Host   |1024   |50-130   |512   |
|Maximum VMs   |4000   |800-960   |N/A  |

## PART 2. WORK WITH VIRTUALBOX

We downloaded and installed virtualbox and ubuntu. Then we created a virtual machine(VM) and installed ubuntu on it, after which we launched ubuntu.
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Install_and_run.jpg)

In this screenshot you are able to see the process of cloning a VM

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Clone.jpg)

A group of two VMs was created here

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Group.jpg)

Here you are able to see the result of creating snapshots

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Snapshots.jpg)

Ubuntu was exported to .voa file

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Exported.jpg)

Here is an example on how to configure USB settings. We made USB filter with Vendor ID wich related to SteelSeries mouses, so now all devices produced by SteelSeries will be available to the guest

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Configure_USB.jpg)

After that, we configured the shared folder to exchange data between the virtual machine and the host

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Shared_Folder.jpg)

Then we checked all possible network modes that available in virtualbox. To check, we used the ping command. Here is one example of how we tested this for "Host Only Adapter"

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Example_of_Testing_VM1-VM2.jpg)

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Example_of_Testing_Windows-VM1.jpg)

| Mode  |VM->Host|VM<-Host   |VM1<->VM2  |VM->Net   |VM<-Net   |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| Not attached  |  - |  - |  - | -  | -  |
| Host-Only  | +  |  + | +  | -  | -  |
| Internal  |  - |  - | +  | -  | -  |
|Bridged   | +  | +  | +  | +  | +  |
|NAT  | +  | Only if port is open  |  - | +  | Only if port is open  |
|NAT Network  | +  | Only if port is open  | +  | +  | Only if port is open  |

We also tested the ability to manage a VM using the CLI. For example, here you are able to see the process of starting the VM from the command line

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Startvm.jpg)

## PART 3. WORK WITH VAGRANT

We downloaded and installed vagrant **2.2.15** (version **2.2.16** was unstable and errors occurred while working with it)
Here is the first launch of vagrant. We also run the precise64 server
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Vagrant.jpg)

Here is a test to connect to this server via SSH and date command in the terminal
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/MobaXterm.jpg)

After that we stopped and destroyed VM
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Stop_and_destroy_VM.jpg)

Then we created our own vagrant box from the virtual machine that we had in the virtualbox

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Vagrant2.jpg)

And here is the process of building this VM

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Up_myownbuild.jpg)

And finally, checking the connection via SSH

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/VM_and_MobaXTerm.jpg)