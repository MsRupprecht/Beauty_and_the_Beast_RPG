from room import Room
from item import Item
from item import Petal
from character import Enemy
from character import Friend
from character import Beast
from rpginfo import RPGInfo
from backpack import Backpack

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

plumette=Friend("Plumette","A feather duster who is going steady \
with Lumiere.")
plumette.set_conversation("Lumiere?  I've been burnt by him before.")
balcony.set_character(plumette)

gaston=Enemy("Gaston","A manly man.  A pure paragon.")
gaston.set_conversation("I'm especially good at expectorating!")
gaston.set_weakness("eggs")
throne.set_character(gaston)

lefou=Enemy("LeFou","Gaston's punching bag.")
lefou.set_conversation("Gaston is the best, and the rest is all drips!")
lefou.set_weakness("portrait of Gaston")
antechamber.set_character(lefou)

bimbettes=Enemy("The Bimbette Squad","Claudette, Laurette, and Paulette.\n\
Gaston's fan club.")
bimbettes.set_conversation("Gaston? Isn't he dreamy?  Oh, he's so cute.")
bimbettes.set_weakness("tiara")
ballroom.set_character(bimbettes)

posse=Enemy("Gaston's posse","Tom, Dick, and Harry.\n\
Gaston's best friends, as far has he has friends.")
posse.set_conversation("No one's slick as Gaston, no one's quick as Gaston!")
posse.set_weakness("mead")
dining_hall.set_character(posse)


beast=Beast("Beast","An angry beast who rules the castle.  His \
selfishness is the cause of the castle's enchantment.")
beast.set_conversation("I told you the West Wing was FORBIDDEN!!")
west_wing.set_character(beast)


# Items - instantiating and setting characteristics
portrait=Item("portrait of the royals on a day out")
portrait.set_description("A small oil painting commemorating the annual \
royal hunting trip.  Gaston is seen in the bottom corner as part of the \
team.")
ballroom.link_item(portrait)

chaise=Item("chaise lounge")
chaise.set_description("A burgundy sofa with hand carved wooden details.")
antechamber.link_item(chaise)

tiara=Item("tiara")
tiara.set_description("A delicate silver and ruby tiara.")
throne.link_item(tiara)

eggs=Item("eggs")
eggs.set_description("5 dozen eggs")
kitchen.link_item(eggs)

mead=Item("mead")
mead.set_description("A round of mead")
kitchen.link_item(mead)

mirror=Item("mirror")
mirror.set_description("A pocket mirror")
servants.link_item(mirror)

enchanted_mirror=Item("enchanted mirror")
enchanted_mirror.set_description("A magic mirror that lets the viewer \
see anyone anywhere.")
beast.set_gift(enchanted_mirror)

lantern=Item("lantern")
lantern.set_description("A lantern, ready to be lit.")

test_item=Item("test")
test_item.set_description("test text here")
entry.link_item(test_item)

petal1=Petal("rose petal from Mrs. Potts")
mrs_potts.set_gift(petal1)
petal2=Petal("rose petal from Lumiere")
lumiere.set_gift(petal2)
petal3=Petal("rose petal from Lumiere")
cogsworth.set_gift(petal3)
petal4=Petal("rose petal from Plumette")
plumette.set_gift(petal4)
petal5=Petal("rose petal from Wardrobe")
wardrobe.set_gift(petal5)
petal6=Petal("rose petal from Chip")
chip.set_gift(petal6)


# Backpack set up
bag=Backpack("Belle's backpack")
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



# Instantiating the game information
castle=RPGInfo("'Investigating the Beast'")


### Gameplay ###

# Initial conditions and introduction
print(gaston.get_backpack())
current_room=entry
playing=True
castle.welcome()
print("-----")
castle.intro()
print("-----")
print("There are",Room.number_of_rooms,"rooms in the castle to explore.")
print("The Beast is not known for taking visitors, so he will take some \
convincing.  \nHe has friends in the castle, and if you make a good impression \
they might pass along a good word and warm him up for you.  \nThey will update \
you on his mood as you meet them.")
print("Thanks to your study of the legend of the Beast, you know to keep an \
eye open for anything related to his enchanted rose.")
### In here we need information about how to play the game,
# ie enter a for option [a] and such


# Starting the game options

while playing == True:


    current_room.print_basic_room_description()
    
    command = input("\nWhat action would you like to take? \n\
[a] check if anyone is in the room\n\
[b] look for items in the room\n\
[c] check your backpack\n\
[d] move to another room\n\
[e] Exit game \n\
>> ")


    # Decide to either check for inhabitants, look for items to collect
    # check your backpack, or move to a different room

    # Check who is in the room
    if command.lower() == "a":
        optionA = True
        # While loop keeping it at the character level
        while optionA == True:
            # Introduce the character
            inhabitant = current_room.get_character()
            if inhabitant is not None:
                print("-----\n"+inhabitant.get_name(),"is here!")
                print("Biography:",inhabitant.describe())
                # Decide what to do next
                command2 = input("-----\nWhat action would you like to take?\n\
[a] Ask "+str(inhabitant.get_name())+" why they are here.\n\
[b] Walk away.\n\
>> ")
                if command2.lower() == "a":
                    option2A = True
                    command3_count = 0
                    while option2A == True:
                    # Check if friend or enemy, then give response
                        if isinstance(inhabitant,Friend):
                            if command3_count == 0:
                                print("-----\nI have lived and worked in \
the castle for years. \n\
How can I help you?")
                            option3A = True
                            command3 = input("-----\nWhat action would \
you like to take next?\n\
[a] Ask if they have any information about the Beast.\n\
[b] Ask if they have any object that could help you.\n\
[c] Ask them to talk to the Beast on your behalf.\n\
[d] Check on the Beast's mood.\n\
[e] Walk away\n\
>> ")
                            command3_count = command3_count+1
                            while option3A == True:
                                if command3.lower() == "a":
                                    if inhabitant.get_beast_info() is not None:
                                        print("-----\n"+inhabitant.get_beast_info())
                                        option3A = False
                                    else:
                                        print("-----\nI don't know anything useful about the Beast.")
                                        option3A = False
                                elif command3.lower() == "b":
                                    if inhabitant.get_gift() is not None:
                                        print("I have something special that will help you win \
the Beast's favour.")
                                        print("A",inhabitant.gift.get_name(),"appears in your backpack.")
                                        bag.set_contents(inhabitant.gift)
                                        bag.add_petal()
                                        print("Your bag now contains:",bag.get_contents_names())
                                        inhabitant.set_gift(None)
                                        option3A = False
                                    else:
                                        print("I do not have anything that could help you.")
                                        option3A = False
                                elif command3.lower() == "c":
                                    if inhabitant.get_beast_influence() == True:
                                        print("-----\nOf course! I'll speak to \
him and let him know you can be trusted.")
                                        beast.increase_heart()
                                        inhabitant.change_beast_influence()
                                        option3A = False
                                    else:
                                        print("-----\nI have already spoken to the Beast \
for you.  \n\
I don't think talking to him again would be helpful.")
                                        option3A = False
                                elif command3.lower() == "d":
                                    if beast.get_heart() < 3:
                                        print("-----\nThe Beast is not pleased.")
                                        print("I'd rate his mood",beast.get_heart(),"/ 10")
                                        option3A = False
                                    elif beast.get_heart() < 6:
                                        print("-----\nThe Beast is warming up to the idea of a visitor.")
                                        print("I'd rate his mood",beast.get_heart(),"/ 10")
                                        option3A = False
                                    else:
                                        print("-----\nI'd rate his mood",beast.get_heart(),"/ 10")
                                        print("The Beast is feeling friendlier than usual. \n\
If you bring him the four missing petals from his rose, I'm sure that would make his mood 10 / 10.")
                                        option3A = False
                                elif command3.lower() == "e":
                                    option3A = False
                                    option2A = False
                                else:
                                   print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
                        elif isinstance(inhabitant,Enemy):
                            if command3_count == 0:
                                print("-----\nI am no friend of the Beast, if that is what you mean.\n\
What do you want?\n\
>> ") #update the character class for individual responses
                                option3B = True
                                command3 = input("-----\nWhat action would you like to take?\n\
[a] Try to distract them with something from your bag.\n\
[b] Ask them if they have any rose petals.\n\
[c] Walk away.\n\
>> ")
                            command3_count=command3_count+1
                            while option3B == True:
                                if command3.lower() == "a":
                                    print("In your bag you have:",bag.get_contents_names())
                                    combat_item_str = input("What will you use to try to distract "+inhabitant.name+"?\n\
>> ")
                                    
                                    if combat_item_str in bag.get_contents_names():
                                        #convert string into object
                                        combat_item = None
                                        for item in bag.get_contents():
                                            if item.get_name() == combat_item_str:
                                                combat_item = item
                                        #do the fight
                                        inhabitant.fight(combat_item,bag)
                                        option3B = False

                                    else:
                                        print("That item is not in your backpack.")
                                        option3B = False
                                # Ask if they have petals
                                elif command3.lower() == "b":
                                    if inhabitant.backpack.get_petal_count() == 0:
                                        print("No, I do not have any rose petals.")
                                    elif inhabitant.get_petal_count() == 1:
                                        print("Yes, I have a rose petal.\nIf you found my favourite item in the castle, I might consider a trade.")
                                    else:
                                        print("I have",inhabitant.get_petal_count(),"rose petals.\nIf you found my favourite item in the castle, I might consider a trade.")
                                    option3B = False
                                # Walk away
                                elif command3.lower() == "c":
                                    option3B = False
                                    option2A = False
                                    optionA = False
                                else:
                                    print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

                            option2A= False

                        elif isinstance(inhabitant,Beast):
                            print("-----\nI am the Beast")
                            option2A = False
                        else:
                            print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
                elif command2.lower() == "b":
                    optionA = False
                else:
                    print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
            else:
                print("-----\nThere are no characters in this room.")
                optionA = False

    elif command.lower() == "b":
        optionB = True
        while optionB == True:
            if len(current_room.get_items()) != 0:
                print("-----\nInside the room, you can see:",current_room.get_item_names())
            else:
                print("-----\nThere are no items inside this room")
            option2 = input("What action would you like to take? \n\
[a] Show the contents of your backpack. \n\
[b] Pick up an item. \n\
[c] Leave an item behind. \n\
[d] Walk away \n\
[e] Exit game \n\
>> ")
            if option2.lower() == "a":
                print("-----\nYour bag contains:",bag.get_contents_names())
            elif option2.lower() == "b":
                new_item = input("Which item do you want to pick up?\n>>")
                added_items = 0
                for item in current_room.linked_items:
                    if new_item == item.name:
                        bag.set_contents(item)
                        current_room.linked_items.remove(item)
                        added_items = added_items+1
                if added_items == 1:
                    print("-----\nThe",new_item,"was added to your backpack.")
                    print("The room now contains:",current_room.get_item_names())
                    print("Your bag now contains:",bag.get_contents_names())
                elif added_items >1:
                    print("-----\nThere was an error here.  \n\
May the odds be ever in your favour.\n")
                else:
                    print("-----\nThat item could not be added.")
            elif option2.lower() == "c":
                left_item=input("Which item would you like to leave?\n>>")
                removed_items=0
                for item in bag.contents:
                    if left_item == item.name:
                        bag.remove_contents(item)
                        current_room.linked_items.append(item)
                        removed_items = removed_items+1
                if removed_items == 1:
                    print("-----\nThe",left_item,"was removed from your bag.")
                    print("The room now contains:",current_room.get_item_names())
                    print("Your bag now contains:",bag.get_contents_names())
                else:
                    print("-----\nThat item could not be removed from your bag.\n")
            elif option2.lower() == "d":
                print("-----\nLet's get out of here!")
                optionB = False
            elif option2.lower() == "e":
                optionB = False
                playing = False
            else:
                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

    # Check backpack contents
    elif command.lower() == "c":
        optionC = True
        while optionC == True:
            print("-----\nYour bag contains:",bag.get_contents_names())
            optionC = False

    # Move to another room
    elif command.lower() == "d":
        optionD = True
        while optionD == True:
            print("-----\nNearby rooms:")
            current_room.print_linked_rooms()
            direction = input("-----\nWhich direction do you want to move? \n\
Use the full direction name.\n\
>> ")
            if direction in current_room.get_linked_rooms():
                current_room = current_room.move(direction)
                optionD = False
            else:
                print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")
    elif command.lower() == "e" or command.lower() == "exit":
        playing = False
    else:
        print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

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
