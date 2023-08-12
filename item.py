class Item:
    def __init__(self,item_name):
        self.name=item_name
        self.description=None
        self.collected=None
        self.location=None

    def get_name(self):
        return self.name

    def set_description(self,item_description):
        self.description=item_description

    def get_description(self):
        return self.description

    def set_collected(self,status):
        self.collected=status

    def get_collected(self):
        return self.collected

    def set_location(self,room_name):
        self.location=room_name

    def get_room(self):
        return self.location

    def get_details(self):
        print("The",self.name)
        print(self.description)
        #print("The",self.name,"is in the",self.location)
        print("---------------")

class Petal(Item):
    petal_total=0
    def __init__(self,item_name):
        super().__init__(item_name)
        self.location=None
        self.collected=None
        self.description="A single rose petal"
        Petal.petal_total=Petal.petal_total+1
