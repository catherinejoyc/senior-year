label day1FinalQuestion:
    menu:
        "It's not that simple":
            jump notThatSimple
        "Of course":
            jump ofCourse

label notThatSimple:

    mc_user "It's not that simple."

    lucy "DD:"

    michelle "cmon [mc] you're pretty much the only hope we got"

    damien "Hate to say it but I think she's right"

    jason "yea dude I'm sure u can do it"
    jason "I heard binary code only has like 2 numbers"
    jason "so like how hard can hacking b"

    michelle "ignore him"
    michelle "but we rly need you here"

    menu:
        "Alright...":
            jump notThatSimple2

label notThatSimple2:

    jason "fuck yea dude dats the spirit"

    lucy "tHx <333333333"

    damien "Thank you for agreeing to help [mc]"

    michelle "thank you sm!!!"
    michelle "I promise I will help you in any way I can."

    jump day1End


label ofCourse:
    $ lucy_Score = lucy_Score + 1
    $ jason_Score = jason_Score + 1
    $ michelle_Score = michelle_Score + 1
    $ damien_Score = damien_Score + 1

    mc_user "Of course, we're all in this together."

    jason "awh yea man High School Musical reference"
    jason "uh I mean"
    jason "that's sick dude"

    lucy "aWeSoMe SaUcE ^^"

    damien "Thank you [mc], that's really chivalric of you."

    michelle "thank you so much!!! I promise I will notify you as soon as I hear any new rumors."

    jump day1End

label day1End:

    michelle "this is the purpose of this chatroom now, we will all support [mc] in this mission and write in here when we hear any new rumors about this damn blog."

    damien "Or we could just talk face to face."

    michelle "and risk getting seen with you? no thx"
    michelle "anyways I gtg, ttyl losers xoxo"

    n "[michelle] logged off"

    damien "I am already sick of her."
    damien "Goodnight to all of you."

    n "[damien] logged off"

    jason "lol these 2 r so funny"
    jason "anyways I shouldget goin as well, I got training2morrow"
    jason "see ya"
    jason "JASON OUT"

    n "[jason] logged off"

    lucy "tHx 4Ur HeLp [mc] c:"

    n "[lucy] logged off"
