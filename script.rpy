
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
            
                jump choice_ending
                
            "I am a murderer":
            
                jump choice_ending
                
            "I am a monster": 
            
                jump choice_ending
        
label choice1_b:     
       
    e "Allow me to give you a reminder..."

    jump choice_ending

label choice_ending:

    hide eileen happy

    "{b}And then everything went dark{/b}."

    return