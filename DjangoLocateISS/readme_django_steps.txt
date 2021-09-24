	1) Install python
		a. Add to env variables
	2) Install PyCharm community edition
	3) Install Django
		a. Inside the terminal of PyCharm, Install pip install Django
			i. SQL Parse DB - Nonvalidating SQL parser for python. It provides support for parsing, splitting and formatting SQL statements. It is compatible from py 2.7 or higher. 
			ii. PYTZ - TZ stands for time. It’s A Third-party module that brings Olson TZ database into Python. This library allows accurate and cross platform time zone calculations using Python 2.4 or higher.
		b. Check for installation & Cross check
			i. Go to cmd
			ii. Type Python -m django --version 
	4) Create a directory inside our project
		a. Go to terminal and Cd to our project -- locateISS
		b. Type django-admin startproject locateiss
		c. Now the dir is created inside our mainproject LocatingInternationalSpaceStation with the same name as project
			i. Files created by Django
				1) Mange.py - cmd line utility to interact with Django project
				2) In terminal - type: python manage.py runserver
				3) Returns IP address
				4) Press ctrl+c in terminal to stop
			ii. Same dir as project name:
				1) init.py- empty dir package used as initialization file
				2) settings.py- settings necessary for current  project
				3) urls.py- All URL declarations for this project
				4) WSGI.py web server gateway interface - calling convention for webservers to forward request to wen app or other servers
	5) Create an APP within my project
		a. Go to terminal and Type python manage.py startserver iss_app
			i. It creates similar files and now you can modify the files based on your content
			ii. Choose views.py
				1) It automatically installed render library
				2) Type  from django.http import HttpResponse
				3) Define a function
				defhome(request):
				returnHttpResponse('<h1>Home</h1>')
				4) Connect Views & URL:
					a) In the iss_app, create a .py file same as urls.py
					b) Go to the project's urls.py copy last lines, including the pattern
					c) Paste the content in the urls.py and import views function inside urls.py and in name you can give any name. from . Means current dir
					
						fromdjango.urlsimportpath
						from.importviews
						urlpatterns=[
						path('',views.home,name='home-page'),
						]
				5) Check Home: in terminal - type: python manage.py runserver
	6) Create Website using HTML
		a. Go to the app dir
		b. Create a dir called templated (Django looks for templates here)
		c. Again inside templated dir, create an dir same as your app name "iss_app"
		d. Now create a HTML file name it home.html
		e. Edit HTML & Save
	7) Configure this to Django
		a. Go to app.py and copy the default function name
		b. Go to settings.py and scroll to installed apps
			i. Now type 'iss_app.apps.IssAppConfig' , 
			ii. Go to views.py
				1) Instead of http response - Use render
				2) Return render(request, 'iss_app/home.html')
			iii. Run in terminal server & check
			
	8) Design your website
		a. Change content in the website
		b. Views.py
		deflocate(request):
		resp=urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
		obj=json.loads(resp.read())
		lat=obj['iss_position']['latitude']
		long=obj['iss_position']['longitude']
		current_position_url='https://www.openstreetmap.org/?mlat='+str(lat)+'&mlon='+str(long)+'#map=3/'+str(
		lat)+'/'+str(long)
		webbrowser.open_new(current_position_url)
		returnrender(request,'iss_app/home.html')
		c. Urls.py in app
		path("locate",views.locate)
		d. Html- form action
		<formaction="/locate">
		<br><buttonid="sub"type="submit">Locatenow</button>
		</form><br>
		
		e. Beautify:
			i. After form:
			<divclass="bg"></div>
			ii. CSS:
			iii. <head><metaname="viewport"content="width=device-width,initial-scale=1"></head>
			<style>
			h1{text-align:center;}
			p{text-align:center;}
			div{text-align:center;}
			button{text-align:center;}
			#sub{
			width:fit-content;
			height:43px;
			border-radius:14px;
			font-size:20px;
			}
			#sub:hover{
			background-color:darkcyan;
			}
			body,html{
			height:100%;
			margin:0;
			}
			.bg{
			/*Theimageused*/
			background-image:url("https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/images/557331main_iss027e036710_full.jpg");
			
			/*Fullheight*/
			height:100%;
			
			/*Centerandscaletheimagenicely*/
			background-position:center;
			background-repeat:no-repeat;
			background-size:cover;
			}
			</style>
			
		
