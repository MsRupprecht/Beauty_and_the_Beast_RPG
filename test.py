from progress_bar import Progress_bar
from character import *
from backpack import *

# intruders = Progress_bar("Intruders",4)
# intruders.set_progress(3)
# intruders.display_progress()

test1 = Enemy("test enemy 1","description of enemy 1")
test2 = Enemy("test enemy 2","description of enemy 2")

test1.set_as_distracted()

print("{} will surely ruin any chance of negotiating with the Beast.  You hope something in your backpack can be used to distract them.".format("This enemy" if len(Enemy.active_list) == 1 else "These enemies"))

