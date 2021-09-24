	1) Install python
		a. Add to env variables
	2) Install PyCharm community edition
	3) Install flask
  4) Design your website
		a. Change content in the website
		b. app.py -> function
		deflocate(request):
		resp=urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
		obj=json.loads(resp.read())
		lat=obj['iss_position']['latitude']
		long=obj['iss_position']['longitude']
		current_position_url='https://www.openstreetmap.org/?mlat='+str(lat)+'&mlon='+str(long)+'#map=3/'+str(
		lat)+'/'+str(long)
		webbrowser.open_new(current_position_url)
		returnrender(request,'iss_app/home.html')
		c. Html- form action
		<formaction="/locate">
		<br><buttonid="sub"type="submit">Locatenow</button>
		</form><br>
		
		e. Beautify with CSS:
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
			
		
