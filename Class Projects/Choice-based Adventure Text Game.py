#gameInnerWorkings

print("""Welcome to Dungeon Escape, a third person story of your adventure! 
Make decisions as they will ultimately decide your fate.""")

#beginning
def gameStart():
  print("""\n You open your eyes and find yourself stuck in a room dimly lit by torches.
  The room seems cramped from the inside, and the walls are made of solid stone.
  \n You rises to your feet and see two doors, one red and one blue. """)

  answer = (input("Type “red” to go through the red door, or “blue” to go through the blue door: ")).lower()

  if answer == ("red"):
    print("\nYou decide to walk through the red door.")
    redDoor()

  else:
    print("\nYou decide to walk through the blue door.")
    blueDoor()

#redDoor path
def redDoor():
  print ("""\nThe room you walk into is completely white, and the walls seem to be invisible to the eye. 
  \n The only visible objects in the room are 3 potions: a potion in all black that smelled of death, 
  another potion that was pink and bubbly, and another potion that was gold and smelled of flowers.
  You hear a faint gentile voice whispering, “Hey… drink the gold potion…”""")

  answer = (input("\n Choose a potion to drink. Type “black,” “pink,” or “gold”: ")).lower()
  if answer == ("black"):
    blackPotion()

  elif answer == ("pink"):
    pinkPotion()

  else:
    goldPotion()

def blackPotion():
  print("""You drink the black potion. 
  Immediately, you fall to the ground and slowly feel your consciousness fading away""")

  answer = (input("\n You Died.\n Press n to try again or any other key to quit: ")).lower()

  if answer == ("n"):
    gameStart()

  else:
    print("\nFarewell")
    quit()

def pinkPotion():
  print("""\n You drink the pink potion. The red door behind you suddenly disappears.
  The voice asks “I see you’ve made your choice…why do you stray from my directions..? 
  Now you will never be able to leave this room.” 
  The voice disappears and you remain stuck in the room forever...
  YOU FAILED""")
  answer = (input("""\n You went insane and died of starvation. 
  Press n to try again or any other key to quit: """)).lower()

  if answer == ("n"):
    gameStart()

def goldPotion():
  print("""\n You drink the gold potion. After a few seconds, you notice that your vision has improved, 
  and suddenly the room changes. 
  The room is no longer all white and returns to its original color. 
  A yellow door appears before you and you hear that voice again.
  Type “A”, “B”, or “C” to ask the voice a question: 
  a: Where am I? b: Who are you? c: What do you want from me?""")

  answer = input("""\n What will you ask the voice?: """).lower()

  if answer == ('a'):
    print("""\n“…You are in a place between what’s real and fiction… 
    a place where life and death are real…but the impossible can become possible… 
    There are bad people in this place…but you can triumph over them…”""")
    yellowDoor()

  elif answer == ('b'):
    print(""""“\nThink of me as your guide… 
    I will provide you with all that you need to achieve what you truly desire… 
    \n Do not listen to outsiders…they will try to deceive you…”""")

    yellowDoor()

  elif answer == ('c'):
    print("""\n“…I have your best interests in mind…I want to lead you to what you deserve…
    \n I recommend you follow the path I chose for you…or you will pay the price”""")
    yellowDoor()

def yellowDoor():
  print("""\nYou walk through the yellow door. 
  The room was a surprisingly large atrium with little to no lighting, 
  and it had multiple different hallways connecting to this one area. 
  In the center of the room was a large black portal outlined in red that glowed from . 
  The voice explains, 
  “...you do not belong here…I have constructed this to lead you to where you belong…It’s what you deserve…
  Please…jump through the gateway for your own good…” 
  In the corner of your eye, you see a beaten down man. 
  You attempt to hide from the voice, 
  and the man began motioning to you as if he were telling you to get away from the portal and follow him. """)

  answer = (input("\n Type “1” to jump through the portal or type “2” to follow the man: "))

  if answer == ('1'):
    print("""\n You disregard the man and jump into the portal. 
    You wakes up in a hospital bed having no idea what had just happened. 
    The doctor explains that a hiker had found you sprawled out in front of an entrance 
    to a large cave, and called for help. 
    You made it out of the ER the same day and left without any injuries. 
    Your memory of the dungeon was completely wiped off an hour after waking up, 
    and you lived a completely normal life after the incident. 
    \n YOU ESCAPED \n The End.""")

  elif answer ==('2'):
    print("""\n You decide to run from the voice and follow the man. The man leads you into one of the many 
    corridors connected to the main complex, both sprinting as fast as they could. 
    The corridor began to grow darker and darker until you could not even see the man running 
    in front of you anymore. You continue to run to not lose sight of the man, but in the process, 
    you unintentionally set off a trap that began firing arrows. The man deceived you.""")

    answer = (input("""\n You Died of blood loss and shock from the arrows...
    Press n to try again or any other key to quit: """)).lower()

    if answer == ("n"):
      gameStart()

    else:
      print("\nFarewell")
      quit()

#blueDoor path
def blueDoor():
  print("""\n On the other side of the door was a narrow hallway that seemed to extend for ages. 
  In the distance, you hear what sounded like a woman crying. 
  As you walked further down the hall, the echo of your voice grew louder and louder 
  until eventually both of your eyes and the woman's meet for a split second. 
  The woman yells, “Get away from me! Take one more step towards me and I’ll make sure you don’t walk again!” while sobbing""")

  answer = (input("\n Type “1” to follow the woman’s wishes and move on to the next room or type “2” to try to calm her down: "))

  if answer == ('1'):
    print("""\n You listened to the woman’s demands and left her alone.""")
    leftAlone()

  elif answer ==('2'):
    print("""\n You attempt to talk to the woman calmly and walk slowly towards her. 
    You explain that you didn't want to hurt her and that you had no idea how they got here in the first place. 
    The woman suddenly snapped and yelled “Nice try demon! I tried to warn you!” 
    She pulled out a sharp object from her pocket and attacked you.""")

    answer = (input("\n You Died from the stab wounds...\n Press n to try again or any other key to quit: ")).lower()

    if answer == ("n"):
      gameStart()

    else:
      print("\nFarewell")
      quit()

def leftAlone():
  print("""\n You moved around slowly to avoid her, and continue on through the hallway. Eventually you reach the end 
  of the hallway and found the next room. There in the room was a die laying on a table with two potential buttons to press. 
  One read “higher” the other “lower”. There was a green door behind this table, but unfortunately it was locked 
  from the inside. An automated voice coming from a speaker explained the rules of the game. 
  “To get to the treasure, you must correctly guess the number you will roll with the die. If you believe the number 
  you roll will be 4 or higher, press the “higher” button. 
  If you believe the number you roll will be 3 or lower, press the “lower” button. """)

  answer = (input("\n Type “higher” to press the higher button, or “lower” to press the lower button: ")).lower()

  if answer == ("higher"):
    print("""{You press the “higher” button. You roll the die and it lands on 1. 
    A trapdoor from under your feet is released and 
    You fall into a pit of poisonous snakes. \n YOU DIED""")

    answer = (input("\n Press n to try again or any other key to quit: ")).lower()

    if answer == ("n"):
      gameStart()

    else:
      print("\nFarewell")
      quit()

  elif answer == ("lower"):
    print("""\n You press the “lower” button then roll the die. It lands on 1.""")
    takeTreasure()

def takeTreasure():
  print(""" The green door unlocks and creeks open. The automated voice reactivates: 
  “Congratulations, you are worthy of entering the treasure room.” 
    [pronoun] walks inside the room and finds a ton of gold and valuables for the taking. 
    What especially caught your attention, however, was a gold statue that stood on a pedestal 
    that looked like it could sell for a fortune.
    \n Do you take the statue?""")

  answer = (input("Type “yes” or “no”: ")).lower()

  if answer == ('yes'):
    print("\n You take the statue. ")
    stoleStatue()

  elif answer == ('no'):
    print("""\nYou choose not to take the statue out of fear of it being a trap, 
    and instead take a few gold coins instead. 
    After some frantic searching, you found the exit with relative ease, but 
    a small part of you still wishes that you took the statue back home. 
    \n YOU ESCAPED!""")

def stoleStatue():
  print("""\n As soon as you pick up the statue, the entire room started to rumble. 
  One of the walls of the treasure room lifted up to reveal a fire-breathing dragon. 
  You bolted out of the treasure room with the statue as the dragon started chasing you. 
  You run from corridor to corridor trying to find a way out. 
  Eventually You find a corridor with what looked to have light from the outside peeking from a corner. 
  However, you fear that the exit was a trap 
  and that it might be better to find another way out.""")

  answer = (input("\n Type “A” to attempt to escape or type “B” to continue searching for an exit: ")).lower()

  if answer == ('a'):
    print("""You make a run for the potential exit. The exit was luckily real and 
    you ran out of the dungeon unscathed. You were able to sell the statue for millions of dollars 
    and lived a luxurious and comfortable life. \nThe End. """)

  elif answer == ('b'):
    print(""" You try to search for another exit in fear of each corridor being a trap. 
    Unfortunately, you run into a dead end while trying to find the second exit. 
    The dragon spits fire at you, burning you alive. \nYOU DIED """)

gameStart()