### mininet custom topology

-  create a custom topology and run it within the 'mn'
-  create a custom topology in a python script and run without the 'mn'
  

<pre>
mininet@10-0-2-15:~/mininet/custom$<b>pwd</b>
/home/mininet/mininet/custom
mininet@10-0-2-15:~/mininet/custom$<b>more README</b>

This directory shuld hod configuration files for custom mininets.

See custom_example.py , which loads the default minimal topology. THe advantage of defining a mininet in a separate file is that you then use the --custom option in mn to run the CLI or specific test with it.

To start up a mininet with the provided custom topology, do: <b> sudo mn --custom custom_example.py  --topo mytopo</b>
mininet@10-0-2-15:~/mininet/custom$
</pre>


<pre>
mininet@10-0-2-15:~/mininet/custom$<b>ls</b>
mesh.py   meshy.py~  README  topo-2sw-2host.py
mininet@10-0-2-15:~/mininet/custom$
</pre>
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/image/VirtualBox_Mini_27_03_2016_22_14_51.PNG)

as an example we will create a topology in mininet with a python file that is already in the custom with file
for example we <b>topo-2sw-2host.py</b>
<pre>
mininet@10-0-2-15:~/mininet/custom$<b>sudo mn --custom topo-2sw-2host.py --topo my topo --controller=remote,ip=10.0.2.15</b>
</pre>

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/VirtualBox_Mini_27_03_2016_22_14_51x.PNG)

then conduct experiments like this
<pre>
mininet><b>dump</b>
</pre>

then ...

<pre>
mininet><b>net</b>
</pre>

then

<pre>
mininet><b>pingall</b>
</pre>
then
<pre>
mininet><b>exit</b>
</pre>

then to clean topology type the following command

mininet@10-0-2-15:~/mininet/custom$<b>sudo mn -c</b>
