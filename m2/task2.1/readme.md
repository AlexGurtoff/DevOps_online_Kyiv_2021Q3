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




The following is a summary of group commands: Start, Pause, Reset, Close (save state, send shutdown signal, poweroff), Discard Saved State, Show in File System, Sort.