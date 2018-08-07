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



	#bu1{
    z-index: 1;
  margin: 0 auto;
  font-size: 2.0rem;
  padding: 0.75rem 2.0rem;
  display:block;
    position: fixed;
    top:25%;
    left:12%;    ;
  background-color: #022742;
  border: 1px solid transparent;
  color: #ffffff;
  font-weight: 300;
 
  border-radius: 6px;
    opacity: 0.7%;

  transition: all 0.3s ease-in-out;
}

	#bu2{
    z-index: 2;
  margin: 0 auto;
  font-size: 2.0rem;
  padding: 0.75rem 2.0rem;
  display:block;
    position: fixed;
    top:25%;
    left:72%;    ;
  background-color: #022742;
  border: 1px solid transparent;
  color: #ffffff;
  font-weight: 300;
 
  border-radius: 6px;
    opacity: 0.7%;

  transition: all 0.3s ease-in-out;
}


	#bu3{
    z-index: 2;
  margin: 0 auto;
  font-size: 2.0rem;
  padding: 0.75rem 2.0rem;
  display:block;
    position: fixed;
    top:75%;
    left:12%;    ;
  background-color: #022742;
  border: 1px solid transparent;
  color: #ffffff;
  font-weight: 300;
 
  border-radius: 6px;
    opacity: 0.7%;

  transition: all 0.3s ease-in-out;
}



	#bu4{
    z-index: 2;
  margin: 0 auto;
  font-size: 2.0rem;
  padding: 0.75rem 2.0rem;
  display:block;
    position: fixed;
    top:75%;
    left:72%;    ;
  background-color: #022742;
  border: 1px solid transparent;
  color: #ffffff;
  font-weight: 300;
 
  border-radius: 6px;
    opacity: 0.7%;

  transition: all 0.3s ease-in-out;
}





#bu1:hover {
  background-color: #ffffff;
  color: #022742;
  border-color: #022742;
    opacity:0.1%;
}


#bu2:hover {
  background-color: #ffffff;
  color: #022742;
  border-color: #022742;
    opacity:0.1%;
}


#bu3:hover {
  background-color: #ffffff;
  color: #022742;
  border-color: #022742;
    opacity:0.1%;
}


#bu4:hover {
  background-color: #ffffff;
  color: #022742;
  border-color: #022742;
    opacity:0.1%;
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
	  .head
	  {
	  width:100%;
	  height:100%;
         opacity: 0.5;      
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

		 <section>
<button  class="b2" id="bu1" type="button" onclick="location.href='http://192.168.0.2:50070'">NameNode</button>
  </section>
      

	 <section>
<button  class="b2" id="bu2" type="button"  onclick="location.href='http://192.168.0.3:50030'" >Job Tracker</button>
  </section>

	 <section>
<button  class="b2" id="bu3" type="button" onclick="location.href='http://192.168.0.2:50070/'" >File System</button>
  </section>

	 <section>
<button  class="b2" id="bu4" type="button">Exit</button>
  </section>


  		<div class="container">
			 <div id="headerdiv">
			 <img class="imagehead" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
			
     



			</div>	
			 <div id="bodydiv">

			 <img class="head" src="http://192.168.0.1/head.jpg">			 
			 <img class="forebodyimg" src="http://192.168.0.1/ele1.png" />
			
			 
			 </div>
			  <div id="footerdiv">
			   <img id="footerimg" src="http://192.168.0.1/darkBlue.jpg">
			 </div>
		</div>
	</body>
	</html>
			
	"""
