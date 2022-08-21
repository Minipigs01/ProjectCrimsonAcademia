## Starters

define e = Character("Mysterious Woman")
define n = Character ("Story")

image Juno = ("juno_1.png")

image BG1 = ("bg1.png")

image Akuma = "akuma.png"

## Introduction Defaults

default yes = False

default liar = False 

default murderer = False

default monster = False

default love = False

default past = False

default failed = False

default won = False

default lying = False

default justice = False

default fairness = False

default yes2 = False

default no2 = False

##Start

label start:

    play music "VSC.ogg"

    scene BG1 

    show Juno

    e "..."

    play sound "Static.ogg"

    e "You didn't listen."

    play sound "Static.ogg"

    e "You didn't listen and now..."

    play sound "Static.ogg"

    e "Everyone has to suffer for what you've done" 

    play sound "Static.ogg"

    e "..."

    play sound "Static.ogg"

label choice:

   

    play sound "Static.ogg"

    hide Akuma 

    show Juno

    menu: 
        e "Do you even remember what you've done...?"
    
        "Yes.":
            
            play sound "Static.ogg"

            jump choice1_a
        "No.":

            play sound "Static.ogg"

            jump choice1_b

label choice1_a:
    $ yes = True

    e "If you remembered then answer me this-"
        
    jump choice_2
    
label choice_2:

    play sound "Static.ogg"
    
    if yes:
    
        menu: 
            e "Why are you really here in the first place?"
     
            "I am a liar":

                play sound "Static.ogg"
            
                jump choice_3a
                
            "I am a murderer":

                play sound "Static.ogg"

                $ murderer = True
            
                jump choice_3b
                
            "I am a monster": 

                play sound "Static.ogg"

                $ monster = True 
            
                jump choice_3c
        
label choice1_b:     

    play sound "Static.ogg"
       
    e "Allow me to give you a reminder..."

    jump intro_end 

label choice_3a:

    $ liar = True

    hide Phill

    e "A liar who's lies finally caught up with you hm?"

    play sound "Static.ogg"

    e "Karma is a {b} bitch {/b} isn't she?"

    play sound "Static.ogg"

    "For a moment, you felt your lips move to answer her..."

    play sound "Static.ogg"
    
    "...but you couldn't respond to the woman on your own"

    play sound "Static.ogg"

    "Almost as if your words weren't yours to speak"

    play sound "Static.ogg"

    menu: 

        e "Tell me, what kind of lie did you tell?"

        "I lied about love.":

            play sound "Static.ogg"
            
            jump love

        "I lied about my past.":

            play sound "Static.ogg"
        
            jump past 

        "I lied about lying.":

            play sound "Static.ogg"
            
            jump lying 

label love: 

    play sound "Static.ogg"

    $ love = True 

    e "Ah, a liar about love."    

    play sound "Static.ogg"
    
    e "Not only have you broken the hearts of others..."

    play sound "Static.ogg"

    e "But you refuse to change your own corrupted heart"

    play sound "Static.ogg"

    menu: 

        e "Tell me, did you fail in this endevor?"
        
        "Yes":

            play sound "Static.ogg"
            
            jump failed 

        "No":

            play sound "Static.ogg"

            jump won


label failed: 

    $ failed = True 

    e "How ironic..."

    play sound "Static.ogg"

    e "Although Karma always finds it's target."

    play sound "Static.ogg"

    e "I think we're done here..."

    play sound "Static.ogg"

    jump intro_end

label won: 

    $ won = True

    e "Color me impressed..."

    e "Above all else, not even your own pride or honor could steer you away from your goal."

    e "Still, you have skeletons in your closet"

    e "{b} M A N Y S K E L E T O N S {/b}"

    e "..."

    e "I think we're done here..."

    jump intro_end 



label choice_3b:

    hide Juno

    e "A unforgivable murderer, how crude."

    play sound "Static.ogg"
    
    "\"You could almost feel her invisible judgemental eyes burning-\""

    play sound "Static.ogg"
    
    "\"holes into the back of your head.\""

    play sound "Static.ogg"

    menu:

        e "Tell me did you kill in the name of justice or in the name of fairness?"

        "I killed in the name of justice":

            play sound "Static.ogg"

            jump justice

        "I killed in the name of fairness":

            play sound "Static.ogg"

            $ fairness = True

            jump fairness

label fairness:

    e "Is it truly fair to take ones life in the name of equality"

    play sound "Static.ogg"

    e "An eye for an eye and the world goes blind"

    play sound "Static.ogg"

    e ""
    
# All introduction ending segments
label intro_end: 

    if liar and love and failed == True:
        
        e "Hm..."

        play sound "Static.ogg"
        
        e "I think I know what you are..."

        play sound "Static.ogg"

        hide Juno

        show Akuma

        e "You are a {b} Hopeless Romantic {/b}"

        play sound "Static.ogg"

        menu: 
            
            e "Is this correct?"

            "Yes":

                play sound "Static.ogg"

                $ hopelessromantic = True

                jump ending

            "No":

                play sound "Static.ogg"

                jump choice
    elif liar and love and won == True:

            e "Hm..."

            e "I think I know what you are..."

            e "You are a {b} Survivor {/b}"

            menu: 

                e "Is this correct?"

                "Yes":

                    $ survivor = True

                    jump ending

                "No":

                    jump choice
    elif liar and past and running == True:

                e "Hm..."

                e "I think I know what you are..."

                e "You are an {b} Unforgivable Theif {/b}"

                menu: 

                    e "Is this correct?"

            
                    "Yes":

                        $   unforgivabletheif = True

                        jump ending

                    "No":

                        jump choice


        

label ending:

    return 