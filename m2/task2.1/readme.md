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

Also I want to describe some features of the most popular hypervisors

**Microsoft Hyper-V**

- Persistent memory support.
- Shielded VM updates.
- Simple Two-Node clusters.
- ReFS Deduplication.
- Storage Spaces Direct improvements.
- Windows Admin Center.
- Encrypted subnets.

**VMware vSphere**

- vCenter Server: A centralized management tool used to configure, provision and manage virtual IT environments.
- vSphere Client: vSphere 6.7 has the final version of Flash-based vSphere Web Client. Newer workflows in the updated vSphere Client release includes vSphere Update Manager, Content library, vSAN, Storage policies, Host profiles, VMware vSphere Distributed Switch topology diagram and Licensing.
- vSphere SDKs: Provides interfaces for third-party solutions to access vSphere.
- VM File System: Cluster file system for VMs.
- Virtual SMP: Enables a single VM to use multiple physical processors at a time.
- vMotion: Enables live migration with transaction integrity.
- Storage vMotion: Enables VM file migration from one place to other without service interruption.
- High Availability: If one server fails, VM is shifted to other server with spare capacity to enable business continuity.
- Distributed Resource Scheduler (DRS): Assigns and balances compute automatically across hardware resources available for VMs.
- Fault Tolerance: Generates copy of primary VM to ensure its continuous availability.
- Distributed Switch (VDS): Spans multiple ESXi hosts and enables considerable reduction of network maintenance activities.

**XenServer**

- Site Recovery
- Host Failure Protection
- Multi-server management
- Dynamic Memory Control
- Active Directory Integration
- Role-Based Administration and Control (RBAC)
- Mixed Resource Pools with CPU Masking
- Distributed Virtual Switch Controller
- In Memory read caching
- Live VM migration & Storage XenMotion 

## PART 2. WORK WITH VIRTUALBOX

We downloaded and installed virtualbox and ubuntu. Then we created a virtual machine(VM) and installed ubuntu on it, after which we launched ubuntu.
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Install_and_run.jpg)

In this screenshot you are able to see the process of cloning a VM

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Clone.jpg)

A group of two VMs was created here

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Group.jpg)

Here you are able to see the result of creating snapshots

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m2/task2.1/Snapshots.jpg)

Ubuntu was exported to .ova file

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