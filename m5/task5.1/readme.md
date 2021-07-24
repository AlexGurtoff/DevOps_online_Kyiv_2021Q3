## Part 1.
2) This command change /etc/passwd file, which has the following structure:
alex: x : 1000 : 1000 : alex , , , : /home/alex:/bin/bash
1. Username
2. Password
3. ID
4. GID
5. GECOS
6. Home Directory
7. Login shell
On most modern systems, password field is set to x, and the user's password is stored in the /etc/shadow file.
Users with ID less than 1000 are system users, they were created during the installation of some services for their safer work.

------------


![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/Log_as_a_root.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/change_personal_info.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/change_personal_info2.jpg)

------------

5) `passwd` - change user password. 
  -d, --delete
           Delete a user's password (make it empty). This is a quick way
           to disable a password for an account. It will set the named
           account passwordless.
	-e, --expire
           Immediately expire an account's password. This in effect can
           force a user to change their password at the user's next
           login.
		   
`finger` - user information lookup program
-l
Produces a multi-line format displaying all of the information
-s      
Finger displays the user's login name, real name, terminal nameand write status (as a * after the terminal name if writepermission is denied), idle time, login time, office location andoffice phone number.
Login time is displayed as month, day, hours and minutes, unlessmore than six months ago, in which case the year is displayedrather than the hours and minutes.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/passwd-e.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/finger-s.jpg)

------------

Here you can see the execution of the "ls -la" command. You can see the following file information: The file type, The file permissions, Number of hard links to the file, File owner, File group, File size, Date and Time when file was created or changed, File name. Blue names are directories. Names with dot before name are hidden.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/ls-la_home_directory.jpg)


------------

## Part 2.
1) `tree` - list contents of directories in a tree-like format.
-P pattern
List only those files that match the wild-card pattern.
-L level
Max display depth of the directory tree.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/tree-ap.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/tree-aL.jpg)

------------

2) `file` - determine file type

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/file_command.jpg)

------------

3) For go back to your home directory from anywhere in the filesystem you have to use `cd ~` command

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/Navigation.jpg)

------------

5)

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/file_tree_root.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/CP_file.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/rm_filetree.jpg)

------------

6) A symbolic or soft link is an actual link to the original file, whereas a hard link is a mirror copy of the original file. If you delete the original file, the soft link has no value, because it points to a non-existent file. But in the case of hard link, it is entirely opposite. If you delete the original file, the hard link can still has the data of the original file. Because hard link acts as a mirror copy of the original file.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/bash_history_copied.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/links_create_and_cat_them.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/change_data_softlink.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/mv_links_and_delete_labwork2.jpg)

------------

7) The `locate` command is used to find files by their filename. The locate command is lightning fast because there is a background process that runs on your system that continuously finds new files and stores them in a database.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/locate_squid_traceroute.jpg)

------------

8) `lsblk` lists information about all available or the specified block devices.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/lsblk.jpg)

------------

9) `wc` - print the number of newlines, words, and bytes in files

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/wc_and_grep.jpg)

------------

10)

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/find_etc_host.jpg)

------------

11)

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/ls_and_grep.jpg)

------------

12) `more` is a filter for paging through text one screenful at a time.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/save_content_into_file_and_view_it.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/more_command.jpg)

------------

13) Linux supports three types of hardware device: character, block and network. Character devices are read and written directly without buffering, for example the system's serial ports /dev/cua0 and /dev/cua1. Block devices can only be written to and read from in multiples of the block size, typically 512 or 1024 bytes. Block devices are accessed via the buffer cache and may be randomly accessed, that is to say, any block can be read or written no matter where it is on the device. Block devices can be accessed via their device special file but more commonly they are accessed via the file system. Only a block device can support a mounted file system. 
The first character in the first column c indicates the type of the file, in the given character device. For regular files the character is -, for directories - d , for block devices - b

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/ls-l-dev.jpg)

------------

14) There are 7 different file types within the Linux operating system.
-- : regular file
d : directory
c : character device file
b : block device file
s : local socket file
p : named pipe
l : symbolic link
For example, you can see links here:

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/link_type.jpg)

------------

15)

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.1/List_the_first_5_directory_files.jpg)

------------

