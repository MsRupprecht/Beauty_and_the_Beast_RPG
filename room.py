class Room:

    number_of_rooms=0
    
    def __init__(self,room_name):
        self.name=room_name
        self.description=None
        self.lights_on=None
        self.tidy=None
        self.linked_rooms={}
        self.character=None
        self.linked_items=[]

        Room.number_of_rooms=Room.number_of_rooms+1


    def set_description(self,room_description):
        self.description = room_description

    def get_description(self):
        return self.description


    def set_name(self,room_name):
        self.name=room_name

    def get_name(self):
        return self.name


    def describe(self):
        return self.description


    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction]=room_to_link

    def get_linked_rooms(self):
        return self.linked_rooms

    def print_linked_rooms(self):
        for direction in self.linked_rooms:
            room=self.linked_rooms[direction]
            print("The",room.get_name(),"is",direction)
        


    def link_item(self,item):
        self.linked_items.append(item)

    def get_items(self):
        return self.linked_items

    def get_item_names(self):
        list_of_names=[]
        for item in self.linked_items:
            list_of_names.append(item.name)
        return list_of_names


    def set_character(self,new_character):
        self.character=new_character

    def get_character(self):
        return self.character


    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that direction.")
            return self


    def get_full_details(self):
        print("-----")
        print("Current room: The",self.name)
        print("Description:",self.describe())
        if len(self.linked_items)!=0:
            print("Inside the room, you can see:",self.get_items())
        print("-----")
        print("Nearby rooms:")
        for direction in self.linked_rooms:
            room=self.linked_rooms[direction]
            print("The",room.get_name(),"is",direction)
        print("-----")
        inhabitant=self.get_character()
        if inhabitant is not None:
            print(inhabitant.name,"is here!")
            print("Biography:",inhabitant.describe())
            #inhabitant.describe()
        else:
            print("There are no characters in this room.")
        print("---------------")



    def print_basic_room_description(self):
        print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\n\n\n")
        print("Current room: The",self.name)
        print("Description:",self.description,"\n\n\n")
