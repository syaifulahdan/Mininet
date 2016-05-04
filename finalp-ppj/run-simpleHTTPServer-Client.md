#####Run a simple web server and client 

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-05%2002:39:15.png)

1. Xterm client 1
<pre>
mininet> h1 xterm
</pre>

<pre>
root@bertopeng17-thinkPad-T520:/home/bertopeng17/mininet/examples#<b>python -m SimpleHTTPServer 80</b>
Serving HTTP on 0.0.0.0 port 80 . . .
10.0.0.20 - - [04/May/2016 01:25:30] “GET /HTTP/1.1”200 -
</pre>
![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-05%2002:39:29.png)

2. Xterm client 2
<pre>
mininet> h2 xterm
</pre>
<pre>
root@bertopeng17-thinkPad-T520:/home/bertopeng17/mininet/examples#<b>curl 10.0.0.10</b>
</pre>

![alt tag](https://github.com/syaifulahdan/mininet/blob/master/finalp-ppj/image/Screenshot%20from%202016-05-05%2002:39:44.png)
