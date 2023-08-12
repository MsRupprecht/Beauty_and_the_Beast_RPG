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
        print("\n\
          :@-@:                                                          :@-@:            \n\
         :@- -@:                                                        :@- -@:            \n\
        .@-   -@.                                                      .@-   -@.           \n\
       .@-     -@.                                                    .@-     -@.          \n\
      .@-       -@.                                                  .@-       -@.         \n\
     .@-         -@.                                                .@-         -@.        \n\
 #***@%. =#***#=  %@***#.                                      :#***@#  +****#- .%%***#   \n\
 @.  .@-:##   +#::@.  .@:                                      -@   -@::%=   #*:=@   :@   \n\
 @.   ====:   :====   .@:                                      -@   .====:   -====   :@   \n\
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
   =#               #*      @:@@@@=+%##:@@@==@@@.%#%==@@@%-%      **               %=     \n\
   =#               #*      @:@@@@%====%@@@==@@@#====@@@@%-%      **               %=     \n\
   =#               #*      @:@@@@@@@@@@@@@==@@@@@@@@@@@@%-%      **               %=     \n\
   =#               #*      @:@@@@@@@@@@@@@-=@@@@@@@@@@@@%-%      **               %=     \n\
   =#............  .#*     .@-************+--************+=%    ..#*              .%=     \n\
   :+++++++++++++==+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:     \n")
        print("Once upon a time, in a far away land, a young prince lived \
in a shining castle. \nAlthough he had nearly everything his heart desired, \
the prince was selfish and unkind. \nBut then, one winter's night, \
an old beggar woman came to the castle and offered him a single rose in return \
for shelter from the bitter cold. \nRepulsed by her haggard appearance, the \
prince sneered at the gift and turned the old woman away. \nBut she warned him \
not to be deceived by appearances, for beauty is found within. \nAnd when he \
dismissed her again, the old woman's ugliness melted away to reveal a beautiful \
enchantress. \nThe prince tried to apologize, but it was too late, for she had \
seen that there was no love in his heart. \nAs punishment, she transformed \
him into a hideous beast and placed a powerful spell on the castle, and all \
who lived there. \nThe rose she had offered was truly an enchanted rose, \
which would bloom and wilt to reflect the openness of his heart. \nIf he could \
learn to empathy for others, and freely offer his service to someone in need, \
then the spell would be broken. \nAs the years passed, he fell into despair \
and lost all hope. \nFor who would ever rely on beast?")
        print("\n...10 years later...\n")
        print("An angry mob is ready to kill the Beast.\n\
Although the Beast has certainly let down his community, you realise that he \
was an 11 year old orphan when he was cursed. \nPerhaps this enchantress \
was a bit disproportionate in her role as judge, jury, and executioner. \n\
You hope to meet with the Beast, help him beat the curse, and get the monarchy \
doing some positive work for the surrounding villages.")

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
    
    


    
