#!/usr/bin/python2


print "content-type:text/html"
 
print "" 

import  time,os,sys,commands,re,cgi,cgitb
cgitb.enable()

x=cgi.FieldStorage()
job=x.getvalue('jobtracker')


name=x.getvalue('y')
	


os.system("nmap -n -sn 192.168.0.0/24 --exclude 192.168.0.20 -oG- |awk '/Up$/{print $2}'")
fh = open('G-','r')				#namp result file
lines = fh.readlines()
count=0
flag=1
index=[]
ipmap={}
ip=[]
h=[]
for line in lines:      			#read the file line by line
	s= line
	if s.startswith('Nmap'):		#filter out lines with ip
		 count=count+1
		 w=[count]
		 #sys.stdout.write(str(count)+'\t')
		 index= index +w
		 t=s.split()			#forms a list 't'
                 #sys.stdout.write (t[4]+'\t ')
		 a=[t[4]]
		 ip=ip+a  
fh.close()
ipmap=dict(zip(index,ip))


i = int(name)
commands.getstatusoutput("sudo sshpass -p redhat ssh " + ipmap[i] + " 'hostnamectl set-hostname master.localdomain'")
master=ipmap[i]

os.system("sudo touch /hosts")
os.system("sudo chmod 777 /hosts")






fh=open('/hosts','w')
fh.write(ipmap[i]+"\tmaster.localdomain\n")
fh.close()


del ipmap[i]

i = int(job)
commands.getstatusoutput("sudo sshpass -p redhat ssh "+ipmap[i]+" 'hostnamectl set-hostname jobtracker.localdomain'")
jobtracker=ipmap[i]
fh=open('/hosts','a')
fh.write(ipmap[i]+"\tjobtracker.localdomain\n")
fh.close()

del ipmap[i]



j= 2
fh=open('/hosts','a')

if j<5: 
	for k in ipmap.keys():
                s=str(k)


		if flag<(j+1):
			fh=open('/hosts','a')
			fh.write(ipmap[k]+"\tnode"+s+".localdomain\n")
			fh.close()
			flag+=1
			
else:
	print 'Not Happening '

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
xox=commands.getstatusoutput(" sudo sshpass -p redhat scp /hosts  "+master+"':/etc'")
to=commands.getstatusoutput(" sudo sshpass -p redhat ssh "+master+" 'hadoop-daemon.sh start namenode'")
if to[0]==0:
	print """
		<head>
 	        <script>
		alert("NameNode has been initiated ;)");
		</script>
		</head>
	      """
print """
  <body>
  		<div class="container">
			 <div id="headerdiv">
			 <img class="imagehead" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
			<div id="valuep">
      """



print """

			</div>	
			 <div id="bodydiv">

			 <img class="imagehead" src="http://192.168.0.1/photoshop-spotlight-background-free-psd-1.jpg">			 
			 <img class="forebodyimg" src="http://192.168.0.1/ele1.png" />
			
			 
			 </div>
			  <div id="footerdiv">
			   <img id="footerimg" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
		</div>

			
	"""



commands.getstatusoutput("  sudo sshpass -p redhat scp /hosts  "+jobtracker+"':/etc'")
t=commands.getstatusoutput(" sudo sshpass -p redhat ssh "+jobtracker+" 'hadoop-daemon.sh start jobtracker'")


if t[0]==0:
	print """
		<head>
 	        <script>
		alert("Job Tracker has been initiated ;)");
		</script>
		</head>
	      """		
for k in ipmap.keys():
        s=str(k)
        t=commands.getstatusoutput(" sudo sshpass -p redhat scp /hosts  "+ipmap[k]+"':/etc'")
        if t[0]==0:
               commands.getstatusoutput(" sudo sshpass -p redhat ssh "+ipmap[k]+" 'hostnamectl set-hostname node'"+s+"'.localdomain ; exec bash'")
	       commands.getstatusoutput(" sudo sshpass -p redhat ssh "+ipmap[k]+" 'hadoop-daemon.sh start datanode'")
               commands.getstatusoutput(" sudo sshpass -p redhat ssh "+ipmap[k]+" 'hadoop-daemon.sh start tasktracker'") 
	       print """
		<head>
 	        <script>
		alert("Your Cluster is ready :D ");
		</script>
		</head>
	      """     	 	








