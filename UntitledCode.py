#uhm I have no name for this lol :'D'

#PROLOGUE #1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("You are running, faster and faster through the desert, sweat trickling down your face.\n")
print("You finally reach the city. Or at least, what they call a city. It's not REALLY a city.\n")
print("The buildings are small and made of stone.")
print("You run through the small crowd of people infront of your destination.")
print("None of them were going inside.\n")
print("You knock on the... well, it's not really a door, is it?\n")
print("It's more of a big, metal gate, seperating you from the inside of the palace.")
print("")
print("")

#PROLOGUE #2 & PLAYER NAME
print("You knock twice. Nothing happens. You knock again. ... Silence.\n")
print("You raise your hand to knock again, when the door suddenly starts")
print("to shake, the floor rumbling slightly.\n")
print("The door opened vertically, revealing a long hallway.")
print("You walk in, still huffing and puffing from the run.\n\nYou made it.\n")
print("You finally made it! As you go down the hallway you see a large")
print("room, filled with people.")
print("\nYou approach them and say hello to the nearest one.\n")
print("They say hello back to you and ask you 'what's your name?\n\n ..... \n")
print("Now that I think of it, we never went over your name. \nWell? What is it?\n")
player_name = input("What is your name?\n")

#ICE COFFEE
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("So, your name is " + player_name + ", huh? Nice name. Now, let's go back on topic, shall we?")
print("")
print("The person tells you their name, Kokoba, but you can tell you're going to forget their name.")
print("You say your goodbyes, and leave the conversation.")
print("You walk around, looking for a spot to sit down and enjoy what you came for- a nice cup of ice coffee.")
print("You monster.")
print("You went ALL the way to the city JUST FOR A CUP OF COFFEE???")
print("Oh. My. God.")
print("\n")

#ICE COFFEE 2
print("You enjoyed the ice coffee (like the monster you are) and went back outside to look for something else to do.")

print("\n\nYou have two options to choose from: Going (s)hopping for something quick to eat or going to a (r)estaurant.")
shopping_or_restaurant = input("Which will you choose?\n")

#FIRST DECISION OF PLAYER

while (shopping_or_restaurant.lower() != "s") and (shopping_or_restaurant.lower() != "r"):
  shopping_or_restaurant = input("Invalid input.\nPlease choose either (S)hopping or (r)estaurant.\nWhich will you choose?\n")

if shopping_or_restaurant.lower() == "s":
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("So, you're going shopping, then. Good choice. Not that it matters anyways.")
  print("You only brought\nwith you a $20 bill.")
  print("You buy yourself a salad for $5 and a can of Pepsi (I'm not sponsored) for $3.")
  print("Sweet, you get to save $12. Not that anyone cares.")
  print("You check out your food and sit down on a bench nearby.")
  print("'Why does everything have to be built out of stone here??' you ask yourself.\n")
elif shopping_or_restaurant.lower() == "r":
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nSo, you decided to go to a restaurant instead of buying something from the local supermarket.\nThat's fine with me I guess. You reach down into your pocket and feel what money you brought with you. Huh, just $20 then. The only thing you can afford around here is a burger from Wackdonalds, or as the locals call it 'Wakkas'. You pay for your burger ($8) and sit down on a\nbench to enjoy your meal.\n")
#END OF DECISION

#ITS A BIRD! IT'S A PLANE! NO, DUMBASS IT'S A SPACESHIP.
print("As you are sitting down and enjoying your meal, something shiny catches your eye. At first, you cover your eyes from the reflection of the sun, wondering to yourself 'IN THE NAME OF- what the hell could that be?? A water bottle? No, that's not very sun-reflectivey. Maybe a phone? NO! Why would someone throw a phone? Hmm, maybe I should just TRY to have a look...'. So that's what you did.\n")

print("As you look up, you see... nothing. You don't see anything. Well, except the sky, and a\ncouple clouds. Nothing else. You hear a loud noise near you, like a rocket landing after a\nlong trip to- back on topic. As you try to search for the 'rocket', sand starts flying everywhere, some getting onto your face and into your eyes. You manage to get all the sand out (somehow) and continue looking for the source of all this destruction. As you look around, more sand gets into your eye. Again, you manage to get all of it out of your eyes, but as you were doing so, the shiny thing caught your eye again.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("'Woah', you think as you look at the shiny thing. It wasn't a waterbottle or a phone or a rocket. At least, not a rocket you would normally find. It was long and horizontal, had engines at the back which would propell it to its destination, a cockpit at the front- ok, it's basically a fancy rocketship that's horizontal. Also-\n\nPEW PEW PEW *reload* PEW PEW PEW PEW PEW *reload again*\n'WOAH!' you scream, as you duck behind the stone bench, hoping not to get shot at. Seems they noticed you, as people with guns came out from the bottom of the ship. Oh, did I mention the ship is NOT on the ground entirely, but has enough space between it and the ground? No? Deal with it.\n\nYou take a quick peek at what's going on on the other side of the bench. It seem that the people are approaching you!\n")

#PLAYER CAN DIE HERE. Ending 1 Is Available. 
#FINAL PART OF PROLOGUE.
ending1_or_continue = input("What will you do? Will you (r)un or (f)ight?\n")

while (ending1_or_continue.lower() != "r") and (ending1_or_continue.lower() != "f"):
  ending1_or_continue = input("Invalid input.\nPlease choose either (R)un or (F)ight estaurant.\nWhich will you choose?\n")

if ending1_or_continue.lower() == "r":
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nRun. So, you chose to run. Whelp, I don't write the endings. You think to yourself'I'm gonna make a run for it. If I make it out, I'll get as far away from here as possible.'. That's your only plan. You quietly do a countdown to run. Even if you shouted, it wouldn't matter. No one would be able to hear your. Even if they did, they wouldn't care. One. Two. THREE! You make a run for it. The people notice you trying to run away from them. They shoot at you, shots going everywhere. One hits you in the shoulder. 'Doesn't hurt that much. I'll get over it... probably.'. You wouldn't. More shots are sent flying your way. Another hits you in the leg. You can't run anymore. Fighting back tears, you try to limp your way to the only safe spot- the same place you got your coffee. However, just as you were going to enter through the metal door, another shot found their mark - on your...\n\nHead.\nIt hit you on your head, from behind. The bullet goes through your entire head, through the brain, out the nose, all in a split second.\n\nYou... died.\n\n...\n\nThe end? No. There MUST be a different ending to this.\nAnd there is. There is an ending where, at least at this part, you survive.")
  quit()
elif ending1_or_continue.lower() == "f":
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nFight. So, out of running away, you choose to fight. Whelp, I don't write the endings. You make a fist and wait for the person to check if you're there. 'Oh, god, please work.' you mumble to yourself. They check if you're there. Then they realised something was on their face. IT WAS PAIIIIIIINNNNNNNNNN!\n\nYou managed to knock the guy out! Good job. You also managed to get attention of almost the whole, well, gang? Group? What can you call them? Ah, I know, invaders.\n\nAll the invaders approach you, but they had but their guns down. What? Oh, but they all had something in their hands. Police handcuffs? WAIT YOU AREN'T A CRIMINAL, ARE YOU? Oh, wait, you aren't. Wrong story.\n\nYou manage to knock two of them out, but eventually they overpowered you, throwing you onto the floor. Two of them grab one of your arms, another three handling your legs. You are powerless. Then, what looks like the leader approached you.\nHe wore a mask, like the rest of them, but it was black. The others had red masks, you realise. How had you not noticed this earlier? I mean, you were fighting for your useless life, but you could have at least have been observant. The leader knocked you out, then put on the handcuffs.")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("Is this the end?")
  print("They have you now, and since you're useless, what good are you to them?")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("It wasn't the end.")
  print("In fact, it was just...")
  print("")
  print("The beginning.")

#The Beginning
print("You wake up. ")
print("...")
print("Where are you?\nWhereever you are, you don't know.\nhonestly, it doesn't matter as you only have one thing on your mind - 'how do I get out of here?'.")
print("You open your eyes to see a bright light shining directly into your eyes. You blink thrice and look in a different direction. \nThe room looks pretty nifty overall, especially for a rocket. ")
