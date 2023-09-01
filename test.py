from progress_bar import Progress_bar
from character import *
from backpack import *

# intruders = Progress_bar("Intruders",4)
# intruders.set_progress(3)
# intruders.display_progress()


option_end1 = True
while option_end1 == True:
    example = input("What public works project do you want to encourage him to do first?\n\
[a] School funding\n\
[b] Food shortages\n\
>> ")
    if example.lower() == "a":
        print("You have the Beast look at the school and show him how understaffed and undersupplied they are.")
        print("You explain that with proper funding, the school would be able to hire enough highly qualified and experienced teachers to properly support the students.  You remind him that the expectations and working conditions for teachers must also be reviewed if they are going to retain staff in the long term and best serve the young people in the kingdom.")
        option_end1 = False
    elif example.lower() == "b":
        print("You have the Beast look at the food bank and see how long the line is and how bare the shelves are.")
        print("You explain that with proper funding, the food bank would be able to serve every member of the community that was in need.  And even more important is proper funding and support for the kingdom's agriculture sector.  Cooperative planning amongst the different farms will help prevent the shortages of staple crops in the future.")
        option_end1 = False
    else:
        print(".\n.\n.\n.    Please try again.\n.\n.\n.\n")

