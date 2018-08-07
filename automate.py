#!/usr/bin/python2

print "content-type:text/html"
 
print "" 

import os,commands
import sys,operator
import cgitb
import cgi
cgitb.enable()




x=cgi.FieldStorage()
aut=x.getvalue('auto')



i=int(aut)
os.system("nmap -n -sn 192.168.0.0/24 --exclude 192.168.0.20 192.168.0.2 192.168.0.3 -oG- |awk '/Up$/{print $2}'")
fh = open('G-','r')                             #namp result file
lines = fh.readlines()
count =1
ip=[]
sto=[]
sr=[]
ipbook={}
ipav={}
if (i<3):
	for line in lines:
        	s= line
		if s.startswith('Nmap'): 
        		if count<=i: 
				 z=[count]
				 sr=sr+z              #filter out lines with ip
                		 t=s.split()                    #forms a list 't'
			         a=[t[4]]
                 	 	 ip=ip+a
                          	 e=commands.getstatusoutput(' sudo ssh '+t[4]+'  df -h |grep /dev/map')
                	  	 a=list(e)
                	 	 s=a[1]
                	 	 d=s.split()
				 u=[d[3]]
                	 	 sto= sto+u
		                 count=count+1
        	 
else:
	print'cant accomaodate request at the moment'

ipbook=dict(zip(sto,ip))
ipav=dict(zip(sr,sto))

sorted_help=sorted(ipav.items(),key=operator.itemgetter(1))

print """



    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="generator" content="CoffeeCup HTML Editor (www.coffeecup.com)">
    <meta name="dcterms.created" content="Mon, 20 Jun 2016 14:55:04 GMT">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <title>CG Hadoop</title>
    <style>
	body
	{
	margin:0;
	padding:0;
	 }
        .container{
            height: 100%;
            width: 100%;
        } 

	#valuep{
     	z-index:1;
	padding:0;
	 margin:1%;
	 width:10%;
	 height:30%;
	 text-align:center;
	 
	 position:fixed;
	 left:7%;
	 bottom:40%;	
         border: 2px bold ;
          font-family:Helvetica;
          background:rgba(0,0,0,.13);
          color:#fff
         
          filter:blur(50px);




		}


	 .forebodyimg
	 {
	 padding:0;
	 margin:0;
	 width:;
	 height:50%;
	 
	 
	 position:fixed;
	 left:37%;
	 bottom:25%;
     opacity: 0.4;     
	  }
	  
	 #headerdiv
	 {position: fixed;
	 width:100%;
	 height:10%;
	 padding:0;
         z-index: 1;
	  }
	  .imagehead
	  {
	  width:100%;
	  height:100%;
      opacity: 0.8;      
	   }
	   #bodydiv
	   {position: fixed;
	   width:100%;
	   height:90%;
	   
	    }
		
      #forebodyimg
	    {
	     width:100%;	
	     height:100%;
	    }
		 
      #footerdiv
	  { border:5px green ;
              position: fixed;
              top: 90%;
	      width:100%;
	      height:15%;
             padding:0;
              z-index: 1;
	   }
		   
	#footerimg
	   {
	      width:100%;	
	      height:100%;
              opacity: 0.8;    
	  }
     </style>
    
  </head>
"""

for i in sorted_help:
	s=i
	t=commands.getstatusoutput(" sudo sshpass -p redhat ssh  "+ipbook[s[1]]+" 'hadoop-daemon.sh start datanode'")
	if t[0]==0:
		print """
		<head>
 	        <script>
		alert("Datanode has been initiated ;)");
		</script>
		</head>
	      """
	e=commands.getstatusoutput(" sudo ssh "+ipbook[s[1]]+" 'hadoop-daemon.sh start tasktracker'")
	if e[0]==0:
		print """
		<head>
 	        <script>
		alert("Task Tracker has been initiated ;)");
		</script>
		</head>
	      """

t=commands.getstatusoutput(" sudo ssh 192.168.0.2 'hadoop-daemon.sh start namenode'")
if t[0]==0:
	print """
		<head>
 	        <script>
		alert("Name Node has been initiated ;)");
		</script>
		</head>
	      """
t=commands.getstatusoutput(" sudo ssh 192.168.0.3 'hadoop-daemon.sh start tasktracker'")
if t[0]==0:
	print """
		<head>
 	        <script>
		alert("task Tracker has been initiated ;)");
		</script>
		</head>
	      """





print """
		<head>
 	        <script>
		alert("Cluster has  been automatically initiated ;)");
		</script>
		</head>
	      """
print "location:http://192.168.0.1/show.py"
