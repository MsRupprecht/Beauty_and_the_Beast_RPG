import time

from room import Room
from item import Item
from item import Petal
from character import Enemy
from character import Friend
from character import Beast
from rpginfo import RPGInfo
from backpack import Backpack
from progress_bar import Progress_bar

# Rooms - instantiating and setting characteristics
entry=Room("entry hall")
entry.set_description("A fairytale come true, with sweeping staircases \
to take you up to the balcony.")

kitchen=Room("kitchen")
kitchen.set_description("A spacious work room with all the \
equipment you could possibly need to host a feast.")

ballroom=Room("ballroom")
ballroom.set_description("A grand room with plenty of space for dancing.")

dining_hall=Room("dining hall")
dining_hall.set_description("A wide room with one long table and several \
smaller tables along the walls.  Grandly appointed to impress visitors \
from any land.")

servants=Room("servants' quarters")
servants.set_description("A rough, but pleasant, set of accomodation for \
the staff working and living in the castle.")

library=Room("library")
library.set_description("A magnificent room with more books than \
you could read in a lifetime.  There are even rolling ladders to \
reach the books on the highest shelves.")

antechamber=Room("antechamber")
antechamber.set_description("A waiting room for those about to visit the \
throne room.  Plenty of seating to keep everyone comfortable.")

throne=Room("throne room")
throne.set_description("The most marvelous room you'll ever see. \
Stained glass windows let in afternoon sun and a gilded throne with deep \
purple velvet cushions.")

balcony=Room("balcony")
balcony.set_description("An open landing with access to the top floor.")

east_wing=Room("east wing")
east_wing.set_description("The upstairs wing of the castle with the bedrooms.")

west_wing=Room("west wing")
west_wing.set_description("The forbidden wing of the castle.  DO NOT ENTER!")


# Rooms - linking directions
west_wing.link_room(balcony,"east")

east_wing.link_room(balcony,"west")

balcony.link_room(entry,"down stairs")
balcony.link_room(east_wing,"east")
balcony.link_room(west_wing,"west")

entry.link_room(dining_hall,"north")
entry.link_room(ballroom,"east")
entry.link_room(library,"west")
entry.link_room(balcony,"up stairs")

dining_hall.link_room(entry,"south")
dining_hall.link_room(kitchen,"east")
dining_hall.link_room(antechamber,"west")

antechamber.link_room(throne,"west")
antechamber.link_room(dining_hall,"east")
antechamber.link_room(library,"south")

throne.link_room(antechamber,"east")

library.link_room(antechamber,"north")
library.link_room(entry,"east")

ballroom.link_room(entry,"west")
ballroom.link_room(kitchen,"north")

kitchen.link_room(dining_hall,"west")
kitchen.link_room(ballroom,"south")
kitchen.link_room(servants,"east")

servants.link_room(kitchen,"west")


# Characters - instantiating and setting characteristics
lumiere=Friend("Lumiere","Castle maitre d' and all around entertainer, \
as well as Cogworth's reluctant best friend.")
lumiere.set_conversation("Be our guest, be our guest.  Put our service \
to the test!")
lumiere.set_beast_info("The Beast is often angry, but you can reason with him. \n\
First, you must gain his trust. \n\
If you get to know the staff around the castle, we can put in a good word \
for you.")
entry.set_character(lumiere)

cogsworth=Friend("Cogsworth","The castle's tightly wound head of \
household and Lumiere's reluctant best friend.")
cogsworth.set_conversation("If it's not Baroque, don't fix it.")
cogsworth.set_beast_info("Beware of the Beast's enemies. \n\
They are vapid, but practised in the art of slight of hand.")
library.set_character(cogsworth)

mrs_potts=Friend("Mrs. Potts","A motherly teapot who always has a \
warm word on offer.")
mrs_potts.set_conversation(" have found that most troubles seem less \
troubling after a bracing cup of tea.")
mrs_potts.set_beast_info("Oh, that poor boy.  Yes, he is troubled. \n\
He is often thinking about that rose the old lady gave him. \n\
It has been losing petals for some time now.")
kitchen.set_character(mrs_potts)

chip=Friend("Chip","The tiniest cup in the cabinet, who is full of \
personality.")
chip.set_conversation("Mama, there's a girl in the castle!")
chip.set_beast_info("The Beast is scary! I never go up to the West Wing.")
servants.set_character(chip)

wardrobe=Friend("Wardrobe","The castle's opera singer and lady in waiting.")
wardrobe.set_conversation("Let's see if we can find you something nice \
and shiny to wear to dinner.")
wardrobe.set_beast_info("Sometimes the Beast's enemies will steal petals\
from his rose.  \nBut they each have a weakness that will distract them \
just long enough, if you happen to be missing anything.")
east_wing.set_character(wardrobe)

# plumette=Friend("Plumette","A feather duster who is going steady \
# with Lumiere.")
# plumette.set_conversation("Lumiere?  I've been burnt by him before.")
# balcony.set_character(plumette)

gaston=Enemy("Gaston","A manly man.  A pure paragon.")
gaston.set_conversation("I'm especially good at expectorating!")
gaston.set_weakness("eggs")
throne.set_character(gaston)
gaston.set_response("I'm here for the hunt, of course!  \n\
We'll save our village and our lives.  \n\
We'll kill the Beast!")

lefou=Enemy("LeFou","Gaston's punching bag.")
lefou.set_conversation("Gaston is the best, and the rest is all drips!")
lefou.set_weakness("painting of Gaston")
antechamber.set_character(lefou)
lefou.set_response("I go wherever Gaston goes.")

bimbettes=Enemy("The Bimbette Squad","Claudette, Laurette, and Paulette.\n\
Gaston's fan club.")
bimbettes.set_conversation("Gaston? Isn't he dreamy?  Oh, he's so cute.")
bimbettes.set_weakness("tiara")
ballroom.set_character(bimbettes)
bimbettes.set_response("We never miss an opportunity to twirl in a ballroom.")

posse=Enemy("Gaston's posse","Tom, Dick, and Harry.\n\
Gaston's best friends, as far has he has friends.")
posse.set_conversation("No one's slick as Gaston, no one's quick as Gaston!")
posse.set_weakness("mead")
dining_hall.set_character(posse)
posse.set_response("We have a blind and stubborn believe that what we're doing is right.\n\
We also assumed the castle would be food and treasures for us to loot.")

beast=Beast("Beast","An angry beast who rules the castle.  His \
selfishness is the cause of the castle's enchantment.")
beast.set_conversation("I told you the West Wing was FORBIDDEN!!")
west_wing.set_character(beast)


# Items - instantiating and setting characteristics
painting = Item("painting of Gaston")
painting.set_description("A small oil painting commemorating the annual \
royal hunting trip.  Gaston is seen in the bottom corner as part of the \
team.")
ballroom.link_item(painting)

chaise = Item("chaise lounge")
chaise.set_description("A burgundy sofa with hand carved wooden details.")
antechamber.link_item(chaise)

tiara = Item("tiara")
tiara.set_description("A delicate silver and ruby tiara.")
throne.link_item(tiara)

eggs = Item("eggs")
eggs.set_description("5 dozen eggs")
kitchen.link_item(eggs)

mead = Item("mead")
mead.set_description("A round of mead")
kitchen.link_item(mead)

book = Item("book")
book.set_description("A book of short stories")
servants.link_item(book)

enchanted_mirror = Item("enchanted mirror")
enchanted_mirror.set_description("A magic mirror that lets the viewer \
see anyone, anywhere.")
beast.set_gift(enchanted_mirror)

planner = Item("planner")
planner.set_description("A day planner, ready to be filled with tasks and schedules.\n\
Includes a generous notes section for brainstorming ideas.")

lantern = Item("lantern")
lantern.set_description("A lantern, ready to be lit.")



petal1=Petal("rose petal from Mrs. Potts")
mrs_potts.set_gift(petal1)
petal2=Petal("rose petal from Lumiere")
lumiere.set_gift(petal2)
petal3=Petal("rose petal from Lumiere")
cogsworth.set_gift(petal3)
# petal4=Petal("rose petal from Plumette")
# plumette.set_gift(petal4)
petal5=Petal("rose petal from Wardrobe")
wardrobe.set_gift(petal5)
petal6=Petal("rose petal from Chip")
chip.set_gift(petal6)


# Backpack set up
bag = Backpack("Belle's backpack")
bag.set_description("A roomy bag with some basic supplies and space for more.")
bag.set_contents(lantern)

bag_gaston = Backpack("Gaston's backpack")
gaston.set_backpack(bag_gaston)
bag_lefou = Backpack("LeFou's backpack")
lefou.set_backpack(bag_lefou)
bag_bimbettes = Backpack("The Bimbettes' backpack")
bimbettes.set_backpack(bag_bimbettes)
bag_posse = Backpack("Gaston's posse's backpack")
posse.set_backpack(bag_posse)
bag_beast = Backpack("The Beast's backpack")
beast.set_backpack(bag_beast)

# Progress bar set up
intruders_bar = Progress_bar("Intruders Distracted",4)
petals_bar = Progress_bar("Petals Collected",5)
mood_bar = Progress_bar("Beast's Mood",10)


# Instantiating the game information
castle=RPGInfo("'Investigating the Beast'")


### Gameplay ###

# Initial conditions and introduction
current_room=entry
playing=True
castle.welcome()

# print("-----")
# castle.intro()
# input("Press enter to continue.\n\
# >> ")
# castle.castle_image()
# print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
# print("There are",Room.number_of_rooms,"rooms in the castle to explore.")
# print("The Beast is not known for taking visitors, so he will take some \
# convincing.  \n\
# He has friends in the castle, and if you make a good impression \
# they might pass along a good word for you.  \n\
# They will update you on his mood as you meet them.")
# print("Thanks to your study of the legend of the Beast, you know to keep an \
# eye open for anything related to his enchanted rose.")
# print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
# input("Press enter to walk into the castle.")
# ### In here we need information about how to play the game,
# # ie enter a for option [a] and such


# Starting the game options

while playing == True:

    current_room.print_basic_room_description()
    # Level One Menu - What to do in the room
    # Decide to either check for inhabitants, look for items to collect
    # check your backpack, check your progress, or move to a different room
    command = input("-----\nWhat action would you like to take? \n\
[a] Check if anyone is in the room\n\
[b] Look for items in the room\n\
[c] Check your backpack and progress status\n\
[d] Move to another room\n\
[e] Exit game \n\
>> ")

    # Check who is in the room
    # Sub menus include character interactions
    if command.lower() == "a":
        optionA = True
        # While loop keeping it at the character level
        while optionA == True:

            # Introduce the character
            inhabitant = current_room.get_character()
            if inhabitant is not None:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n"+inhabitant.get_name(),"is here!")
                print("Biography:",inhabitant.describe(),"\n\n\n")
                
                # Decide if you want to interact
                # Sub menus dictate how to interact
                command2 = input("-----\nWhat action would you like to take?\n\
[a] Ask "+str(inhabitant.get_name())+" why they are here.\n\
[b] Walk away.\n\
>> ")

                # Interact with the character
                if command2.lower() == "a":
                    option2A = True
                    command3_count = 0
                    # While loop to keep it at the interaction level
                    while option2A == True:
                    
                    # Check if friend or enemy, then give response
                        # FRIEND response path
                        if isinstance(inhabitant,Friend):
                            if command3_count == 0:
                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI have lived and worked in the castle for years. \n\
How can I help you?\n\n\n")
                            option3A = True
                            # While loop to keep it at the information level ~~CHANGE HERE
                            while option3A == True:
                                command3 = input("-----\nWhat action would you like to take next?\n\
[a] Ask if they have any information about the Beast.\n\
[b] Ask if they have any object that could help you.\n\
[c] Ask them to talk to the Beast on your behalf.\n\
[d] Check on the Beast's mood.\n\
[e] Go to previous menu.\n\
>> ")
                                command3_count = command3_count+1


                                # Give information about the Beast, if known
                                if command3.lower() == "a":
                                    if inhabitant.get_beast_info() is not None:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n"+inhabitant.get_beast_info(),"\n\n\n")
                                        option3A = False
                                    else:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI don't know anything useful about the Beast.\n\n\n")
                                        option3A = False
                                
                                # Offer an object to help, if they have it
                                elif command3.lower() == "b":
                                    if inhabitant.get_gift() is not None:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI have something special that will help you win the Beast's favour.")
                                        print("A",inhabitant.gift.get_name(),"appears in your backpack.\n\n\n")
                                        bag.set_contents(inhabitant.gift)
                                        bag.add_petal()
                                        inhabitant.set_gift(None)
                                        option3A = False
                                    else:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI do not have anything that could help you.\n\n\n")
                                        option3A = False
                                
                                # Offer to talk to the Beast, if they haven't already
                                elif command3.lower() == "c":
                                    if inhabitant.get_beast_influence() == True:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nOf course! I'll speak to him and let him know you can be trusted.\n\n\n")
                                        beast.increase_heart()
                                        inhabitant.change_beast_influence()
                                        option3A = False
                                    else:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI have already spoken to the Beast for you.  \n\
I don't think talking to him again would be helpful.\n\n\n")
                                        option3A = False

                                # Respont with the Beast's mood
                                elif command3.lower() == "d":
                                    if beast.get_heart() < 3:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast is not pleased.")
                                        print("I'd rate his mood",beast.get_heart(),"/ 10\n\n\n")
                                        option3A = False
                                    elif beast.get_heart() < 6:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast is warming up to the idea of a visitor.")
                                        print("I'd rate his mood",beast.get_heart(),"/ 10\n\n\n")
                                        option3A = False
                                    else:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI'd rate his mood",beast.get_heart(),"/ 10")
                                        print("The Beast is feeling friendlier than usual. \n\
If you bring him the four missing petals from his rose, I'm sure that would make his mood 10 / 10.\n\n\n")
                                        option3A = False
                                
                                # Exit the character level menu
                                elif command3.lower() == "e":
                                    option3A = False
                                    option2A = False
                                
                                # Incorrect menu selection, loop back to top of character interaction menu
                                else:
                                    print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

                        
                        # ENEMY response path
                        elif isinstance(inhabitant,Enemy):
                            if inhabitant.get_distracted_status() == True:
                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n",inhabitant.get_name(),"is distracted with the",inhabitant.get_weakness()+".  You get no response.\n\n\n")
                            
                            # Print the dialogue only once per interaction with the menu
                            elif command3_count == 0:
                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n"+inhabitant.get_response(),"\n\
What do you want?\n\n\n")
                                option3B = True
                                command3 = input("-----\nWhat action would you like to take?\n\
[a] Try to distract them with something from your bag.\n\
[b] Ask them if they have any rose petals.\n\
[c] Walk away.\n\
>> ")
                            command3_count=command3_count+1
                            # While loop to keep it at the enemy interaction level
                            while option3B == True:

                                # Attempt to distract the enemy
                                if command3.lower() == "a":
                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nIn your bag you have:",bag.get_contents_names(),"\n\n\n")
                                    combat_item_str = input("-----\nWhat will you use to try to distract "+inhabitant.name+"?\n\
Type out the full item name.\n\
>> ")
                                    # Check if the chosen item is in the backpack
                                    if combat_item_str in bag.get_contents_names():
                                        #convert string into object
                                        combat_item = None
                                        for item in bag.get_contents():
                                            if item.get_name() == combat_item_str:
                                                combat_item = item
                                        #do the fight
                                        inhabitant.fight(combat_item,bag)
                                        option3B = False

                                    # Item is not in the backpack, loop back up
                                    else:
                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThat item is not in your backpack.\n\n\n")
                                        option3B = False
                                
                                # Ask if they have petals
                                elif command3.lower() == "b":
                                    inhabitant.ask_petal_count()
                                    option3B = False
                                
                                # Walk away
                                elif command3.lower() == "c":
                                    option3B = False
                                    option2A = False
                                    optionA = False
                                
                                # Incorrect menu input, loop back up
                                else:
                                    print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

                            option2A= False

                        # BEAST response path
                        elif isinstance(inhabitant,Beast):
                            print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nI am the Beast and this is my castle.\n\n\n")
                            option3C = True
                            
                            # Loop to keep it at the Beast interaction level
                            while option3C == True:
                                
                                # If the Beast is still in a bad mood
                                if inhabitant.get_heart() < 5: 
                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou are no friend of mine - GET OUT!")
                                    print("...\n...\n...")
                                    print("You run out of the library quick as you can.\n\n\n")
                                    current_room = balcony
                                    option3C = False
                                    option2A = False
                                    optionA = False

                                # If the Beast is ready for visitors
                                else:
                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast appears reluctant, but allows you to enter the West Wing.\n\
A better question is, what are *you* doing here?\n\n\n")
                                    command3C = input("-----\nWhat action would you like to take?\n\
[a] Offer the beast the "+str(bag.get_petal_count())+" rose petals you collected.\n\
[b] Run away\n\
>> ")
                                    # Offer the petals
                                    if command3C.lower() == "a":
                                                                                        
                                            # Give the Beast the petals
                                            # See the mood increase
                                            if command3C.lower() == "a":
                                                temp_list = []
                                                #temp list (above) to hold the petals as they transfer bags (below)
                                                for item in bag.get_contents():
                                                    if isinstance(item,Petal):
                                                        temp_list.append(item)
                                                for item in temp_list:
                                                    bag.remove_contents(item)
                                                    bag_beast.set_contents(item)
                                                    inhabitant.increase_heart()

                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYour gift of the missing rose petals has weakened the curse's strength and he is starting to relax.")
                                                print("The Beast's mood is now",inhabitant.get_heart(),"/ 10.\n\n\n")
                                                
                                                # If the petals boost the Beast to full power
                                                if inhabitant.get_heart() >= 10:
                                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast is ready to talk.\n\n\n")

                                                    # If any enemies remain active
                                                    while Enemy.distracted_enemies < 4 and playing == True:
                                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou move towards the Beast, but hear a rustling behind you.\n\n\n")
                                                        command4C = input("-----\nWhat do you do?\n\
[a] Give the Beast your full attention and introduce yourself.\n\
[b] Turn and investigate the noise\n\
>> ")

                                                        # Ignore noise, straight to defenestration scene
                                                        if command4C.lower() == "a":
                                                            print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou introduce yourself to the Beast and begin to explain that you have come to the castle to help him understand the needs of the community.")
                                                            print("Suddenly, you are interrupted by a body pushing past you.")
                                                            for character in Enemy.enemy_list:
                                                                if character.distracted == False:
                                                                    print("You see",character.get_name(),"run towards the Beast.")
                                                            print("There is a struggle.  The fight moves towards the window and you see the Beast lose his balance.")
                                                            print("The enemies of the Beast were not fully distracted, and defenestrated him before you were able to convince him to change his ways and see to the needs of the community.\n\n\n")
                                                            option3C = False
                                                            option2A = False
                                                            optionA = False
                                                            playing = False
                                                        
                                                        # Investigate noise - opportunity to distract
                                                        elif command4C.lower() == "b":
                                                            print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n")
                                                            # See who is here
                                                            if len(Enemy.active_list) > 1:
                                                                print("You look behind you and see:")
                                                                for character in Enemy.active_list:
                                                                    print(character.get_name())
                                                            elif len(Enemy.active_list) == 1:
                                                                print("You look behind you and see",Enemy.active_list[0].get_name())
                                                            else: 
                                                                print("You look behind you, but don't see anyone.\n\
                                                                      It is an old castle, so noises are bound to happen.") #THIS SHOULDN'T ACTIVATE

                                                            # Open bag to see what we can distract with
                                                            print("{} will surely ruin any chance of negotiating with the Beast.  You hope something in your backpack can be used to distract them.".format("This enemy" if len(Enemy.active_list) == 1 else "These enemies"))
                                                            print("You open your bag and find:")


                                                            #loop here to go through all the items in my bag to try to distract the enemy/enemies
                                                            fighting = True
                                                            while fighting == True and len(bag.get_contents()) != 0:
                                                                # Select combat item
                                                                print(bag.get_contents_names(),"\n\n\n")
                                                                combat_item_str = input("-----\nWhat will you use to fend off the {}".format("enemy?\n>> " if len(Enemy.active_list) == 1 else "enemies?\n>> "))
                                                                
                                                                # Check if it is a successful distraction
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n")
                                                                for character in Enemy.active_list:
                                                                    if character.get_weakness() == combat_item_str:
                                                                        print(character.get_name(), "was distracted by the", combat_item_str+".")
                                                                        character.set_as_distracted()
                                                                for character in Enemy.active_list:
                                                                    print(character.get_name(),"is still active and looks menacing.")
                                                                # Remove item from my bag
                                                                combat_item = None
                                                                for item in bag.get_contents():
                                                                    if item.get_name() == combat_item_str:
                                                                        combat_item = item
                                                                bag.remove_contents(combat_item)
                                                                print("\n\n\n")

                                                                # If there are no enemies, end fighting
                                                                if len(Enemy.active_list) == 0:
                                                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou successfully distracted all the enemies in the castle!  The Beast is grateful for your help, and  eager to listen to what you have to say.\n\n\n")
                                                                    fighting = False
                                                                
                                                                # If there are still enemies, but no items left
                                                                # End fighting and end game.
                                                                elif len(bag.get_contents()) == 0:
                                                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYour bag is empty, and the enemies are still pushing forward.")
                                                                    print("There is a struggle.  The fight moves towards the window and you see the Beast lose his balance.")
                                                                    print("The enemies of the Beast were not fully distracted, and defenestrated him before you were able to convince him to change his ways and see to the needs of the community.\n\n\n")
                                                                    fighting = False
                                                                    option3C = False
                                                                    option2A = False
                                                                    optionA = False
                                                                    playing = False
                                                                # If there are still enemies and items in my bag, keep looping
                                                                else:
                                                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe",combat_item_str,"didn't distract them, so you look in your bag and try again.\n\n\n")

                                                            # If all distracted, then go to end scene                                                   
                                                            option3C = False

                                                    # If all enemies are distracted --> Winning end scene
                                                    if playing == True:
                                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou sit down with the Beast and introduce yourself,  You explain that you are from the surrounding village and undertand that there is a lot of misinformation about the him and his history.")
                                                        time.sleep(1.8)
                                                        print("The Beast is a bit uncomfortable, but appreciates your point of view.")
                                                        print("You tell him that the kingdom is in need of leadership with the resources to make postive changes, and that it would really help if he could start participating in public life again.  If he would just come out and see what people are going through, he would understand.")
                                                        time.sleep(2.8)
                                                        print("The Beast gets out his magic mirror, and explains that it can show him anyone, anywhere, at any time.")
                                                        time.sleep(0.8)
                                                        print("You think that's a more than a bit creepy, but the mirror will be a useful tool to illustrate your point.  You make a mental note to address this with him after you make your case.\n\n\n")

                                                        option_end1 = True
                                                        while option_end1 == True:
                                                            example = input("-----\nWhat public works project do you want to encourage him to do first?\n\
[a] School funding\n\
[b] Food shortages\n\
>> ")
                                                            if example.lower() == "a":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou have the Beast look at the school and show him how understaffed and undersupplied they are.")
                                                                print("You explain that with proper funding, the school would be able to hire enough highly qualified and experienced teachers to properly support the students.  You remind him that the expectations and working conditions for teachers must also be reviewed if they are going to retain staff in the long term and best serve the young people in the kingdom.\n\n\n")
                                                                option_end1 = False
                                                            elif example.lower() == "b":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou have the Beast look at the food bank and see how long the line is and how bare the shelves are.")
                                                                print("You explain that with proper funding, the food bank would be able to serve every member of the community that was in need.  And even more important is proper funding and support for the kingdom's agriculture sector.  Cooperative planning amongst the different farms will help prevent the shortages of staple crops in the future.\n\n\n")
                                                                option_end1 = False
                                                            else:
                                                                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 
                                                        
                                                        
                                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast sits stands up and starts to pace.")
                                                        print("He tells you, 'I had no idea...Sure, sometimes I would use my mirror to look at life outside the castle, but all I could ever see was the misery.  I assumed it was part of the curse that had consumed the castle.  I thought it was inevitable.'\n\n\n")

                                                        option_end2 = True
                                                        while option_end2 == True:
                                                            response = input("-----\nHow do you want to respond to the Beast?\n\
[a] That is understandable, given what you went through when you were so young. \n\
[b] Huff, and roll your eyes. \n\
>> ")
                                                            if response.lower() == "a":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast thanks you for your understanding.\n\n\n")
                                                                option_end2 = False
                                                            elif response.lower() == "b":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast responds, 'How was I supposed to know? I was just 11 when this all happened to me!'")
                                                                print("You respond with an apology, and remember that you are here to try to move things forward, not take out your frustrations.\n\n\n")
                                                                option_end2 = False
                                                            else:
                                                                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 
                                                        
                                                        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nWell, now that you know what is happening, and that there are solutions within your control, let's do something about it.")
                                                        print("The Beast agrees, and vows to work with his kingdom and for his kingdom.")
                                                        time.sleep(1.8)
                                                        print("*  *  *  *\nSuddenly, you see petals floating and the rose begins to reform itself.  Lights start sparkling around the Beast and he is returned to his human form.  The curse is lifted!")
                                                        time.sleep(1.8)
                                                        print("*  *  *  * \nThe Beast, who had resigned himself to his fate long ago, is in a state of disbelief.")
                                                        print("You look at the Beast, and tell him that empathy is what makes us human, and the willingness to look out for each other is truly what binds us together.  As long as he stays true to that, the curse shouldn't be able to touch him.")
                                                        time.sleep(1.8)
                                                        print("*  *  *  *  \nThe Beast promises to be true and live every day with a thankful heart.  He asks you to be his Counsellor of State, to advise him and keep him accountable.")
                                                        print("You accept this position, and watch as the curse continues to melt away from the castle and its inhabitants.  As you do, you feel your backpack get a bit heavier.\n\n\n")
                                                        bag.set_contents(planner)

                                                        option_end3 = True
                                                        while option_end3 == True:
                                                            choice = input("-----\nWhat would you like to do next?\n\
[a] Open your bag and see what is inside.\n\
[b] Leave that mystery alone. \n\
>> ")
                                                            if choice.lower() == "a":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nInside your bag you see a day planner, ready for scheduling projects and brainstorming ways to serve the kingdom.")
                                                                print("You hear the Beast ask, 'What's next?' and you know things will work out just fine.\n\n\n")
                                                                option_end3 = False
                                                                optionA = False
                                                                playing = False
                                                            elif choice.lower() == "b":
                                                                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou think there has been more than enough excitement for one day, and it is probably time for everyone to get a good rest.")
                                                                print("You suggest to the Beast that he visits with his friends and explain everything that has happened.  In the meantime you will rest and return in the morning to start working on a plan.")
                                                                print("The Beast offers you a room in the East Wing of the castle, which you accept, as your home is rather far away.")
                                                                time.sleep(2.8)
                                                                print("In the morning, after you visit the kitchen for some breakfast, you hear noises in the library.  As you approach, you realise the Beast has gathered the enemies from around the castle and is holding his first town hall meeting.  He looks flustered, but is listening and taking notes.  You're optimistic that this is your opportunity to work hard and work worth doing.\n\n\n")
                                                                option_end3 = False
                                                                optionA = False
                                                                playing = False
                                                            else:print("\n.\n.\n.    Please try again.\n.\n.\n.\n") 
                                                        option3C = False 
                                                        optionA = False
                                                        playing = False

                                                
                                                # If the petals do not yet boost the Beast to full power
                                                if inhabitant.get_heart() < 10:
                                                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe Beast is not ready to talk yet.  There are two ways to convince the Beast to speak with you: encouragement from his friends in the castle, or rose petals to weaken the curse.  Only then will when all his friends are supporting him and the rose is full will the spell be weak enough for the Beast to see clearly.\n\n\n")
                                                    option3C = False
                                                    option2A = False

                                        
                                    # Leave the room
                                    elif command3C.lower() == "b":
                                        option3C = False
                                    
                                    # Incorrect menu option, loop back up
                                    else:
                                        print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 
                                
                                # End character interaction menu
                                option2A = False
                            # Incorrect menu option, loop back up
                        else:
                            print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 
                
                # Walk away from the character
                elif command2.lower() == "b":
                    optionA = False

                # Incorrect menu option, loop back up
                else:
                    print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 

            
            # No characters present to interact with, loop back up to room choice menu
            else:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThere are no characters in this room.\n\n\n")
                optionA = False

    # Look for items in the room
    # Sub menus include interacting with the items
    elif command.lower() == "b":
        optionB = True
        while optionB == True:
            if len(current_room.get_items()) != 0:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nInside the room, you can see:",current_room.get_item_names(),"\n\n\n")
            else:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThere are no items inside this room.\n\n\n")
            option2 = input("-----\nWhat action would you like to take? \n\
[a] Show the contents of your backpack. \n\
[b] Pick up an item. \n\
[c] Leave an item behind. \n\
[d] Go to previous menu \n\
>> ")
            if option2.lower() == "a":
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYour bag contains:",bag.get_contents_names(),"\n\n\n")
            elif option2.lower() == "b":
                new_item = input("-----\nWhich item do you want to pick up?\n\
Type the full name of the object\n\
>>")
                added_items = 0
                for item in current_room.linked_items:
                    if new_item == item.name:
                        bag.set_contents(item)
                        current_room.linked_items.remove(item)
                        added_items = added_items+1
                if added_items == 1:
                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe",new_item,"was added to your backpack.\n\n\n")
                elif added_items >1:
                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThere was an error here.  \n\
May the odds be ever in your favour.\n\n\n")
                else:
                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThat item could not be added.\n\n\n")
            elif option2.lower() == "c":
                left_item=input("-----\nWhich item would you like to leave?\n>>")
                removed_items=0
                for item in bag.contents:
                    if left_item == item.name:
                        bag.remove_contents(item)
                        current_room.linked_items.append(item)
                        removed_items = removed_items+1
                if removed_items == 1:
                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThe",left_item,"was removed from your bag.")
                else:
                    print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nThat item could not be removed from your bag.\n\n\n")
            elif option2.lower() == "d":
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nLet's get out of here!\n\n\n")
                optionB = False
            else:
                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

    # Check backpack contents
    # No sub menu
    elif command.lower() == "c":
        optionC = True
        while optionC == True:
            print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYour bag contains:",bag.get_contents_names())
            print("\nYour progress so far:")
            intruders_bar.set_progress(Enemy.distracted_enemies)

            intruders_bar.display_progress()
            petals_bar.set_progress(bag.get_petal_count())
            petals_bar.display_progress()
            mood_bar.set_progress(beast.get_heart())
            mood_bar.display_progress()
            print("\n\n\n")
            optionC = False

    # Move to another room
    # Sub menus are just navigation
    elif command.lower() == "d":
        optionD = True
        while optionD == True:
            print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nNearby rooms:")
            current_room.print_linked_rooms()
            print("\n\n\n")
            direction = input("-----\nWhich direction do you want to move? \n\
Use the full direction name.\n\
>> ")
            if direction in current_room.get_linked_rooms():
                current_room = current_room.move(direction)
                optionD = False
            else:
                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
    
    # Exit the game
    # The End
    elif command.lower() == "e" or command.lower() == "exit":
        check = input("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nAre you sure you want to quit?\n\
If yes, type YES in all caps.  If no, press enter.\n\
>>> ")
        if check == "YES":
            playing = False
        else:
            print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
    
    # Incorrect menu choice - loop back to level one menu
    else:
        print(".\n.\n.\n.    Please try again.\n.\n.\n.\n") 

# Game Over
print("\n\
   _____              __  __   ______   \n\
  / ____|     /\     |  \/  | |  ____|  \n\
 | |  __     /  \    | \  / | | |__     \n\
 | | |_ |   / /\ \   | |\/| | |  __|    \n\
 | |__| |  / ____ \  | |  | | | |____   \n\
  \_____| /_/    \_\ |_|  |_| |______|  \n\
  \n\
   ____   __      __  ______   _____    \n\
  / __ \  \ \    / / |  ____| |  __ \   \n\
 | |  | |  \ \  / /  | |__    | |__) |  \n\
 | |  | |   \ \/ /   |  __|   |  _  /   \n\
 | |__| |    \  /    | |____  | | \ \   \n\
  \____/      \/     |______| |_|  \_\  \n")

RPGInfo.author="Claire"
RPGInfo.credits()
RPGInfo.info()
