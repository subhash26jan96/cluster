#!/usr/bin/python2


print "content-type:text/html"
 
print ""

import  time,os,sys,commands,re,cgi,cgitb
cgitb.enable()


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

print """

				
			 <div id="bodydiv">

			 <img class="imagehead" src="http://192.168.0.1/photoshop-spotlight-background-free-psd-1.jpg">			 
			 <img class="forebodyimg" src="http://192.168.0.1/ele1.png" />
			
			 
			 </div>
			  <div id="footerdiv">
			   <img id="footerimg" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
		</div>

			
	"""
print """


	<head>

	<script>


    	var auto = prompt("Maximum No. Of Available Data Nodes: 2");
	if (auto!="")	
		{
		document.location="http://192.168.0.1/cgi-bin/automate.py?auto=" + auto;					 
		
				
		}

	</script>
	</head>
      
       	

  </body>
</html>
"""

