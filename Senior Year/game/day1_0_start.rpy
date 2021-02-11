define n = nvl_narrator

define michelle = Character("SpiceGirl2004xX", color="#e7318d", kind=nvl)
define jason = Character("football_ladXD", color="#0000B2", kind=nvl)
define damien = Character("Lord_Damien_The_Fifth", color="#49674e", kind=nvl)
define lucy = Character("qUeEn_Of_RaNdOm", color="#bcbd51", kind=nvl)
define mc_user = Character("[username]", kind=nvl)
define mc = Character("[name]")

define michelle_Score = 0
define jason_Score = 0
define damien_Score = 0
define lucy_Score = 0

label start:

    scene bg room

    show eileen happy

    n "You have been invited to a group chat. \nPlease enter your name and a username to join."

    python:
        name = renpy.input(_("Please enter your first name."))
        name = name.strip() or __("Sam")
        username = renpy.input(_("Please enter a username."))
        username = username.strip() or __("xXuncreative_personXx")

    nvl clear

    n "[michelle] added you to group chat NORTHRIDE HIGH BLOG"
    n "[mc_user] is online"
    n "[jason] is online"
    n "[lucy] is online"
    n "[damien] is online"

    michelle "ok guys, you're all here"

    michelle "I made this group chat because of the Northride High blog"
    michelle "I know from a reliable source that we're all suspects"
    michelle "and I can't afford to get in trouble in my last year"
    michelle "so either one of u fesses up or we figure this shit out together"
    michelle "bc I cannot mess up my record bc of this"

    jason "wuuuut I didn't do anything"
    jason "y would I get involved in this shit"
    jason "idek how2set up a blog"

    michelle "I don't get it either but I have heard that Mrs. Norburry is planning to speak to all of us alone sometime this week"

    lucy "(゜ロ゜)"

    damien "Then why don't you just tell her that you didn't do it if you're innocent?"

    michelle "bc I know for a fact that this woman won't believe me"
    michelle "she almost got me kicked off the cheerleading team last year over some petty thing"

    jason "wut thing?"

    michelle "doesn't matter now"
    michelle "I just rly rly need to clear my name here guys"

    damien "Why should I care? I know that I am innocent"

    michelle "ppl already think that ur a fuckin creep Damien"
    michelle "if word gets out that you're one of the suspects everyone will just believe u did it"
    michelle "let's face it, no one in this school is crazy abt you"
    michelle "u wear guyliner ffs"

    damien "I've received many compliments for that"

    michelle "name one person who complimented you for that"

    pause 3.0

    michelle "I thought so"
    michelle "let's just get this over w"
    michelle "so we can all return to our normal lives"
    michelle "bc I'm sure we all have better things to do"
    michelle "at least I have..."

    lucy "O.O I dOn'T wAnT 2gEt iN2 tRoUbLe"

    menu:
        "Who are you?":
            jump whoAreYou
        "What blog?":
            jump whatBlog


label day2:

    "SpiceGirl2004xX is online"

    michelle "GUYS OMG HAVE YOU HEARD THE NEWS YET????"

    return
