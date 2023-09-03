from backpack import Backpack
from item import Item
from item import Petal

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.backpack = None

    # Get character name
    def get_name(self):
        return self.name
    

    # Describe this character
    def describe(self):
        return self.description

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " cannot be distracted.")
        print(self.name + " will always come to your aid.")
        return True

    # Check frenemy status
    def check_frenemy_status(self):
        if isinstance(self,Enemy) == True:
            print("This is an enemy.")
        elif isinstance(self,Friend) == True:
            print("This is a friend.")
    
    def set_backpack(self,backpack):
        self.backpack = backpack

    def get_backpack(self):
        return self.backpack

class Enemy(Character):
    enemy_total = 0
    distracted_enemies = 0
    enemy_list = []
    distracted_list = []
    active_list = []
    
    # Create an enemy
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness = None
        Enemy.enemy_total = Enemy.enemy_total+1
        self.item = []
        self.combat_count = 0
        self.distracted = False
        Enemy.enemy_list.append(self)
        Enemy.active_list.append(self)
        self.response = None

        
    # Set the enemy's weakness
    def set_weakness(self,weakness_item):
        self.weakness = weakness_item

    # Get the enemy's weakness
    def get_weakness(self):
        return self.weakness

    # Set the object the enemy has
    def set_item(self,item):
        self.item.append(item)

    # Get the objects the enemy has
    def get_item(self):
        item_names=[]
        for item in self.item:
            item_names.append(item.name)
        return item_names
    
    # Set the enemy's response to why they are here
    def set_response(self,response_text):
        self.response = response_text
    
    # Get enemy's response to why they are here
    def get_response(self):
        return self.response   
    
    # Set as distracted
    def set_as_distracted(self):
        self.distracted = True
        Enemy.distracted_enemies = Enemy.distracted_enemies + 1
        Enemy.distracted_list.append(self)
        Enemy.active_list.remove(self)

    # Set as undistracted
    def set_as_undistracted(self):
        self.distracted = False
    
    # Check if distracted
    def get_distracted_status(self):
        return self.distracted


    # Fight with this enemy
    def fight(self,combat_item,player_backpack):
        if self.combat_count == 0:
            if combat_item.get_name() == self.weakness:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou distract",self.name,"with the",combat_item.get_name(),"\n\n\n")
                self.combat_count = self.combat_count + 1
                self.backpack.set_contents(combat_item)
                player_backpack.remove_contents(combat_item)
                self.set_as_distracted()
            else:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n"+self.name,"isn't interested in",combat_item.get_name()+".")
                self.combat_count = self.combat_count + 1
                if player_backpack.get_petal_count() > 0:
                    stolen = False
                    while stolen == False:
                        for item in player_backpack.get_contents():
                            if isinstance(item,Petal):
                                player_backpack.remove_contents(item)
                                player_backpack.subtract_petal()
                                self.backpack.set_contents(item)
                                self.backpack.add_petal()
                                stolen = True
                    print("You notice your backpack feels a little lighter.\n\n\n")
                
        else:
            if combat_item.get_name() == self.weakness:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\nYou distract",self.name,"with the",combat_item.get_name())
                self.combat_count = self.combat_count + 1
                self.backpack.set_contents(combat_item)
                player_backpack.remove_contents(combat_item)
                self.set_as_distracted()
                for item in self.backpack.get_contents():
                    if isinstance(item,Petal):
                        self.backpack.remove_contents(item)
                        self.backpack.subtract_petal()
                        player_backpack.set_contents(item)
                        player_backpack.add_petal()
                print("Your bag feels a bit heavier.\n\n\n")
            else:
                print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n"+self.name,"isn't interested in",combat_item.get_name()+".\n\n\n")
                self.combat_count = self.combat_count + 1

    def get_fight_history(self):
        return self.fight_history

    
    def ask_petal_count(self):
        if self.backpack.get_petal_count() == 0:
            print("No, {} do not have any rose petals.".format("I" if self.get_name() == "lefou" or self.get_name() == "gaston" else "we"))
        elif self.backpack.get_petal_count() == 1:
            print("Yes, {} have a rose petal.\nIf you found {} favourite item in the castle, {} might consider a trade.".format("I" if self.get_name() == "lefou" or self.get_name() == "gaston" else "we","my" if self.get_name() == "lefou" or self.get_name() == "gaston" else "our","I" if self.get_name() == "lefou" or self.get_name() == "gaston" else "we"))
        else:
            print("{} have",self.backpack.get_petal_count(),"rose petals.\nIf you found {} favourite item in the castle, {} might consider a trade.".format("I" if self.get_name() == "lefou" or self.get_name() == "gaston" else "we","my" if self.get_name() == "lefou" or self.get_name() == "gaston" else "our","I" if self.get_name() == "lefou" or self.get_name() == "gaston" else "we"))




class Friend(Character):

    friend_total = 0

    # Create a friend
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.gift = None
        self.gift_text = None
        Friend.friend_total = Friend.friend_total+1
        self.beast_info = None
        self.beast_influence = True

    # Set the friend's offering
    def set_gift(self,offering):
        self.gift = offering

    # Get the friend's offering
    def get_gift(self):
        return self.gift

    # Set the friend's individual knowledge of the Beast
    def set_beast_info(self,beast_information):
        self.beast_info = beast_information

    # Get the friend's individual knowledge of the Beast
    def get_beast_info(self):
        return self.beast_info

    # Set gift giving text
    def set_gift_text(self,gift_text):
        self.gift_text = gift_text

    # Get gift giving text
    def get_gift_text(self):
        return self.gift_text

    # Get Beast influence
    def get_beast_influence(self):
        return self.beast_influence

    # Change Beast influce
    def change_beast_influence(self):
        if self.beast_influence == True:
            self.beast_influence = False
        else:
            self.beast_influence = True

class Beast(Character):
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.heart = 0
        self.gift = None

    def increase_heart(self):
        self.heart = self.heart + 1

    def get_heart(self):
        return self.heart

    def set_gift(self,offering):
        self.gift = offering

    def get_gift(self):
        return self.gift
    


