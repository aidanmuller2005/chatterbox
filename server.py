#  http://31.187.40.218/action?=create&name?=x&password?=hashy/

#  GET /asd.html HTTP/1.1
#  Host: localhost
#  Connection: keep-alive
#  Upgrade-Insecure-Requests: 1
#  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
#  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
#  Accept-Encoding: gzip, deflate, br
#  Accept-Language: en-IE,en-US;q=0.9,en;q=0.8

import socket, os, base64, datetime, time

postcounter = 0
HOST, PORT = '', 80

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((HOST, PORT))
ls.listen(1)

def openhtml(file):
	file = open(file, 'r')
	data = file.read()
	return data

cookie = ''

filez = ''

header = ''

while True:
    header = 'Content-Type: text/html'
    mainfileappend = open('www/main.html', 'a')
    mainfileread = open('www/mainz.html', 'r')
    mainfilelines = []
    for line in mainfileread:
             mainfilelines.append(line)
    mainfilewrite = open('www/main.html', 'w+')
    mainfilewrite.truncate(0)
    mainfilewrite.close()
    del mainfilelines[60]
    mainfilelines.insert(60, '')
    # print(mainfilelines)
    mainfileread.close()
    for file in os.listdir('www/posts/'):
            if file != 'template.html':
                    mainfilelines.insert(60, '<div id="mainpostbackground" onclick="window.location.href=\'http://31.187.40.218/www/posts/{}\'"><p id="mainposttitle">{}</p></div>'.format(file, file))
    for line in mainfilelines:
            mainfileappend.write(line)
    mainfileappend.close()
    mainfileappend = open('www/mainsignedout.html', 'a')
    mainfileread = open('www/mainsignedoutz.html', 'r')
    mainfilelines = []
    for line in mainfileread:
             mainfilelines.append(line)
    mainfilewrite = open('www/mainsignedout.html', 'w+')
    mainfilewrite.truncate(0)
    mainfilewrite.close()
    del mainfilelines[41]
    mainfilelines.insert(41, '')
    mainfileread.close()
    for file in os.listdir('www/posts/'):
            if file != 'template.html':
                    mainfilelines.insert(41, '<div id="mainpostbackground" onclick="window.location.href=\'http://31.187.40.218/www/posts/{}\'"><p id="mainposttitle">{}</p></div>'.format(file, file))
    for line in mainfilelines:
            mainfileappend.write(line)
    mainfileappend.close()
    cc, ca = ls.accept()
    print(ca, str(datetime.datetime.now()))
    req = cc.recv(1024)
    if 'Cookie' in req:
        cookieplace = req.index('Cookie')+15
        reqlength = len(req)
	cookie = req[cookieplace:reqlength]
	cookie = list(cookie)
	del cookie[len(cookie)-4:len(cookie)]
	cookie = ''.join(cookie)
    else:
	cookie = ''
    try:
    	site = req[5:req.index('HTTP/1.1')-1]
	if 'action' not in site:
            filer = open(site, 'r')
            if 'www/main' in site:
                if cookie:
                        data = filer.read().format(cookie, cookie)
                else:
                        filer = open('www/mainsignedout.html', 'r')
                        data = filer.read().format(cookie, cookie)
	    elif 'www/users' in site:
                data = filer.read().format(cookie, cookie)
            elif 'www/posts/' in site:
	    	data = filer.read().format(cookie, cookie)
            elif 'assets/imag' in site:
                with open(site, "rb") as imageFile:
                    data = imageFile.read()
	    else:
		data = filer.read()
	    http_response = """\
HTTP/1.1 200 OK

{}
	    """.format(data)
	else:
            action = site[8:site.index('&')]
            print(action)
            if action == 'dm':
                    site = list(site)
                    nurl = []
                    del site[0:site.index('&')+5]
                    to = ''.join(site[0:site.index('&')])
                    del site[0:site.index('&')+6]
                    msg = ''.join(site)
                    to = list(to)
                    if '=' in to:
                            del to[to.index('=')]
                    to = ''.join(to)
                    msgfile = open('messages', 'a')
                    msgfile.write('{},{},{}\n'.format(to,cookie,msg))
                    msgfile.close()
                    http_response = """\
<html>
<script>
window.location.href='http://31.187.40.218/action?=getdms&person={}/'
</script>
</html>
                    """.format(to)
            if action == 'getdms':
                    atplace = site.index('&')
                    site = list(site)
                    del site[0:site.index('&')]
                    person = ''.join(site[8:site.index('/')])
                    if '=' in person:
                        person = list(person)
                        del person[person.index('=')]
                        person = ''.join(person)
                    http_response = """\

<!DOCTYPE html>
<html>
<head>
    <title>Messages</title>
    <link rel = "icon" href ="../assets/images/chatterboxchrome.png" />
    <link rel = "stylesheet" href="../assets/css/stylesheet1.css" />
    </head>

    
<body id = 'b1'>
    
        
       
       
    
    
        <div id="maintop">
            
            
            
            
                <button id="toprightname" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/users/{}.html'">{}</button>
            
           <div id="dropdowncontent" style="visibility: hidden">
            
            <!-- Create post -->
            
            
            <button id="cpostbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:76px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/www/post.html'">Post</button>
            
            <!-- Go to messages -->
               
               <button id="messagepgbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:119.49px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=checkdm&/'">Messages</button>
               
         <!-- Sign out -->
             <button id="signoutbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:162.98px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=logout&/'">Sign out</button>
               
               
        
            </div>
            <button id="homebtn" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/main.html'">Home</button>
        
        <img src="../assets/images/chatterboxlogo.png" style="position: absolute; top:-37px; left: 3px;" />
            
            <h1 style="color: blue; font-family: sans-serif;">{}</h1>
        </div>
    
    <div style="position: absolute; top: 52%; left: 50%; width: 650px; height: 515px; box-shadow: 0 0 5px #ccc; background: #fff; border: 1px solid #ccc; border-radius: 0 0 5px 5px; transform: translate(-50%, -50%); overflow-y: scroll; overflow-x: hidden;">
                             """.format(cookie, cookie, person)
                    print('here')
                    for line in open('messages', 'r'):
                            info = line.split(',')
                            print(info)
                            if cookie == info[0] and person == info[1]:
                                    http_response = """{}<div id='otheridbackground'><p id='othernameid'>{}</p><p id='otherid'>{}</p></div><br><br><br><br>""".format(http_response, info[1], info[2].replace("%20", " ").replace("%27", "'").replace("/", ""))
                            if cookie == info[1] and person == info[0]:
                                    http_response = """{}<div id='youidbackground'><p id='younameid'>{}</p><p id='youid'>{}</p></div><br><br><br><br>""".format(http_response, info[1], info[2].replace("%20", " ").replace("%27", "'").replace("/", ""))
                    http_response = """\
{}            </div>
    <input id="messagecontent" style="position: absolute; left: 50%; text-align: center; border-radius: 4px; border: 1px solid black; bottom: 3px; transition: 0.9s; transform: translate(-50%); width: 130px; height:39px; font-size:30px; font-family: Arial" placeholder="Message" onfocus="openInput()">
        <img id="sendmsgbtn" src="../assets/images/sendmsgbtn.png" style="position: absolute; bottom: 0px; right: 41%; transition: 0.9s;" onclick="sendDM()" />
    
    <div id="sendmsgdmbox" style="background-color: white; position: absolute; border: 1px solid #ccc; box-shadow: 0 0 5px #ccc; z-index: 3; width: 650px; height: 56px; bottom: 0px; left: 50%; transform: translate(-50%); z-index: -1;">
    
    </div>
    
    
        <p id="namelink" style="visibility: hidden">{}</p>
        
    
    <script src="../assets/js/script3.js"></script>
    <script src="../assets/js/dmscript.js"></script>
    
    </body>    
</html>           """.format(http_response, person)
            if action == 'checkdm':
                    http_response = """\
<!DOCTYPE html>
<html>
<head>
    <title>Messages</title>
    <link rel = "icon" href ="../assets/images/chatterboxchrome.png" />
    <link rel = "stylesheet" href="../assets/css/stylesheet1.css" />
    </head>

    
<body id = 'b1'>
    <script src="../assets/js/script3.js">
        
    
            
            
        
        </script>
        
       
    <script src="../assets/js/messagescript.js"></script>    
    
        <div id="maintop">
            
            
            
            
                <button id="toprightname" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/users/{}.html'">{}</button>
            
           <div id="dropdowncontent" style="visibility: hidden">
            
            <!-- Create post -->
            
            
            <button id="cpostbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:76px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/www/post.html'">Post</button>
            
            <!-- Go to messages -->
               
               <button id="messagepgbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:119.49px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=checkdm&/'">Messages</button>
               
         <!-- Sign out -->
             <button id="signoutbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:162.98px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=logout&/'">Sign out</button>
               
               
        
            </div>
            <button id="homebtn" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/main.html'">Home</button>
        
        <img src="../assets/images/chatterboxlogo.png" style="position: absolute; top:-37px; left: 3px;" />
            
            <h1 style="color: blue; font-family: sans-serif; position: absolute; left: 50%; transform: translate(-50%, 0);">Messages</h1>
        </div>
    
    <div style="position: absolute; top: 56%; left: 50%; width: 550px; height: 560px; box-shadow: 0 0 5px #ccc; background: #fff; border: 1px solid #ccc; border-radius: 0 0 5px 5px; transform: translate(-50%, -50%); overflow-y: scroll; overflow-x: hidden;">

                    """.format(cookie, cookie)
                    ppllist = []
                    for line in open('messages', 'r'):
                            try:
                                    info = line.split(',')
                                    if info[0] == cookie:
                                            if info[1] in ppllist:
                                                4+4
                                            else:
                                                ppllist.append(info[1])
                                                zz = 'http://31.187.40.218/action?=getdms&person?={}/'.format(info[1])
                                                url = '<div id="contactbackground" onclick="window.location.href=\'{}\'"><p id="contacttext">{}</p></div>'.format(zz, info[1])
                                                http_response = """{}{}""".format(http_response, url)
                            except:
                                    pass
                    http_response="""\
{}          </div>
    
    <img id ="composebtn" src="../assets/images/composebtn.png" onclick="rotatebtn()">
    
    <div id="composebox" style="visibility: hidden; border: 1px solid #ccc; border-radius:0 0 5px 5px; box-shadow: 0 0 5px #ccc; background: #fff; width: 300px; height: 400px; position: absolute; bottom: 1%; right: 6%;">
    <h1 style="position: absolute; left: 50%; transform: translate(-50%); font-family: sans-serif">Compose</h1>
        <br />
        <br />
        <br />
        
        <p style="font-size: 30px; font-family: sans-serif">To</p><input id="personto" style="height: 25px; font-size: 20px; width: 250px; position: absolute; top: 87px; right: 5px;">
        
        <p style="font-size: 30px; font-family: sans-serif; position: absolute; left: 50%; transform: translate(-50%); margin-top:-20px">Message</p>
        <br/>
        <textarea id="messagecontent" style="padding-top: 0px; resize: none; margin-top: 0px; position: absolute; left: 50%; transform: translate(-50%); width: 280px; height:220px; font-size: 20px"></textarea>
        <img id="sendmsgbtn" src="../assets/images/sendmsgbtn.png" style="position: absolute; top: 3px; right: 2px;" onclick="sendMsg()" />
    </div>
    
    
    </body>    
</html>
                    """.format(http_response)
	    if action == 'post':
                if cookie == '':
                    http_response = """\
HTTP/1.1 200 OK

You are required to be logged in to post something
                    """
                else:
                    oldsite = site
                    newsite = ''
                    site = list(site)
                    del site[0:oldsite.index('&')+1]
                    newsite = ''.join(site)
                    posttitle = ''.join(site[7:newsite.index('&')])
                    newsite1 = list(newsite)
                    del newsite1[0:newsite.index('&')+1]
                    newsite1 = ''.join(newsite1)
                    content = newsite1[9:newsite1.index('/')]
                    newfile = open(os.path.join('www/posts/', '{}.html'.format(postcounter)), 'w')
                    newfile.write("""
<!DOCTYPE html>
<html>

<head>
    
    <title>{}</title>
    
    <link rel="icon" href="../../assets/images/chatterboxchrome.jpg" />
    <link rel="stylesheet" type="text/css" href="../../assets/css/stylesheet1.css" />
    
    
    
    </head>

    <body style="background: #f0f2f3; margin: 0px;">
        
        <p id="titlevar" style="visibility: hidden;">{}</p>
        <p id="creatorvar" style="visibility: hidden;">{}</p>
        <p id="creatorurl" style="visibility: hidden;">{}</p>
        
        

        <div id ="maintop">
            
             <!-- Sign out -->
<button id="toprightname" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/users/{}.html'">{}</button>
            
           <div id="dropdowncontent" style="visibility: hidden">
            
            <!-- Create post -->
            
            
            <button id="cpostbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:76px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/www/post.html'">Post</button>
            
            <!-- Sign out -->
         
             <button id="signoutbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:119.49px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=logout&/'">Sign out</button>
        
            </div>
        <!-- -->
            
            <button id="homebtn" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/main.html'">Home</button>
            
            <img src="../../assets/images/chatterboxlogo.png" style="position: absolute; top:-37px; left: 3px" />
        </div>
        
        <div style="width: 1300px; height: 530px; position: absolute; left: 50%; top: 55%; transform: translate(-50%, -50%); box-shadow: 0 0 5px #ccc; position: absolute; background: #fff; border: 1px solid #ccc; word-wrap: break-word;">
                
            <h1 id="posttitle" style="margin-top: 4px; font-size: 40px"></h1>
            
            <hr style="margin-top:-1em; padding-top: -1em; border: 1px solid black;">
            <!-- Character Limit = 1362 --> 
            <p style="font-size: 30px; margin: 0px">{}</p>
            
                
                </div>
         
        
        
        
        <script src="../../assets/js/script3.js"></script>
        <script src='../../assets/js/script4.js'></script>
        
    </body>
    
    
    
</html>
                    """.format(posttitle.replace("%20", " "), posttitle.replace("%20", " "), cookie, "http://31.187.40.218/www/users/{}.html".format(cookie), '{}', '{}', content.replace("%20", " ")))
                    newfile.close()
                    http_response = """\
HTTP/1.1 200 OK

<a href='www/posts/{}.html'>Your post?</a>
                    """.format(postcounter)
                    userpagew = open('www/users/{}.html'.format(cookie), 'a')
                    userpager = open('www/users/{}.html'.format(cookie), 'r')
                    lines = []
                    print(postcounter, posttitle)
                    for line in userpager:
                        lines.append(line)
                    lines.insert(57, '<a href="http://31.187.40.218/www/posts/{}.html">{}</a><br>'.format(postcounter, posttitle.replace("%20", " ")))
                    userpagewr = open('www/users/{}.html'.format(cookie), 'w')
                    userpagewr.write('')
                    userpagewr.close()
                    for line in lines:
                        userpagew.write(line)
                    userpagew.close()
                    userpager.close()
                    postcounter += 1
	    if action == 'logout':
                http_response = """
HTTP/1.1 200 OK
Set-Cookie: userid=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT

{}
                """.format(openhtml('www/signedout.html'))
	    if action == 'login':
                oldsite = site
                newsite = ''
                site = list(site)
                del site[0:oldsite.index('&')+1]
                newsite = ''.join(site)
		username = ''.join(site[6:newsite.index('&')])
		newsite1 = list(newsite)
		del newsite1[0:newsite.index('&')+1]
		newsite1 = ''.join(newsite1)
		password = newsite1[10:newsite1.index('/')]
		gotaccount = 0
		for line in open('accounts', 'r'):
                        data = line.split(',')
                        if username == str(data[0]):
                                passwd = list(str(data[1]))
                                del passwd[len(passwd)-1:len(passwd)]
                                passwd = ''.join(passwd)
                                print(passwd, password)
                                if password == passwd:
                                        print('got here!')
                                        gotaccount = 1
                                        http_response = """
HTTP/1.1 200 OK
Set-Cookie: userid={}; HttpOnly

<html>
<script>
window.location.href='http://31.187.40.218/www/users/{}.html'
</script>
</html>
                                        """.format(username, username)
                if gotaccount == 0:
                        http_response = """
HTTP/1.1 200 OK

{}
                        """.format(openhtml('www/loginfail.html'))
	    if action == 'create':
		oldsite = site
		newsite = ''
		site = list(site)
		del site[0:oldsite.index('&')+1]
		newsite = ''.join(site)
		username = ''.join(site[6:newsite.index('&')])
		newsite1 = list(newsite)
		del newsite1[0:newsite.index('&')+1]
		newsite1 = ''.join(newsite1)
		password = newsite1[10:newsite1.index('/')]
		accountsfile = open('accounts', 'a')
		accountsfile.write('{},{}\n'.format(username, password))
		accountsfile.close()
		http_response = """
HTTP/1.1 200 OK
Set-Cookie: userid={}; HttpOnly

{}
		""".format(username, openhtml('www/creationpage.html').format(cookie, cookie, 'www/users/{}.html'.format(username)))
		newfile = open(os.path.join('www/users/', '{}.html'.format(username)), 'w')
		newfiledata = """
<!DOCTYPE html>
<html>
<head>
    
    <title>{}'s Page</title>
    <link rel="icon" href="../../assets/images/chatterboxchrome.png" />
    <link rel ="stylesheet" type="text/css" href="../../assets/css/stylesheet1.css" />
    
    </head>
    
    <body style="margin: 0px; background-color: #f0f2f3">
        
        <script src="../../assets/js/script3.js">
        
    
            
            
        
        </script>
        
       
        
        <div id="maintop">
            
            
                <button id="toprightname" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/users/{}.html'">{}</button>
            
           <div id="dropdowncontent" style="visibility: hidden">
            
            <!-- Create post -->
            
            
            <button id="cpostbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:76px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/www/post.html'">Post</button>
            
            <!-- Go to messages -->
               
               <button id="messagepgbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:119.49px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=checkdm&/'">Messages</button>
               
         <!-- Sign out -->
             <button id="signoutbtn" style="position: absolute; height: 43.49px; z-index: 1; background: #ffffff; border: 1px solid blue; color: blue; margin-right: 0px; right: 0px; top:162.98px; width: 100px; cursor: pointer;" onclick="window.location.href='http://31.187.40.218/action?=logout&/'">Sign out</button>
               
               
        
            </div>
            <button id="homebtn" style="float: right; height: 76px; margin-top: 0px; margin-right: 0px; background: white; border: 0px solid white; color: blue;" onclick="window.location.href='http://31.187.40.218/www/main.html'">Home</button>
        
        <img src="../../assets/images/chatterboxlogo.png" style="position: absolute; top:-37px; left: 3px;" />
        </div>
    
    
    
    
        
    <div style="width: 1300px; height: 545px; box-shadow: 0 0 5px #ccc; position: absolute; background: #fff; border: 1px solid #ccc; border-radius: 0 0 5px 5px; left: 50%; transform: translate(-50%, -50%); top:354px">
        <h1 id="templateusername" style="position: absolute; left: 50%; transform: translate(-50%, -50%); color: dimgray">{}'s Page</h1>
            
        
        
            
            </div>
    
    
    
    </body>














</html>
                """.format(username, '{}', '{}', username)
		newfile.write(newfiledata)
		print(cookie, username)
		newfile.close()
    except:
		if cookie == '':
			filer = open('www/index.html', 'r').read()
		else:
			filer = open('www/main.html', 'r').read().format(cookie, cookie)
		data = str(filer)
		http_response = """\
HTTP/1.1 200 OK

{}
		""".format(data)
    cc.sendall(http_response)
    cc.close()
