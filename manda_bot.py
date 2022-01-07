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
\033[1;96m
███████╗██╗░░░░░░██████╗░░█████╗░██████╗░░█████╗░████████╗
██╔════╝██║░░░░░██╔════╝░██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
█████╗░░██║░░░░░██║░░██╗░███████║██████╦╝██║░░██║░░░██║░░░
\033[1;97m██╔══╝░░██║░░░░░██║░░╚██╗██╔══██║██╔══██╗██║░░██║░░░██║░░░
███████╗███████╗╚██████╔╝██║░░██║██████╦╝╚█████╔╝░░░██║░░░
╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░\n\n\033[1;96mCreated By \033[1;92mRaka Andrian Tara Instagram \033[1;92mraka_andrian27 
\033[1;96mCuma Work Di \033[1;92mPost Publik\033[1;96m
Tidak Berjalan Di \033[1;92mPost Photo Profil dan Sampul !!!
\033[1;96mLimit Minimal \033[1;92m50 \033[1;96mComment ...""")

# LOGIN

def log():
	clear()
	banner()
	os.system("rm -rf bokep.json")
	print("\n______________________________________________________\n")
	bos = input("╠══◍➤®[•] Token : \033[1;92m")
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
		print("╚══◍➤®[•] Login Succes")
		menu()
	except KeyError:
		print("╚══◍➤®[•] Token Invalid")
		log()

# MENU

def menu():
	clear()
	banner()
	print("\n______________________________________________________\n")
	print("╔══◍➤®[1] Auto Comment")
	print("╠══◍➤®[2] Auto Followers")
	print("╠══◍➤®[0] Log Out")
	pilih()

# PILIH MENU

def pilih():
	sc = input("\n╠══◍➤®[•] Choose : \033[1;92m")
	if sc=="":
		pilih()
	elif sc=="1":
		komen()
	elif sc=="2":
		tok = input("\033[1;96m╠══◍➤®[•] Token : \033[1;92m")
		cs = open("bokep.json","a")
		cs.write(","+tok)
		cs.close()
		print("\033[1;96m╠══◍➤®[•] Token Added")
		input("╚══◍➤®[•] Back")
		menu()
	elif sc=="0":
		os.system("rm -rf tokek.json bokep.json")
		print("╚══◍➤®[•] Thank You For Using My Tool.!!!")
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
		print("╠══◍➤®[•] First Login")
		log()
	ki = input("\033[1;96m\n╠══◍➤®[•] Enter Publik Post ID : \033[1;92m")
	v = open("id.json","w")
	v.write(ki)
	v.close()
	print("\033[1;96m╠══◍➤®[•] Input Comment Text...")
	print("╠══◍➤®[•] Use a Comma(\033[1;92m,\033[1;96m)For Random Comments")
	print("╠══◍➤®[•] Example : \033[1;92mI love you,I Miss you")
	ka = input("\033[1;96m╠══◍➤®[•] Comment : \033[1;92m")
	w = open("kom.json","w")
	w.write(ka)
	w.close()
	say = open("id.json","r").read()
	soy = open("kom.json","r").read()
	soyy = soy.split(",")
	bc = open("bokep.json","r").read()
	gi = bc.split(",")
	bb = int(input("\033[1;96m╠══◍➤®[•] Enter The Number of Comments : \033[1;92m"))
	print("\033[1;96m\n╚══◍➤®[•] Starting...\n")
	for k in range(bb):
		k +=1
		bo = random.choice(gi)
		id = say
		ko = random.choice(soyy)
		yt = requests.post("https://graph.facebook.com/"+id+"/comments/?message="+ko+"&access_token="+bo)
		bh = json.loads(yt.text)
		if "id" in bh:
			print("\033[1;92m[✔] Comment To %s Success To Send" %(k))
		if "error" in bh:
			print("\033[1;91m[✖] Comment To %s Failed To Send" %(k))
	print("╠══◍➤®[•] Finished")
	input("╚══◍➤®[•] Back")
	menu()
menu()
