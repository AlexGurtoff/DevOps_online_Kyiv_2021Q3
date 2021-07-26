1) Analyze the structure of the /etc/passwd and /etc/group file, what fields are 
present in it, what users exist on the system? Specify several pseudo-users, how 
to define them?

------------


**Answer:**
**/etc/passwd** file has the following structure: 
alex: x : 1000 : 1000 : alex , , , : /home/alex:/bin/bash
Username
Password
UID
GID
GECOS
Home Directory
Login shell
**/etc/group** file has the following structure:
adm: x : 4 : syslog,alex
Where:
**group_name:** It is the name of group. If you run ls -l command, you will see this name printed in the group field.
**Password:** Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.
**Group ID (GID):** Each user must be assigned a group ID. You can see this number in your /etc/passwd file.
**Group List:** It is a list of user names of users who are members of the group. The user names, must be separated by commas.

To define users you can use command `adduser` or `useradd`

`useradd` is a low-level utility for creating users in Linux.

`adduser` is a simpler solution for creating users and is in fact an add-on over useradd, groupadd and usermod.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/etc_passwd.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/etc_group.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/Define_users.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/passwd_file_with_new_users.jpg)

------------

2) What are the uid ranges? What is UID? How to define it?

------------


**Answer:**
A **UID** (user identifier) is a number assigned by Linux to each user on the system. This number is used to identify the user to the system and to determine which system resources the user can access.
UID 0 (zero) is reserved for the root.
UID 1–999 are reserved by system for administrative and system accounts/groups.
UID 1000+ are used for user accounts.
You can change the UID with the `usermod` command as follows:
`usermod -u 1111 testEPAM`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/usermod-u.jpg)

------------

3) What is GID? How to define it?

------------


**Answer:**
Groups in Linux are defined by **GIDs** (group IDs).
GID 0 (zero) is reserved for the root group.
GID 1–99 are reserved for the system and application use.
GID 100+ allocated for the users group.
You can change the UID with the `groupmod` command as follows:
`groupmod -g 1111 testEPAM`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/groupmod-g.jpg)

------------

4) How to determine belonging of user to the specific group?

------------


**Answer:**
Command `groups`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/groups_alex.jpg)

------------

5) What are the commands for adding a user to the system? What are the basic 
parameters required to create a user?

------------



I answered on this question in the first paragraph

------------



6) How do I change the name (account name) of an existing user?

------------


**Answer:**
You can change the name of an existing user with the following command
`usermod -l new_username old_username`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/usermod-l.jpg)

------------

7) What is skell_dir? What is its structure?

------------


**Answer:**
Directory /etc/skel/ (skel is derived from the skeleton) is used to initiate home directory when a user is first created. A sample layout of skel user files is as shown below:

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/skel_structure.jpg)

------------

8) How to remove a user from the system (including his mailbox)?

------------


**Answer:**
Here is 2 commands `userdel` and `deluser`. I showed the work of these commands in the screenshots below.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/delete_user.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/userdel_%20command.jpg)

------------

9) What commands and keys should be used to lock and unlock a user account?

------------


**Answer:**
To lock or unlock users you can use `passwd` command with -l and -u keys. To check the status of user you can use -S key.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/lock_and_unlock_user.jpg)

------------

10) How to remove a user's password and provide him with a password-free 
login for subsequent password change?

------------


**Answer:**
You can use the `passwd -d` command to remove the password, and `passwd -e` to expire it. In this case, the user will be able to log in without a password and then system will ask him to enter a new password

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/del_and_expire_passwd.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/log_and_set_new_passwd.jpg)

------------

11) Display the extended format of information about the directory, tell about 
the information columns displayed on the terminal.

------------


**Answer:**
Here you can see the execution of the "ls -la" command. You can see the following file information: The file type, The file permissions, Number of hard links to the file, File owner, File group, File size, Date and Time when file was created or changed, File name. Blue names are directories. Names with dot before name are hidden.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/ls-la.jpg)

------------

12,13,14,15) What access rights exist and for whom (i. e., describe the main roles)? 
Briefly describe the acronym for access rights. What is the sequence of defining the relationship between the file and the user? What commands are used to change the owner of a file (directory), as well as the mode of access to the file? Give examples, demonstrate on the terminal. What is an example of octal representation of access rights? Describe the umask command.

------------


**Answer:**
On a Linux system, each file and directory is assigned access rights for the owner of the file, the members of a group of related users, and everybody else. Rights can be assigned to read a file, to write a file, and to execute a file (i.e., run the file as a program).

To see the permission settings for a file, we can use the `ls` command.

In the diagram below, we see how the first portion of the listing is interpreted. It consists of a character indicating the file type, followed by three sets of three characters that convey the reading, writing and execution permission for the owner, group, and everybody else.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/access_rights.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/diagram.jpg)

------------

The `chmod` command is used to change the permissions of a file or directory. There are two ways to specify the permissions. Octal notation and symbolic.

It is easy to think of the permission settings as a series of bits (which is how the computer thinks about them). Here's how it works:

rwx rwx rwx = 111 111 111
rw- rw- rw- = 110 110 110
rwx --- --- = 111 000 000

and so on...

rwx = 111 in binary = 7
rw- = 110 in binary = 6
r-x = 101 in binary = 5
r-- = 100 in binary = 4

Also you can change permission settings in a symbolic way, for example:
`chmod ugo+rwx file`
So, let's practice:

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/access_rights_practice.jpg)

------------

**Umask**, or the user file-creation mode, is a Linux command that is used to assign the default file permission sets for newly created folders and files.

**How Umask Works**
The umask command masks permission levels by qualifying them with a certain value. To explain further how the umask value is applied, we will illustrate with an example. Let’s say that we want to set the default permissions for all new files or folders to 644 and 755. We would then use the following command.
`[root]# umask 022`
The number "2" permission (write permission) will be "filtered" from the system’s default permissions of 666 and 777 (hence the name “mask.”) From now on, the system will now assign the default permissions of 644 and 755 on new files and directories. Simply put, to calculate the permission bits for a new file or directory, we just subtract the umask value from the default value, like so.

666 - 022 = 644
777 - 022 = 755

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/umask_table.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/umask.jpg)

------------

16) Give definitions of sticky bits and mechanism of identifier substitution. Give 
an example of files and directories with these attributes

------------


**Answer:**
**SUID** - if this bit is set, then when the program is running, the id of the user from which it was launched is replaced with the id of the file owner. In fact, it allows regular users to run programs as the superuser;
**SGID** - This flag works in a similar way, only the difference is that the user is considered a member of the group that the file is associated with, and not the groups to which he actually belongs. If the SGID flag is set to a directory, all files created in it will be associated with the directory group, not the user. This behavior is used to organize public folders;
**Sticky-bit** - This bit is also used to create shared folders. If it is installed, then users can only create, read and execute files, but cannot delete files owned by other users.

You can set these right with `chmod` command.
For example, `chmod u+s file1`:

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.2/SUID_SGID_Sticky_bit.jpg)

------------

17) What file attributes should be present in the command script?

------------


**Answer:**
The command script must have the "x" attribute to run the script.