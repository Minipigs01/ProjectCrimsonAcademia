
define e = Character("Mysterious Woman")
define n = Character ("Story")

default yes = False

label start:

    play music "VSC.mp3"

    scene bg room

    show eileen happy

    e "..."

    e "You didn't listen."

    e "You didn't listen and now..."

    e "Everyone has to suffer for what you've done"

    e "..."

label choice:
    menu: 
        e "Do you even remember what you've done...?"
    

        "Yes.":
            
            jump choice1_a
        "No.":

            jump choice1_b

label choice1_a:
    $ yes = True

    e "If you remembered then answer me this-"
        
    jump choice_2
    
label choice_2:
    
    if yes:
    
        menu: 
            e "Why are you really here in the first place?"
     
            "I am a liar":
            
                jump choice_3a
                
            "I am a murderer":
            
                jump choice_3b
                
            "I am a monster": 
            
                jump choice_3c
        
label choice1_b:     
       
    e "Allow me to give you a reminder..."

    jump intro_end 

label choice_3a:

    hide eileen happy

    e "A liar who's lies finally caught up with you hm?"

    e "Karma is a {b} bitch {/b} isn't she?"

    "For a moment, you felt your lips move to answer her..."
    
    "...but you couldn't respond to the woman on your own"

    "Almost as if your words weren't yours to speak"

    menu: 

        e "Tell me, what kind of lie did you tell?"

        "I lied about love.":
            
            jump love

        "I lied about my past.":
        
            jump past 

        "I lied about lying.":
            
            jump lying 

label love: 

    e "Ah, a liar about love."    
    
    e "Not only have you broken the hearts of others..."

    e "But you refuse to change your own corrupted heart"





label choice_3b:

    hide eileen happy

    e "A unforgivable murderer, how crude."
    
    "\"You could almost feel her invisible judgemental eyes burning-\""
    
    "\"holes into the back of your head.\""

    e "Tell me did you kill in the name of justice or in the name of fairness?"

    
label intro_end: 

    return 