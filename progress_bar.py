class Progress_bar():
    def __init__(self,name,total_points):
        self.name = name
        self.total = total_points
        self.progress = 0

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    
    def set_total(self,total_points):
        self.total = total_points
    
    def get_total(self):
        return self.total

    def set_progress(self,points):
        self.progress = points

    def get_progress(self):
        return self.progress
    
    def display_progress(self):
        image = ""
        if self.get_progress() > self.get_total():
            for i in range (0,self.get_total()):
                image = image + "[X]"
            print(self.get_name()+" progress: "+image)
        else: 
            for i in range (0,self.get_progress()):
                image = image + "[X]"
            for i in range (0,self.get_total()-self.get_progress()):
                image = image + "[ ]"
            print(self.get_name()+" progress: "+image)