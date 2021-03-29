#ATTENTION!!!! this is meant to be played by itself, so make a copy and don't run it by yourself so you don't mess up the experiance of others
import os as o
o.system("clear")
import time as t
o.system("clear")
import random as r
o.system("clear")
o.system("pip install playsound")
o.system("clear")
persistant = open("persistant.txt", "r")
o.system("clear")
weapon = open("weapon.txt", "r")
o.system("clear")
with open('version.txt') as vers:
	version = vers.read()
print("WARNING!! this game is in ",version," ,so put bugs in the git ")
input("press enter to continue...")
o.system("clear")
class swamp:
 swamptf = None
 swamprnd = None
class vars:
 randnum = None
 currh = 20
 kit = 0
def swrd():
	weapon = open("weapon.txt", "w")
	weapon.write("y")
	weapon = open("weapon.txt", "r")
def swprd():
	swamp.swamprnd = r.randint(1, 5)
def hkit():
	print("You found a healthkit!")
	vars.kit = 1
	yorn = input("type y to use it and n to not use it: ")
	if yorn == "y":
		input("you have used your healthkit, you have gone to maximum health, hit enter to contiune...")
		vars.currh = 20
		vars.kit = 0
	else:
		input("you have saved your healthkit, hit enter to continue...")
def swampdef():
	randnum = r.randint(1,20)
	if randnum == 13:
		swamp.swamptf = True
		print("you have entered the swamp")
	else:
		swamp.swamptf = False
def randplay():
	vars.randnum = r.randint(1, 5)
def newplayer():
	persistant = open("persistant.txt", "w")
	persistant.write("played")
	print("you must be a new player!")
	t.sleep(2)
	print("this is my string based story game that is controlled by multiple choice questions that vary between environments")
	t.sleep(8)
	print("anyway, have fun!")
	t.sleep(3)
	o.system('clear')
	persistant = open("persistant.txt", "r")
def walk():
	input("you have walked straight because that is the only way, click enter to continue...")
def walkb():
	while True:
		rorl = input("you come at a T in the road, will you go right or left (r or l)")
		if rorl == "r":
			print("you went right")
			break
		elif rorl == "l":
			print("you went left")
			break
def walkc():
	while True:
		rorl = input("you come at a X in the road, will you go right, left, or striaght (r, l, or v)")
		if rorl == "r":
			print("you went right")
			break
		elif rorl == "l":
			print("you went left")
			break
		elif rorl == "v":
			print("you went straight")
			break
def walkd():
	while True:
		if vars.currh < 1:
			death()
			break
		rorl = input("you come up to a ravaging man, will you flee (50% success), yell (50% scare success), or attack (25% chance without a weapon, 75 with)\n")
		flag = 0
		for line in persistant:  
			pass
			if "y" in line:
				flag = 1
				break
		if flag == 0:
			if rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 3
					print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif rorl == "yell":
				chance = r.randint(1,2)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 2
					print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
			elif rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("CRITICAL HIT, YOU TAKE HIM DOWN IN ONE PUNCH, hit enter to continue...")
					break
				else:
					vars.currh -= 10
					input("He grabs your punch and throws you to the ground dealing 10 damage!","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
		else:
			if rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 3
					print("Oh No! The man runs up to you as you're vunrible and attacks you for 3 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif rorl == "yell":
				chance = r.randint(1,2)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 2
					input("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
					o.system("clear")
			elif rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1 or 2 or 3:
					input("You stab him in the heart, he bleeds out, hit enter to continue...")
					break
					o.system("clear")
				else:
					vars.currh -= 20
					print("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
					break
def walka():
	chance = r.randint(0,1)
	if chance == 0:
		swrd()
		input("YOU FOUND A SWORD!!! hit enter to continue...") 
		o.system("clear")
	else:
		input("you come at a small outpost, you sit down, hit enter to search the area...")
		hkit()
def death():
	print("you died LOL")
	playsound.playsound("dead.mp3")
	weapon = open("weapon.txt", "w")
	weapon.write("")
	weapon = open("weapon.txt", "r")
def health():
	global currh
	if currh < 20:
		currh += 1
	else:
		print("you have full health, didn't heal")
def s1():
	print("phew,")
	hkit()
def s2():
	while True:
		if vars.currh < 1:
			death()
		rorl = input("you come up to a ravaging man, will you flee (1/4 success), yell (1/8% scare success), or attack (1/5% chance without a weapon, 8/9 with)\n")
		flag = 0
		for line in persistant:  
			pass
			if "y" in line:
				flag = 1
				break
		if flag == 0:
			if rorl == "flee":
				chance = r.randint(1,4)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 15
					print("Oh No! The golem runs up to you as you're vunrible and attacks you for 15 health. Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif rorl == "yell":
				chance = r.randint(1,8)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 10
					print("it just pounces at you and takes 10 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
			elif rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("CRITICAL HIT, YOU TAKE IT DOWN IN ONE PUNCH, hit enter to continue...")
					break
				else:
					vars.currh -= 20
					input("it grabs your punch and throws you to the ground dealing 20 damage!","hit enter to continue...")
		else:
			if rorl == "flee":
				chance = r.randint(1,2)
				if chance == 1:
					input("FLEE SUCCESS! hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 15
					print("Oh No! The golem runs up to you as you're vunrible and attacks you for 15 health. Your health is now down to:",str(vars.currh))
					input("\nhit enter to continue...")
					o.system("clear")
			elif rorl == "yell":
				chance = r.randint(1,8)
				if chance == 1:
					input("HE IS TERRIFIED, HE RUNS AWAY SCREAMING LIKE A LITTLE GIRL. hit enter to continue...")
					o.system("clear")
					break
				else:
					vars.currh -= 2
					print("he just pounces at you and takes 2 points away from your health.","Your health is now down to:",str(vars.currh))
					input("hit enter to continue...")
					o.system("clear")
			elif rorl == "attack":
				chance = r.randint(1,4)
				if chance == 1:
					input("You slap and kick him, he dies, hit enter to continue...")
					break
					o.system("clear")
				else:
					vars.currh -= 20
					input("He grabs your sword and throws you to the ground and stabs you, *CRITICAL HIT* dealing 20 damage!","Your health is now down to:",str(vars.currh),"\nhit enter to continue...")
					break
def s3():
	rorl = input("you come up to an abandoned house you can either 'go in' or 'run away'\nwhat will you choose: ")
	o.system("clear")
	if rorl == "go in":
		chance = r.randint(1,4)
		spic = r.randint(1,2)
		if chance == 1:
			input("A spider jumps on you! hit enter to continue...")
			o.system("clear")
			if spic == 1:
				vars.currh -= 10
				input("OH NO! You panic and the spider bites you, you lose 10 health from the poison then leave the house, hit enter to continue...")
				o.system("clear")
			else:
				input("Phew, the spider jumps off of you and you leave the house, hit enter to continue...")
				o.system("clear")
		elif chance == 2:
			input("future interation, hit enter to continue...")
			o.system("clear")
			pass#WIP below v
			
			#WIP above ^
		elif chance == 3:
			input("future interation, hit enter to continue...")
			o.system("clear")
		else:
			input("future interation, hit enter to continue...")
			o.system("clear")
	elif rorl == "run away":
		input("you ran away and survived, hit enter to continue...")
		o.system("clear")
	else:
		input("you messed up, hit enter to continue...")
		o.system("clear")
def s4():
	input("future interaction, hit enter to continue...")
	o.system("clear")
while True:
	swampdef()
	o.system("clear")
	if vars.currh < 1:
		death()
	else:
		flag = 0
		index = 0
		for line in persistant:  
			pass
			if "played" in line:
				flag = 1
				break 
		if flag == 0: 
			newplayer() 
		else: 
			while True:
				if swamp.swamptf == False:
					health()
					randplay()
					if vars.randnum == 1:
						walk()
					elif vars.randnum == 2:
						walka()
					elif vars.randnum == 3:
						walkb()
					elif vars.randnum == 4:
						walkc()
					elif vars.randnum == 5:
						walkd()
				else:
					input("OH CRAP you're in the swamp, hit enter to continue...")
					while True:
						health()
						swprd()
						if swamp.swamprnd == 1:
							s1()
						elif swamp.swamprnd == 2:
							s2()
						elif swamp.swamprnd == 3:
							s3()
						elif swamp.swamprnd == 4:
							s4()
						elif swamp.swamprnd == 5:
							input("OMG OMG OMG, YOU MADE IT OUT! hit enter to continue..")
							break
				input("hit enter to continue")
				o.system("clear")