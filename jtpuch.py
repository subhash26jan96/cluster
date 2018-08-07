#!/usr/bin/python2


print "content-type:text/html"
 
print "" 

import  time,os,sys,commands,re,cgi,cgitb,sys
cgitb.enable()

x=cgi.FieldStorage()
y=x.getvalue('namenode')




commands.getstatusoutput("nmap -n -sn 192.168.0.0/24 --exclude 192.168.0.20 -oG- |awk '/Up$/{print $2}'")
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
		
		 e=commands.getstatusoutput('ssh '+t[4]+' lscpu|grep name ')      		
	         l=list(e)                      #cast tuple to list
        	 s=l[1]				#assaign 2nd list value to str	
        	 d=s.split(':')			#the out into list
		 f=d[0]				#list to str
		 q=f.strip()			#remove whitespace
        	 #sys.stdout.write( q)	
		 z=commands.getstatusoutput('ssh '+t[4]+' free -m | grep Mem ')
		 x=list(z)			
		 s=z[1]					
		 o=s.split()
		 #sys.stdout.write(" \t       "+o[3]+"\t \t ")
		 e=commands.getstatusoutput('ssh '+t[4]+'  df -h |grep /dev/map')
		 l=list(e)
		 s=l[1]
		 d=s.split()
		 #print '\t\t'+d[3]
	        
	fh.close()


ipmap=dict(zip(index,ip))

os.system("sudo touch iplist.txt")
os.system("sudo chmod 777 iplist.txt")	
os.system("sudo echo {} > iplist.txt".format(ip))
fop=open("iplist.txt","r")
fopr=fop.read()
gopr=fopr.split("\n")[0]
h=gopr[1:-1].split(",")



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
	body
	{
	margin:0;
	padding:0;
	 }
        .container{
            height: 100%;
            width: 100%;
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

print """
  <body>
  		<div class="container">
			 <div id="headerdiv">
			 <img class="imagehead" src="http://192.168.0.1/darkBlue.jpg">
			 </div>


<div id="valuep" >        """

kount=0
for i in h:
        
        
	sys.stdout.write( str(kount+1)+"=>"+str(h[kount]))
	print "<br />"	
	print "<br />"
	print "<br />"
		
	kount+=1

print """ </div>
			 <div id="bodydiv">
  

			 <img class="imagehead" src="http://192.168.0.1/photoshop-spotlight-background-free-psd-1.jpg">			 
			 <img class="forebodyimg" src="http://192.168.0.1/ele1.png" />
			
			 
			 </div>
			  <div id="footerdiv">
			   <img id="footerimg" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
		</div>
  </body>
</html>
			
	"""

print """
	<head>
	<script>

    	var jobtracker = prompt("Please enter serial no of JT");

	if (jobtracker!="")	
		{"""
print "document.location='http://192.168.0.1/cgi-bin/mainback.py?jobtracker=' + jobtracker + '&y="+y+ "';"	

print """		
				
		}	

	</script>
	</head>
      
       """





