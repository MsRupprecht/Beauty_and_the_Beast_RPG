from progress_bar import Progress_bar
from character import *


# intruders = Progress_bar("Intruders",4)
# intruders.set_progress(3)
# intruders.display_progress()

test1 = Enemy("test enemy 1","description of enemy 1")
test2 = Enemy("test enemy 2","description of enemy 2")


for character in Enemy.enemy_list:
    print(character.get_name())