
### <b>Create Topology and Slices</b>

![alt img](https://github.com/syaifulahdan/mininet/blob/master/image/Screenshot%20from%202016-04-13%2012:19:29.png)



### <b>FlowVisor</b>
-  A special OpenFlow controller that can slice the network
-  Allows multiple tenants to use the same physical network

### <b>FlowVisor Installation</b>
-  <b>Download flowvisor : git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git</b>
<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git</b>
Cloning into 'flowvisor'...
remote: Counting objects: 6356, done.
remote: Total 6356 (delta 0), reused 0 (delta 0), pack-reused 6356
Receiving objects: 100% (6356/6356), 8.67 MiB | 484.00 KiB/s, done.
Resolving deltas: 100% (3823/3823), done.
Checking connectivity... done.
bertopeng17@bertopeng17-ThinkPad-T520:~$ 
</pre>

- <b>sudo apt-get install ant default-jdk build-essential</b>
<pre>
bertopeng17@bertopeng17-ThinkPad-T520:~$ <b>sudo apt-get install ant default-jdk build-essential</b>
[sudo] password for bertopeng17: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ant is already the newest version.
ant set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-headers-3.19.0-25 linux-headers-3.19.0-25-generic
  linux-image-3.19.0-25-generic linux-image-extra-3.19.0-25-generic
Use 'apt-get autoremove' to remove them.
The following extra packages will be installed:
  default-jre default-jre-headless dpkg-dev g++ g++-4.8 libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libstdc++-4.8-dev
Suggested packages:
  debian-keyring g++-multilib g++-4.8-multilib gcc-4.8-doc libstdc++6-4.8-dbg
  libstdc++-4.8-doc
The following NEW packages will be installed:
  build-essential default-jdk default-jre default-jre-headless dpkg-dev g++
  g++-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libstdc++-4.8-dev
0 upgraded, 11 newly installed, 0 to remove and 55 not upgraded.
Need to get 19,8 MB of archives.
After this operation, 40,8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://id.archive.ubuntu.com/ubuntu/ trusty-updates/main libstdc++-4.8-dev i386 4.8.4-2ubuntu1~14.04.1 [1.058 kB]
Get:2 http://id.archive.ubuntu.com/ubuntu/ trusty-updates/main g++-4.8 i386 4.8.4-2ubuntu1~14.04.1 [18,0 MB]
Get:3 http://id.archive.ubuntu.com/ubuntu/ trusty/main g++ i386 4:4.8.2-1ubuntu6 [1.500 B]
Get:4 http://id.archive.ubuntu.com/ubuntu/ trusty-updates/main dpkg-dev all 1.17.5ubuntu5.5 [726 kB]
Get:5 http://id.archive.ubuntu.com/ubuntu/ trusty/main build-essential i386 11.6ubuntu6 [4.824 B]
Get:6 http://id.archive.ubuntu.com/ubuntu/ trusty/main default-jre-headless i386 2:1.7-51 [3.834 B]
Get:7 http://id.archive.ubuntu.com/ubuntu/ trusty/main default-jre i386 2:1.7-51 [934 B]
Get:8 http://id.archive.ubuntu.com/ubuntu/ trusty/main default-jdk i386 2:1.7-51 [932 B]
Get:9 http://id.archive.ubuntu.com/ubuntu/ trusty/main libalgorithm-diff-perl all 1.19.02-3 [50,0 kB]
Get:10 http://id.archive.ubuntu.com/ubuntu/ trusty/main libalgorithm-diff-xs-perl i386 0.04-2build4 [13,1 kB]
Get:11 http://id.archive.ubuntu.com/ubuntu/ trusty/main libalgorithm-merge-perl all 0.08-2 [12,7 kB]
Fetched 19,8 MB in 7min 24s (44,6 kB/s)                                        
Selecting previously unselected package libstdc++-4.8-dev:i386.
(Reading database ... 266076 files and directories currently installed.)
Preparing to unpack .../libstdc++-4.8-dev_4.8.4-2ubuntu1~14.04.1_i386.deb ...
Unpacking libstdc++-4.8-dev:i386 (4.8.4-2ubuntu1~14.04.1) ...
Selecting previously unselected package g++-4.8.
Preparing to unpack .../g++-4.8_4.8.4-2ubuntu1~14.04.1_i386.deb ...
Unpacking g++-4.8 (4.8.4-2ubuntu1~14.04.1) ...
Selecting previously unselected package g++.
Preparing to unpack .../g++_4%3a4.8.2-1ubuntu6_i386.deb ...
Unpacking g++ (4:4.8.2-1ubuntu6) ...
Selecting previously unselected package dpkg-dev.
Preparing to unpack .../dpkg-dev_1.17.5ubuntu5.5_all.deb ...
Unpacking dpkg-dev (1.17.5ubuntu5.5) ...
Selecting previously unselected package build-essential.
Preparing to unpack .../build-essential_11.6ubuntu6_i386.deb ...
Unpacking build-essential (11.6ubuntu6) ...
Selecting previously unselected package default-jre-headless.
Preparing to unpack .../default-jre-headless_2%3a1.7-51_i386.deb ...
Unpacking default-jre-headless (2:1.7-51) ...
Selecting previously unselected package default-jre.
Preparing to unpack .../default-jre_2%3a1.7-51_i386.deb ...
Unpacking default-jre (2:1.7-51) ...
Selecting previously unselected package default-jdk.
Preparing to unpack .../default-jdk_2%3a1.7-51_i386.deb ...
Unpacking default-jdk (2:1.7-51) ...
Selecting previously unselected package libalgorithm-diff-perl.
Preparing to unpack .../libalgorithm-diff-perl_1.19.02-3_all.deb ...
Unpacking libalgorithm-diff-perl (1.19.02-3) ...
Selecting previously unselected package libalgorithm-diff-xs-perl.
Preparing to unpack .../libalgorithm-diff-xs-perl_0.04-2build4_i386.deb ...
Unpacking libalgorithm-diff-xs-perl (0.04-2build4) ...
Selecting previously unselected package libalgorithm-merge-perl.
Preparing to unpack .../libalgorithm-merge-perl_0.08-2_all.deb ...
Unpacking libalgorithm-merge-perl (0.08-2) ...
Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
Setting up libstdc++-4.8-dev:i386 (4.8.4-2ubuntu1~14.04.1) ...
Setting up g++-4.8 (4.8.4-2ubuntu1~14.04.1) ...
Setting up g++ (4:4.8.2-1ubuntu6) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Setting up dpkg-dev (1.17.5ubuntu5.5) ...
Setting up build-essential (11.6ubuntu6) ...
Setting up default-jre-headless (2:1.7-51) ...
Setting up default-jre (2:1.7-51) ...
Setting up default-jdk (2:1.7-51) ...
Setting up libalgorithm-diff-perl (1.19.02-3) ...
Setting up libalgorithm-diff-xs-perl (0.04-2build4) ...
Setting up libalgorithm-merge-perl (0.08-2) ...
W: Duplicate sources.list entry http://dl.google.com/linux/chrome/deb/ stable/main i386 Packages (/var/lib/apt/lists/dl.google.com_linux_chrome_deb_dists_stable_main_binary-i386_Packages)
W: You may want to run apt-get update to correct these problems

</pre>

### <b>Create Mininet Topology</b>
<b>sudo mn --topo=linear,4 --arp --mac --controller=remote</b>

<pre>
mininet@CO0-19216856-101:~$ <b>sudo mn --topo=linear,4 --arp --mac --controller=remote</b>
sudo: unable to resolve host CO0-19216856-101
*** Creating network
*** Adding controller
Unable to contact the remote controller at 127.0.0.1:6633
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 s2 s3 s4 
*** Adding links:
(h1, s1) (h2, s2) (h3, s3) (h4, s4) (s2, s1) (s3, s2) (s4, s3) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 4 switches
s1 s2 s3 s4 ...
*** Starting CLI:
mininet> 

</pre>
