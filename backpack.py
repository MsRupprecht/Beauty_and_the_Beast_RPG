class Backpack():
    def __init__(self,item_name):
        self.name = item_name
        self.description = None
        self.contents = []
        self.contents_total=len(self.contents)
        self.petal_count = 0

    def set_description(self,bag_description):
        self.description = bag_description

    def get_description(self):
        return self.description

    def set_contents(self,item):
        self.contents.append(item)

    def get_contents(self):
        return self.contents

    def get_contents_names(self):
        item_names=[]
        for item in self.contents:
            item_names.append(item.name)
        return item_names

    def get_contents_total(self):
        return self.contents_total

    def remove_contents(self,item):
        self.contents.remove(item)

    def add_petal(self):
        self.petal_count = self.petal_count + 1

    def get_petal_count(self):
        return self.petal_count
    
 
