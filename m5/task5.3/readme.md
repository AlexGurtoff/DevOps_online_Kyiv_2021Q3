## Part 1
1) How many states could has a process in Linux?

------------


**Answer:**

Linux has basically 5 states:
- Running/Runnable (R): running processes are processes using a CPU core right now, a runnable process is a process that has everything to run and is just waiting for a CPU core slot.
- Sleeping: a sleeping process is a process waiting for a resource to be available (for example, a I/O operation to complete) or an event to happen (like a certain amount of time to pass). The difference between process in Interruptible Sleep (S) state and Uninterruptible Sleep (D) is that the former will wake up to handle signals while the former won't. We'll talk about signals in a moment, but let's suppose that a process is waiting for a I/O operation to complete before wake up. If in the meantime, it receives a signal to terminate (SIGKILL), it will terminate before having the chance to handle the requested data. That's why I/O operations normally go to uninterruptible sleep while waiting for the result: they will wake up with when the operation is ready, handle the result and, only then, check for any pending signal to handle. Processes that can be terminated before the wake up condition is fulfilled without any consequence usually go to interruptible sleep instead.
- Stopped (T): a process becomes stopped when it receives the SIGSTOP signal (not unlike when you press <ctrl>+z in the shell, although <ctrl>+z sends a SIGTSTP instead). When stopped, the process execution is suspended and the only signals it will handle are SIGKILL and SIGCONT. The former will remove the process permanently, while the later will put the process back to the Running/Runnable state (like when you run fg or bg after pressing <ctrl>+z in the shell).
- Zombie (Z): When a process finishes with exit() system call, its state needs to be "reaped" by its parent (calling wait()); in the meantime, the child process remains in zombie state (not alive nor dead).

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/diagram.jpg)

------------

2) Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

------------
**Answer:**

`pstree` -  shows running processes as a tree.  The tree is rooted at
       either pid or init if pid is omitted.  If a user name is
       specified, all process trees rooted at processes owned by that
       user are shown.

To make the highlighted output of the current process, we need to run the command `pstree -h`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-h.jpg)

------------

3) What is a proc file system?

------------
**Answer:**

Proc file system (procfs) is virtual file system created on fly when system boots and is dissolved at time of system shut down.

It contains the useful information about the processes that are currently running, it is regarded as control and information centre for kernel.

The proc file system also provides communication medium between kernel space and user space.
You can type `ls -l /proc` command to see what processes are currently running. 

------------

4) Print information about the processor (its type, supported technologies, etc.).

------------
**Answer:**

`lscpu` gathers CPU architecture information from sysfs and /proc/cpuinfo. The command output can be optimized for parsing or for easy readability by humans.
The information includes, for example, the number of CPUs, threads, cores, sockets, and Non-Uniform Memory Access (NUMA) nodes. There is also information about the CPU caches and cache sharing, family, model, bogoMIPS, byte order, and stepping.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/lscpu1.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/lscpu2.jpg)

------------
5) Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc. 

------------
**Answer:**

`ps` displays information about a selection of the active processes. 
To set our own information formatting, we can specify the -o key

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-o.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-o-output.jpg)

------------
6) How to define kernel processes and user processes?

------------
**Answer:**

Kernel processes (or "kernel threads") are children of PID 2, so:

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/define_kernel_proc.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/define_kernel_proc2.jpg)

------------
7)  Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?

------------
**Answer:**
To check the status of proccess we need to type `ps -o stat`
So, here you can see only 3 procceses with status S, R+ and S+

S mean interruptible sleep (waiting for an event to complete)

R mean running or runnable (on run queue)

+    is in the foreground process group

Among the process groups in a session at most one can be the foreground process group of that session. The tty input and tty signals (signals generated by ^C, ^Z, etc.) go to processes in this foreground process group.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-o_stat.jpg)

------------
8) Display only the processes of a specific user

------------
**Answer:**

To display the processes of a specific user we can user key -u
`ps -u username`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-u.jpg)

------------
9) What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

------------
**Answer:**

You can use `ps -r` to  restrict the selection to only running processes.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/ps-r.jpg)

------------
10) What information does top command display?

------------
**Answer:**

The `top` program provides a dynamic real-time view of a running system.  It can display system summary information as well as a list of processes or threads currently being managed by the Linux kernel.  The types of system summary information shown and the types, order and size of information displayed for processes are all user configurable and that configuration can be made persistent across restarts.

------------

11) Display the processes of the specific user using the top command.

------------
Answer:

To display the processes of the specific user you need to use `top -u username` command or also you can use just a `top` command and then in an interactive mode type `u` and name of the user. 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/top-u-alex.jpg)

------------
12) What interactive commands can be used to control the top command? Give a couple of examples.

------------
**Answer:**
A  :Alternate-Display-Mode toggle

This command will switch between full-screen mode and alternate-display mode.  See topic 5. ALTERNATE-DISPLAY Provisions and the `g' interactive command for insight into `current' windows and field groups.

Z  :Change-Color-Mapping

This key will take you to a separate screen where you can change the colors for the `current' window, or for all windows.  For details regarding this interactive command see topic 4d. COLOR Mapping.

k  :Kill-a-task

You will be prompted for a PID and then the signal to send.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/top_z.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/top_A.jpg)

------------
13) Sort the contents of the processes window using various parameters (for example, the amount of processor time taken up, etc.)

------------
**Answer:**

To sort the processes, you can use the interactive command F and then choose sort column 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/top_sort_by_time.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/top_sort_by_mem.jpg)

------------
14)  Concept of priority, what commands are used to set priority?

------------
**Answer:**

Some processes may be highly CPU-intensive but not as important as others and hence can have a lower priority while others may or may not be highly CPU-intensive but are very important and hence should have higher priority.

For example- if there is a process A, which detects fraud with input data and there is another process B, which makes hourly backups of some data, then the priority(A) > priority(B)!

This ensures that if both A and B are running at the same time, A would be allocated more processing bandwidth.

**Priority value** — The priority value is the process actual priority which is used by the Linux kernel to schedule a task.
In Linux system priorities are 0 to 139 in which 0 to 99 for real-time and 100 to 139 for users.

**Nice value** — Nice values are user-space values that we can use to control the priority of a process. The nice value range is -20 to +19 where -20 is highest, 0 default and +19 is lowest.

The relation between nice value and priority is as such -

Priority_value = Nice_value + 20

There are two ways to do this:

Start the process with the nice value in the command as
`nice -n nice_val [command]`

or

Change the nice value of a running process using its PID using renice as `renice -n nice_val -p [pid]`

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/nice-n_15_bash.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/check_PR_NI_bash.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/renice_bash.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/renice_bash2.jpg)

------------
15) Can I change the priority of a process using the top command? If so, how?

------------
**Answer:**

Yes, you can. 

r  :Renice-a-Task

You will be prompted for a PID and then the value to nice it to.

------------
16) Examine the kill command. How to send with the kill command process control signal? Give an example of commonly used signals

------------
**Answer:**

The command `kill` sends the specified signal to the specified processes or process groups. If no signal is specified, the TERM signal is sent. The default action for this signal is to terminate the process. This signal should be used in preference to the KILL signal (number 9), since a process may install a handler for the TERM signal in order to perform clean-up steps before terminating in an orderly fashion. If a process does not terminate after a TERM signal has been sent, then the KILL signal may be used; be aware that the latter signal cannot be caught, and so does not give the target process the opportunity to perform any clean-up before terminating.

To see all possible signals you can type `kill -l`, there are 64 different singals. The most useful are 9) SIGKILL and 15) SIGTERM

SIGTERM - This signal requests the termination of the process. It can be ignored. The process is given time to complete correctly. If the program terminates correctly, then it used this time to save its state or work results and free up resources. In other words, it was not forced to stop.

SIGKILL - This signal causes the process to terminate immediately. The program cannot ignore this signal. Unsaved results will be lost.

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/kill_9_15_signals.jpg)

------------
17) Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to 
demonstrate the process control mechanism with fg, bg

------------
**Answer:**

The `jobs` utility shall display the status of jobs that were started in the current shell environment

If job control is enabled the `fg` utility shall move a background job from the current environment into the foreground.

If job control is enabled the `bg` utility shall resume suspended jobs from the current environment by running them as background jobs. If the job specified by job_id is already a running background job, the bg utility shall have no effect and shall exit successfully.

If the process was originally started in the usual way, it can be put into the background by doing the following:

1) Stop the execution of the command by pressing the key combination Ctrl + Z.

2) Bring the process to the background with the bg command.

`disown` - Removes the job from the shell active job table. i. e. the process continues to run in the background, but is no longer a job, this can be used when we need to close the terminal, but the process must continue to run.

All processes except at and batch are exited when you log off. If you want the process to continue running in the background after you log off, you need to use the nohup command. The nohup command has the following format:

`nohup command &`

So, I executed the command `nohup sleep 200 &`  from the user "alex" and logged out. Then I log in as a root and found this proccess. 

------------

![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/jobs_command.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/sleep_after_30_sec.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/sleep_after_30_sec.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/start_process_as_usual_and_go_bg.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/disown.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/nohup.jpg)
![](https://github.com/AlexGurtoff/DevOps_online_Kyiv_2021Q3/blob/master/m5/task5.3/root_log_in_sleep.jpg)

------------
## Part 2
