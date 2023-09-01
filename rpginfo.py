import time

class RPGInfo():
    author = "Anonymous"
    
    # Initialising game information
    def __init__(self,game_title):
        self.title=game_title

    # Welcome message
    def welcome(self):
        print("Welcome to",self.title)

    # Introduction
    def intro(self):
        #input("Press any key to begin the game.\n")
        print("\n\
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n\n\
  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * \n\n\
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  \n\n\
  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * \n\n\
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
        print("Once upon a time, in a far away land, a young prince lived \
in a shining castle. \nAlthough he had nearly everything his heart desired, \
the prince was selfish and unkind.\n\
*  *  *  *")
        time.sleep(1.8)
        print("One winter's night, an old beggar woman came to the castle.\n\
She offered him a single rose in return for shelter from the bitter cold. \n\
Repulsed by her haggard appearance, the prince sneered at the gift and turned the old woman away. \n\
She warned him not to be deceived by appearances, for beauty is found within.\n\
*  *  *  *")
        time.sleep(2.8)
        print("When he dismissed her again, the old woman's ugliness melted away to reveal a beautiful enchantress. \n\
The prince tried to apologize, but it was too late, for she had seen that there was no love in his heart. \n\
As punishment, she transformed the prince into a hideous beast and placed a powerful spell on the castle, \n\
and all who lived there.\n\
*  *  *  *")
        time.sleep(2.8)
        print("The rose she had offered was truly an enchanted rose, which would bloom and wilt to reflect the openness of his heart. \n\
If he could learn to empathy for others, and freely offer his service to someone in need, \n\
then the spell would be broken. \nAs the years passed, he fell into despair \
and lost all hope. \nFor who would ever rely on beast?\n\
*  *  *  *")
        input("Press any key to continue\n\
>> ")
        print("\
*\n\
*\n\
*")
        print("\n...10 years later...\n")
        print("\
*\n\
*\n\
*")
        print("Discontent in the kingdom has grown over the past decade.\n\
The story of Prince Adam turning into a viscious Beast has spread far and wide.\n\
Distrust is at an all time high, and the villages are turning into an angry mob.\n\
You have heard rumours about groups gathering to storm the castle and kill the Beast.\n\
*  *  *  *")
        time.sleep(2.8)
        print("Although the Beast has certainly let down his community, you realise there is more to the story. \n\
He was an 11 year old orphan when he was cursed. \n\
Yes, he was in a position of power, and perhaps he should have known better and been kinder.\n\
But an 11 year old is hardly in a position to be running a castle and managing the affairs of the state.\n\
Even so, this enchantress's actions were surely disproportionate.\n\
No one deserves this curse - least of all the working inhabitants of the castle who had nothing to do with the incident\n\
*  *  *  *")
        time.sleep(2.8)
        print("You hope to meet with the Beast and explain what is happening in the kingdom.\n\
You have studied the lore and are ready to help him beat the curse.\n\
Surely that will calm the furore in the village, and there will be a chance for some positive change.")


    def castle_image(self):
        print("\n\
          :@-@:                                                          :@-@:            \n\
         :@- -@:                                                        :@- -@:            \n\
        .@-   -@.                                                      .@-   -@.           \n\
       .@-     -@.                                                    .@-     -@.          \n\
      .@-       -@.                                                  .@-       -@.         \n\
     .@-         -@.                                                .@-         -@.        \n\
 #***@%. =#***#=  %@***#.                                      :#***@#  +****#- .%%***#   \n\
 @.  .@-:##   +#::@.  .@:                                      -@   -@::%=   #*:=@   :@   \n\
 @+++++++++++++++++++++@:                                      :@++++++++++++++++++++*@   \n\
   *%+++++++++++++++%#                                           .##+++++++++++++++@*     \n\
   =#               #*                                            **               %=     \n\
   =#    :#@@@%:    #*    *%+++++*@    -@++++++@:    @*+++++%+    **    -%@@@#.    %=     \n\
   =#    #@@@@@#    #*....#*     -@....=@      @-...:@:     #*....#*    %@@@@@*    %=     \n\
   =#    #@@@@@#    ##=====:     .=======      =======.     -=====%*    %@@@@@*    %=     \n\
   =#   #%%%%%%%%.  #*                                            **  .%%%%%%%%*   %=     \n\
   =#               #*                :=+*****++=:                **               %=     ")
        print("\
   =#               #*            .+#*++**#--#**++*#+.            **               %=     \n\
   =#               #*  -%+     -#*+*@@@@@@==@@@@@@*+*#:     +%-  **               %=     \n\
   =#               #* *#.+%  .#*=%@@@@@@@@==@@@@@@@@%=#*. .%=.#+ **               %=     \n\
   =#               #*.@- .@-:@=#@@@@@@@@@@==@@@@@@@@@@*=%.=@  -@ **               %=     \n\
   =#               #* :@@@+.@-#@@@@@@@@@@@==@@@@@@@@@@@#=% +@@@: **               %=     \n\
   =#               #*   @. %-@@@@@@#*@@@@@==@@@@@+#@@@@@%=# :#   **               %=     \n\
   =#               #*   *  @:@@@@%=:.=%@@@==@@@#=.:=@@@@%-% .+   **               %=     \n\
   =#               #*      @:@@@@@@@@@@@@@==@@@@@@@@@@@@%-%      **               %=     \n\
   =#               #*      @:@@@@@@@@@@@@@-=@@@@@@@@@@@@%-%      **               %=     \n\
   :+++++++++++++==+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:     \n")

    # Game creation information
    # Structure of these assumes others authors will use my classes
    # to generate their own games.  This is just shoehorning in making
    # a class method, so let's just roll with it.

    @staticmethod
    def info():
        print("Made using the STEM Learning OOP RPG tutorial.")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by", RPGInfo.author)
    
    


    
