print "+++++++++++++++++++++++\nSAN FRANCISCO ADVENTURE\n+++++++++++++++++++++++"

""" User starts out on a Friday evening after work.
Prompt user to make a decision, go home or grab some dinner. Use foursquare api to list popular places in the SOMA area.

"""
import FoursquareAPI
# def pause():
# print ('Press enter to continue')
# # 	input()
def intro():
	print "The clock finally strikes 5p and you bolt out the front door of your office in SOMA.\nYay! Thank God it's Friday night and you just got paid!"
	print "Now what? Do you want to 'go home' or grab a bite to 'eat'?"
	first_decision=str(raw_input("Type 'go home' or 'eat'"))
	#for eat decision, use foursquare api for trending places in SOMA
	if first_decision=="go home":
		print "Wow! What a boring way to start the weekend. You go home and fall asleep while watching Netflix. Your SF adventure is over."
	elif first_decision=="eat":
		print "Good choice! Your stomach just growled. Let's find some good places to eat in SOMA!"
		outToeat()
	else:
		print "|", first_decision, "| wasn't a choice. Have you started drinking already? Let's try this again."
		intro()

def headhome():
	print "You're over everything and just want to binge watch LOST on Netflix.\nYou head home and stay in for the weekend."
	
def outToeat():
	FoursquareAPI.getvenues()
	food_choice=str(raw_input("What place around here looks good to you?"))
	print "Oh nice choice!", food_choice, "has really good food."
	print "You walk over to",food_choice, "\nWhen you open the door you see a familiar face standing in line, it's your best friend!"
	print "Unfortunately, you see another familiar face and the two of you make eye contact..."
	print "It's your ex, sitting alone at a table. Your ex looks like they're on the struggle bus.\nIs...is that a single tear you see on their face?!"
	print "Oh boy, what do you do now? Do you go say hi to your ex and see what's going on?\nOr pretend like you don't recognize them and go talk to your best friend?"
	exOrbff()

def exOrbff():
	friendorfoe=str(raw_input("Type 'ex' or 'bff'"))
	if friendorfoe=="ex":
		print "You sigh because you have been spotted. Reluctantly, you walk over to your ex."
		print "'Hey-oooh!' you say to your ex, 'How's it going?'"
		print "'I could be better,' your ex replies, 'Would you like to sit down?'"
		print "A bead of sweat runs down your face. It's taking every ounce of restraint you have to not go running through the door like the Kool-Aid man." 
		print "Enter '1' if you're way too nice of a person and decide to sit down."
		print "Enter '2' if you would rather go talk to your best friend."
		sitorgo=str(raw_input("Choose '1' or '2'"))
		if sitorgo=="1":
			print "You pull out a chair and take a seat."
			ex()
		elif sitorgo=="2":
			print "'No thanks. I'm meeting a friend here. I just wanted to say hi,' you say. You then walk away because you are a sane person."
			bff()	
		else:
			print "Really? |", sitorgo, "| That's what you're going with? Oh I see, you're a rebel. You didn't want to choose '1' or '2'. Have fun getting stuck in an infinite loop until you choose!"
			exOrbff()
	elif friendorfoe=="bff":
		print "You walk over to your best friend."	
		bff()
	else:
		print "|", friendorfoe, "| You don't want to talk to either of them, huh? Let's go back to the start so you can reevaluate your life choices."	
		intro()
def ex():
	print "As soon as your ex opens their mouth you think to yourself..."
	print "'Self? Would I rather spend my Friday listening to my ex complain or go hang out with my bff? What am I doing?"
	print "You apologize to your ex and say 'I'm so sorry, I just realized I have ummm...things to do. Good luck with your situation. Bye!'"
	print "Phew! Let's blame that temporary lack in judgement on hunger.\n You walk over to your bff like you should have done in the first place."
	bff()

def bff():	
	print "You grab some food and eat dinner with your friend. Your BFF 'knows a guy' at one of the venues in the area and suggests you go to a concert." 
	print "You kind of feel like taking it easy and hanging out in Golden Gate Park."
	print "Go to the park or head to a concert?"
	parkorconcert=str(raw_input("Type 'park' or 'concert'"))
	if parkorconcert=="park":
		print "You pull out your sweet new iPhone 5 and request an Uber ride. Ain't nobody got time for MUNI."
		park()
	elif parkorconcert=="concert":
		print "Your friend has connections at multiple places."
		concert()
	else:
		print "|", parkorconcert, "| doesn't seem to be an option. You must be tired. Go home!"
		headhome()

def concert():
	print "Which venue do you prefer to go to?"
	FoursquareAPI.independent()
	FoursquareAPI.foxtheater()
	FoursquareAPI.gamh()
	venuechoice=str(raw_input("Type choice here"))
	if venuechoice=="Fox Theater":
		print "You and your friend hop on the BART to head over to Oakland."
		fox()
	elif venuechoice=="The Independent":	
		print "You and your friend hop into an Uber and head to The Independent."
		theindy()
	elif venuechoice=="Great American Music Hall":
		print "You and your friend hop into an Uber and head to Great American Music Hall."	
		greatamerican()
	else:
		print "|", venuechoice, "| doesn't seem to be an option. Let's try this again."	
		concert()

def park():	
	print "You and your friend hop into an Uber to head to Golden Gate Park."
	print "Your Uber driver is kind of eccentric and insists on serenading you guys with 'Hey There Delilah'"
	print "Hate is a strong word, but you really,really,really don't like the Plain White Tees."
	print "You are so traumatized by the experience that you decide you've had enough adventure for one day."
	headhome()

def fox():
	print "Wow! You picked a great night to head to The Fox because your favorite band is playing!"
	print "You're friend has connections so you guys are able to get backstage."
	print "You're ecstatic because everything worked out so well!\nYou feel sorry for the 'you' that exists in alternate dimensions and made other choices."
	print "You have a feeling that going to Great American Hall would have been disastrous."

def theindy():
	print "Oh no! The Independent is closed for the night."
	print "Kanye West rented out the whole venue so he could work on his new stand up comedy act, 'Kiddin' With Kanye'"
	print "You can hear some of his jokes from outside, they're terrible."	
	print "If you hurry, you guys might be able to make it to another venue on time! There's barely any traffic because half the city is at Burning Man."
	concert()

def greatamerican():
	print "Well this is...unfortunate. Smashmouth is headlining GAMH tonight."	
	print "You think to yourself, maybe I can make the best of a less than desirable situation. I can still have fun!"
	print "YOU'RE" 
	print "WRONG" 
	print "The lead singer, who closely resembles Guy Fieri, goes on another one of his tirades and storms off the stage."
	print "The rest of the band members continue to play 'All Star' for an hour, while you slowly go insane."
	headhome()

intro()