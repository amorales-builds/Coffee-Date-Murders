# The script of the game goes in this file.

### animated images

image testbox:
    "gui/white_textbox2.png"
    align (0.5, -1.0)
    pause 0.2
    "gui/white_textbox.png"
    align (0.5, -1.0)
    pause 0.2
    repeat

image menu_animated_idle:
    "gui/menu_line1_idle.png"
    pause 0.8
    "gui/menu_line2_idle.png"
    pause 0.8
    repeat

image menu_animated_hovered:
    "gui/menu_line1_hover.png"
    pause 0.4
    "gui/menu_line2_hover.png"
    pause 0.2
    "gui/menu_line3_hover.png"
    pause 0.4
    "gui/menu_line2_hover.png"
    pause 0.2
    repeat

image bb_neutral:
    "images/badboy1.png"
    pause 1.0
    "images/badboy2.png"
    pause 1.0
    "images/badboy3.png"
    pause 1.0
    "images/badboy2.png"
    pause 1.0
    "images/badboy3.png"
    pause 1.0
    "images/badboy2.png"
    pause 0.5
    "images/badboy_blink.png"
    pause 0.1
    "images/badboy2.png"
    pause 0.4
    repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.
    
define n = Character(None) 
define u = Character("???")
define mc = Character("[name]")
define smc = Character(image = "mc", what_italic = True, what_kerning = 3) 
define smcs = Character(image = "mc", window_background = "testbox")
define bb = Character("Bad Boy")
define sbb = Character("Bad Boy", image = "bb")
define d = Character("Doctor")
define sd = Character("Doctor", image = "d")
define gg = Character("Gentle Giant")
define sgg= Character("Gentle Giant", image = "gg")
define cc = Character("Cute Cook")
define scc = Character("Cute Cook", image = "cc")
define pg = Character("Pretty Girl")
define spg = Character("Pretty Girl", image = "pg")
define bl = Character("Barista Lady")
define sbl = Character("Barista Lady", image = "bl")
define bm1 = Character("Braids")
define sbm1 = Character("Braids", image = "bm1")
define bm2 = Character("Albino")
define sbm2 = Character("Albino", image = "bm2")
define lbguy = Character("Love Bird Guy")
define slbguy = Character("Love Bird Guy", image = "lbguy")
define lbgirl = Character("Love Bird Girl")
define slbgirl = Character("Love Bird Girl", image = "lbgirl")
define e = Character("Editor", window_background = "testbox")

### customs

define flash = Fade(0.2, 0.0, 0.8, color='#fff')

### transforms

transform center:
    xalign 0.5
    yalign 1.0

transform newcenter:
    zoom 2.0
    xalign 0.5

transform slightright:
    xalign 0.75
    yalign 1.0

transform slightleft:
    xalign 0.25
    yalign 1.0

transform bbcenter:
    zoom 1.1
    xpos 0.5
    xanchor 0.5

transform completeleft:
    xalign 0.0
    yalign 1.0

transform lurking:
    xalign 0.5
    yalign 3.0

transform bigcenter:
    xpos 0.5
    xanchor 0.5
    ypos 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5

transform tremblecenter:
    xalign 0.5 yalign 1.0
    linear 0.05 xalign 0.497
    linear 0.05 xalign 0.5
    repeat 

transform swaycenter:
    xalign 0.5 yalign 1.0
    linear 0.09 xalign 0.497
    linear 0.09 xalign 0.5
    repeat 

transform tremble:
    xalign 0.75 yalign 1.0
    linear 0.05 xalign 0.745
    linear 0.05 xalign 0.75
    repeat 3

transform glitch:
    xalign 0.75 yalign 1.0
    linear 0.05 xalign 0.745
    linear 0.05 xalign 0.75
    repeat

transform shake:
    xalign 0.75 yalign 1.0
    linear 0.08 yalign 1.05
    linear 0.08 yalign 1.0
    repeat 

transform breathecenter:
    xalign 0.5 yalign 1.0
    linear 0.3 yalign 1.05
    linear 0.3 yalign 1.0
    repeat 

transform pantstop:
    xalign 0.75 yalign 1.0
    linear 0.08 yalign 1.05
    linear 0.08 yalign 1.0
    repeat 3

transform pant:
    xalign 0.75 yalign 1.0
    pause 0.7
    linear 0.08 yalign 1.07
    linear 0.08 yalign 0.95
    linear 0.08 yalign 1.0
    pause 1.1
    repeat 

transform quip:
    xalign 0.5 yalign 1.1
    linear 0.1 yalign 0.92
    linear 0.08 yalign 1.17
    linear 0.1 yalign 1.0
    repeat 1

transform textbox:
    xalign 0.0
    yalign 3.0

transform sitting:
    xpos 0.2
    ypos 0.0


### Scenes
     
screen middle1:
    if pg_name == True:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_middle")
        imagebutton:
            #xanchor 1.1
            xanchor -1.4
            #yanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_right_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("deadbody_3")
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.51
            ypos 0.2
            auto "gui/testbutton_%s.png"
            action Jump("jukebox")
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.1
            ypos 0.32
            auto "gui/testbutton_%s.png"
            action Jump("investigation_hallway")
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.08
            ypos 0.67
            auto "gui/testbutton_%s.png"
            action Jump("investigation_bar")

    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("middle1")

screen middle2:
    if pg_name:
        imagebutton:
            #xanchor -0.1
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), NullAction()

        imagebutton:
            #xanchor 1.1
            xanchor 2.1
            #yanchor 0.5
            yanchor 1.3
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_left_%s.png"
            action Play("sound", "audio/boing.wav"), NullAction()

    else:
        imagebutton:
            #xanchor -0.1
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("middle2")

        imagebutton:
            #xanchor 1.1
            xanchor 2.1
            #yanchor 0.5
            yanchor 1.3
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_left_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("hallway_intro")

screen hallway:
    if pg_name:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_middle")

        imagebutton:
            xanchor 1.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_left_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_kitchen")

        imagebutton:
            xanchor 0.5
            yanchor 1.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_restroom")
        
        imagebutton:
            xanchor -0.5
            yanchor 0.5
            xpos 0.73
            ypos 0.44
            auto "gui/testbutton_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_backdoor")
    

    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("middle2")

        imagebutton:
            xanchor 1.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_left_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("kitchen")

        imagebutton:
            xanchor 0.5
            yanchor 1.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("restroom")

    #if freedom_flag == True:
    #else: 
    #    pass

screen hallway_intro_after:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_down_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("middle2")

    imagebutton:
        xanchor 1.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_up_left_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("kitchen")

    imagebutton:
        xanchor 0.5
        yanchor 1.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_up_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("restroom")

    if freedom_flag == True:
        imagebutton:
            xanchor -0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_right_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("trash")
    else:
        pass

screen kitchen:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_down_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("hallway_intro")

screen restroom:
    if interrogation_start and not poison_bottle:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_hallway")
        imagebutton:
            xanchor 1.0
            yanchor 1.0
            xpos 1.0
            ypos 0.85
            auto "gui/testbutton_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("poison_bottle")
    if interrogation_start and poison_bottle:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_hallway")
    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("hallway_intro")

screen exit:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_up_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("exit")

screen entrance:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_down_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("entrance")

screen parkinglot_intro:
    imagebutton:
        xpos 0.29
        ypos 0.09
        auto "images/outside_doorparkinglot_%s.png"
        action Play("sound", "audio/bell.wav"), Jump("entrance")

    #imagebutton:
    #    xanchor 0.5
    #    yanchor 0.5
    #    xpos 0.5
    #    ypos 0.85
    #    auto "gui/arrow_down_%s.png"
    #    action Play("sound", "audio/boing.wav"), Jump("parked")
   
    imagebutton:
        xanchor 1.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_up_left_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("diner_back")    

    imagebutton:
        xanchor -0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_right_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("cars")

screen cars:
    imagebutton:
        xanchor 0.5
        yanchor 1.5
        xpos 0.5
        ypos 1.05
        auto "gui/arrow_up_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("trash")
    imagebutton:
        xanchor 1.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_left_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("outside_intro")  

screen trash:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_down_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("cars")
    if freedom_flag == True:
        imagebutton:
            xanchor 1.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_up_left_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("hallway_intro")
    else:
        pass

screen diner_back:
    imagebutton:
        xpos 0.279
        ypos 0.0
        auto "images/outside_door_%s.png"
        action Play("sound", "audio/bell.wav"), Jump("entrance")
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_down_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("outside_intro")  

screen leave_doctor:
    imagebutton:
        xanchor -0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_right_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("idcards_take")

screen leave_doctor_2:
    imagebutton:
        xanchor -0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_right_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("identify_body_2")

screen leave_doctor_3:
    imagebutton:
        xanchor -0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_right_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("investigation_starts")

screen go_doctor:
    imagebutton:
        xanchor -0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_right_%s.png"
        action Play("sound", "audio/boing.wav"), Jump("identify_body")

screen bar_interrogation:
    hbox:
        xalign 0.5
        yalign 0.4
        spacing 250
        imagebutton:
            #xalign 0.1
            idle "cutecook.png"
            action Jump ("interrogation_cc")
        imagebutton:
            #xalign -0.05
            idle "baristalady.png"
            action Jump ("interrogation_bl")
    imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Hide ("bar_interrogation"), Jump("investigation_starts")

screen jukebox:
    if dagger == False:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.7
            auto "gui/testbutton_%s.png"
            #action Show("jukebox_closeup")
            action Jump ("jukebox_closeup")
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.8
            auto "gui/testbutton_%s.png"
            action [SetVariable("dagger", True), Jump ("jukebox_dagger")]
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_starts")

    else:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.7
            ypos 0.7
            auto "gui/testbutton_%s.png"
            action Jump ("jukebox_closeup")
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.85
            auto "gui/arrow_down_%s.png"
            action Play("sound", "audio/boing.wav"), Jump("investigation_starts")

screen jukebox_closeup:
    modal True
    dismiss action [Hide ("jukebox_closeup"), Jump("jukebox")]
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 40
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                spacing 40
                textbutton "Morning Stroll":
                    action [Play ("music", "audio/morning_stroll.wav")]
                textbutton "Resting Suspicion":
                    action [Play ("music", "audio/restingsuspicion.wav")]
                textbutton "Main Tune":
                    action [Play ("music", "audio/maintune_happy2.wav")]

        frame:
            textbutton "stop":
                action [Stop("music")]            

screen dagger_closeup:
    frame:
        xalign 0.5
        yalign 0.5
        xminimum 400
        yminimum 400
        image "gui/testbutton_hover.png":
            xalign 0.5
            yalign 0.5

screen bottle_closeup:
    frame:
        xalign 0.5
        yalign 0.5
        xminimum 400
        yminimum 400
        image "gui/testbutton_hover.png":
            xalign 0.5
            yalign 0.5

### Ending Screens

screen rude_ending:
    frame:
        xalign 0.5
        yalign 0.5
        textbutton "Rude Ending Achieved!":
            text_size 80
            action Hide("rude_ending"), Show("rude_ending_why")

screen rude_ending_why:
    frame:
        xalign 0.5
        yalign 0.5
        textbutton "But why would you want this ending...?":
            text_size 35
            action Return()

### Tools

#screen mask:
    #image "images/frame2.png"
    #image "images/triangles.png"

screen qmenu:
    modal True
    #image "images/triangles.png"
    image "menus/quick_menu08.png":
        xalign 0.5
        yalign 0.5
    imagebutton:
        auto "buttons/menu_close_%s.png"
        hovered [Play("sound", "audio/click2.wav")]
        #xpos 1671
        #ypos 112
        #xpos 1695
        #ypos 126
        #yalign 0.54
        xpos 1675
        ypos 144
        action Hide("game_menu"), Hide("qmenu"), Return()
        #Play("sound", "audio/click.wav"),
    vbox:
            xalign 0.2
            yalign 0.55
            spacing 40
            #textbutton _("Back") action Rollback()
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("☼    Main Menu") action Play("sound", "audio/lasershot.wav"), MainMenu() 
            textbutton _("☼    Save") action Play("sound", "audio/lasershot.wav"), ShowMenu('save') 
            #textbutton _("☼    Q.Save") action QuickSave()
            #textbutton _("☼    Q.Load") action QuickLoad()
            textbutton _("☼    Load") action Play("sound", "audio/lasershot.wav"), ShowMenu("load") 
            textbutton _("☼    Back") action Play("sound", "audio/lasershot.wav"), Rollback() 
    #vbox:
            #hovered [Play("sound", "audio/bell2.wav")]
            #xalign 0.65
            #yalign 0.5
            #spacing 100
            textbutton _("☼    Preferences") action Play("sound", "audio/lasershot.wav"), ShowMenu('preferences') 
            textbutton _("☼    Log") action Play("sound", "audio/lasershot.wav"), ShowMenu ('history') 
            textbutton _("☼    Quit") action Play("sound", "audio/lasershot.wav"), Quit(confirm=not main_menu) 
    #image "images/triangles.png"
    #imagebutton:
    #    xanchor 0.0
    #    yanchor 0.0
    #    xoffset 20
        #auto "buttons/menu_icon_%s.png"
        #idle "buttons/menu_icon_idle.png"
        #hover "buttons/menu_icon_hover.png"
    #    auto "buttons/menu_icon_selected_%s.png"
    #    action Return()
        #Play("sound", "audio/pulse.wav"),

screen qmenu_button:
    #frame:
    #    xanchor 0.0
    #    yanchor 0.0
    #    xoffset 35
    #    yoffset 15
    #    ypadding -3
        #xpadding -1
    #    vbox:
    #        textbutton "Menu":
    #            text_size 30
    #            action Show("qmenu"), Hide("qmenu_button")
    #vbox:
    #    #xalign 0.5
    #    #yalign 0.5
    #    spacing 2
    #    xanchor 0.0
    #    yanchor 0.0
    #    xoffset 35
    #    yoffset 15
    #    frame:
    #        vbox:    
    #            textbutton "":
    #                xminimum 80
    #                ypadding -11
    #                text_size 25
    #                action Show("qmenu"), Hide("qmenu_button")    
    #    frame:
    #        vbox:
    #            textbutton "Menu":
    #                ypadding -5
    #                text_size 25
    #                action Show("qmenu"), Hide("qmenu_button")
    #    frame:
    #        vbox:
    #            textbutton "":
    #                xminimum 80
    #                ypadding -11
    #                text_size 25
    #                action Show("qmenu"), Hide("qmenu_button")    
    #vbox:
    #        textbutton "♦♦♦":
    #            xanchor 0.0
    #            yanchor 0.0
    #            xoffset 35
    #            yoffset 15
                #text_size 30
    #            action Show("qmenu"), Hide("qmenu_button")

    imagebutton:
        #xanchor 0.0
        #yanchor 0.0
        #xoffset 20
        #auto "buttons/menu_icon_%s.png"
        xalign 0.5
        yalign 0.98
        idle "menu_animated_idle"
        hover "menu_animated_hovered"
        #hovered [Play("sound", "audio/softclick.wav")]
        #hovered [Play("sound", "audio/pulse.wav")]
        #hovered [Play("sound", "audio/click2.wav")]
        #hovered [Play("sound", "audio/notebook_sounds_thump.wav")]
        #idle "buttons/menu_icon_idle.png"
        #hover "buttons/menu_icon_hover.png"
        #selected_idle "buttons/menu_icon_selected_idle.png"
        #selected_hover "buttons/menu_icon_selected_hover.png"
        action Play("sound", "audio/bell.wav"), ShowMenu("qmenu")
        #, Hide("qmenu_button")

screen test:
    imagebutton:
        xanchor 1.0
        yanchor 0.0
        xpos 1.0
        ypos -0.15
        #ypos 0.4
        idle "gui/testbutton_idle.png"
        hover "gui/testbutton_hover.png"
        #action Jump("end")
        action Jump("end")

        #hovered Show("displayTextScreen", displayText = "hey")
        #unhovered Hide("displayTextScreen")

screen notebook_object:
    imagebutton: 
        auto "buttons/notebook_button_%s.png" 
        #idle "buttons/notebook_button_idle.png" 
        #hover "buttons/notebook_button_hover.png", [Play ("sound", "audio/notebook_sounds_page.wav")]
        #hovered [Play("sound", "audio/notebook_sounds_thump.wav")]
        #selected [Play ("sound", "audio/notebook_sounds_page.wav")]
        xalign 0.9
        yalign 0.6
        #ypadding -3
        xoffset -35
        #yoffset 10
        action Hide("notebook_object", transition=Dissolve(0.5)), Play ("sound", "audio/lasershot.wav"), Jump ("name") 
        #Show("notebook_intro", transition=Dissolve(0.5))

screen notebook_intro:
    vbox:
        spacing 30
        xalign 0.5
        yalign 0.5        
        text "Name:"
        input default "Max":
            pixel_width (300)
            value VariableInputValue ("name")
            #action Show("notebook_button", transition=Dissolve(0.5))
        frame:
            yoffset 50
            xalign 0.5
            yalign 0.5
            textbutton "ok":
                action SetVariable("quick_menu", True), Play ("sound", "audio/notebook_sounds_thump.wav"), Hide("notebook_intro"), Jump ("named") 
    hbox:
            xpos 0.9
            xoffset -5
            yoffset 20
            textbutton "close":
                text_size 40
                action SetVariable("quick_menu", True), Play ("sound", "audio/notebook_sounds_thump.wav"), Hide("notebook_intro"), Jump ("named")

screen notebook_people_intro:
    modal True
    frame:
        #vbox:
        #    #xoffset 200
        #    xoffset 60
        #    yoffset 150
        #    spacing 25
        #    textbutton "Me":
        #        action NullAction()
        fixed:
            vbox:
                xalign 0.48
                yalign 0.07
                text "[name]"
            image "images/player.png":
                yalign 0.5
                xpos 0.55
                xzoom 1.6
                yzoom 1.6
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 20
                text "Info:":
                    xoffset -50
                text "In my 20 somethings."
                text "My therapist said this was a good idea."
                text "Currently hungry"
        hbox:
            xpos 0.9
            xoffset -5
            yoffset 20
            textbutton "return":
                text_size 40
                action [Hide ("notebook_people_intro"), Play ("sound", "audio/lasershot.wav")]
                #Show("notebook_button", transition=Dissolve(1.5))

screen notebook_open:

    dismiss action [Hide("notebook_open"), Show("notebook_button")], Return()

    imagebutton: 
        xalign 0.17
        yalign 0.93
        idle "images/mbttn.png" 
        action [Hide("notebook_open"), Show("notebook_button"), ShowMenu("qmenu")], Play("sound", "audio/bell.wav")
    
    imagebutton: 
        xalign 0.35
        yalign 0.9
        idle "images/nbttn.png" 
        action [Hide("notebook_open"), Show("notebook_people")], Play ("sound", "audio/notebook_sounds_button.wav")

    imagebutton: 
        xalign 0.635
        yalign 0.89
        idle "images/bbttn.png" 
        action [Hide("notebook_open"), Show("notebook_objects")], Play ("sound", "audio/notebook_sounds_button.wav")
    
    imagebutton: 
        xalign 0.83
        yalign 0.93
        idle "images/babttn.png" 
        action [Hide("notebook_open"), Show("notebook_info")], Play ("sound", "audio/notebook_sounds_button.wav")

    image "images/nb.png":
        xalign 0.5
        yalign 1.0

screen notebook_button:

    imagebutton: 
        auto "buttons/notebook_button_%s.png" 
        #idle "buttons/notebook_button_idle.png" 
        #hover "buttons/notebook_button_hover.png", [Play ("sound", "audio/notebook_sounds_page.wav")]
        hovered [Play("sound", "audio/notebook_sounds_thump.wav")]
        #selected [Play ("sound", "audio/notebook_sounds_page.wav")]
        xalign 1.0
        ypadding -3
        xoffset -35
        yoffset 10
        #action SetVariable("quick_menu", False), Show("notebook_inside"), Play ("sound", "audio/notebook_sounds_onepage.wav")
        action [Hide("notebook_button"), Show("notebook_inside")], Play ("sound", "audio/notebook_sounds_onepage.wav")

screen notebook_inside:
    modal True
    frame:
        vbox:
            #xoffset 200
            #yoffset 150
            xalign 0.2
            yalign 0.5
            #xoffset -50
            spacing 50
            textbutton "People":
                text_size 50
                action Show("notebook_people"), Play ("sound", "audio/notebook_sounds_button.wav")
            
            if objects_notebook == True:
                textbutton "Objects":
                    text_size 50
                    action [Hide("notebook_inside"), Show("notebook_objects")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                textbutton "???":
                    text_size 50

            #if info_notebook == True:
            textbutton "Notes":
                text_size 50
                action Show("notebook_info"), Play ("sound", "audio/notebook_sounds_button.wav")
            #else:
                #textbutton "???":
                    #text_size 50

            if clues_notebook == True:
                textbutton "Clues":
                    text_size 50
                    action NullAction(), Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                textbutton "???":
                    text_size 50
        hbox:
            xpos 0.9
            xoffset -5
            yoffset 20
            textbutton "close":
                text_size 40
                action SetVariable("quick_menu", True), Play ("sound", "audio/notebook_sounds_thump.wav"), [Hide("notebook_inside"), Show("notebook_button")]


screen notebook_people:
    modal True
    frame:
        vbox:
            #xoffset 200
            xoffset 60
            yoffset 150
            spacing 25
            textbutton "Me":
                action [Show("notebook_people_mc"), Hide ("notebook_people_bb"), Hide ("notebook_people_bl"), Hide ("notebook_people_d")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif dd_name == True:
                textbutton "Doctor":
                    action [Show("notebook_people_d"), Hide ("notebook_people_bb"), Hide ("notebook_people_bl"), Hide ("notebook_people_mc")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass

            showif cc_name == True:
                textbutton "Cute Cook":
                    action NullAction()
            else:
                pass

            showif gg_name == True:
                textbutton "Gentle Giant":
                    action NullAction()
            else:
                pass

            showif bb_name == True:
                textbutton "Bad Boy":
                    action [Show("notebook_people_bb"), Hide ("notebook_people_d"), Hide ("notebook_people_bl"), Hide ("notebook_people_mc")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass

            showif bm1_name == True:
                textbutton "Business Man 1":
                    action NullAction()
            else:
                pass

            showif bm2_name == True:
                textbutton "Business Man 2":
                    action NullAction()
            else:
                pass

            showif bl_name == True:
                textbutton "Barista Lady":
                    action [Show("notebook_people_bl"), Hide ("notebook_people_bb"), Hide ("notebook_people_d"), Hide ("notebook_people_mc")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass

            showif lbguy_name == True:
                textbutton "Love Bird Guy":
                    action NullAction()
            else:
                pass

            showif lbgirl_name == True:
                textbutton "Love Bird Girl":
                    action NullAction()
            else:
                pass

            showif lbgirl_name == True and pg_name == False:
                textbutton "???"

            elif pg_name == True:
                    textbutton "Pretty Girl":
                        action NullAction()
            else:
                pass
        hbox:
            xpos 0.9
            xoffset -5
            yoffset 20
            textbutton "return":
                text_size 40
                action [Hide("notebook_people"), Hide ("notebook_people_bb"), Hide ("notebook_people_mc"), Hide ("notebook_people_bl"), Hide ("notebook_people_d"), Show("notebook_inside")], Play ("sound", "audio/notebook_sounds_onepage.wav")

screen notebook_people_mc:
    modal True
    dismiss action Hide ("notebook_people_mc")
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "[name]"
        image "images/player.png":
            yalign 0.5
            xpos 0.55
            xzoom 1.6
            yzoom 1.6
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 20
                text "Info:":
                    xoffset -50
                text "In my 20 somethings."
                text "Use plants as bookmarks sometimes."
                text "Currently hungry"
            
        #hbox:
        #    xpos 0.9
        #    xoffset -5
        #    yoffset 20
        #    textbutton "return":
        #        text_size 40
        #        action Hide("notebook_people_mc")

screen notebook_people_d:
    #modal True
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Doctor"
        image "images/doctor.png":
            yalign 0.0
            xpos 0.55
            xzoom 1.5
            yzoom 1.5
        vbox:
            #xmaximum 550
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 600
            vbox:
                spacing 20
                text "Info:":
                    xoffset -50
                text "A man of great taste in novels."
                showif d_fear == True and d_fear_revealed == False:
                    text "Paralyzing fear of thunderstorms."
                showif d_fear and d_fear_revealed == True:
                    text "Paralyzing fear of thunderstorms, because of childhood trauma."
            vbox:
                spacing 10
                text "love points":
                    xoffset -50
                bar value VariableValue ("d_attraction_points", 50):
                    xmaximum 450
                    xoffset 50
            vbox:
                spacing 10
                text "friendship points":
                    xoffset -50
                bar range 10/10:
                    xmaximum 450
                    xoffset 50
            vbox:
                spacing 10
                text "morality":
                    xoffset -50
                bar range 10/10:
                    xmaximum 450
                    xoffset 50
                
                
        #hbox:
        #    xpos 0.9
        #    xoffset -5
        #    yoffset 20
        #    textbutton "return":
        #        text_size 40
        #        action Hide("notebook_people_d")

screen notebook_people_bl:
    #modal True
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Barista Lady"
        image "images/baristalady.png":
            yalign 0.1
            xpos 0.55
            xzoom 1.6
            yzoom 1.6
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 20
                text "Info:":
                    xoffset -50
                text "Maybe in her 50's?."
                text "Found out her name from her name tag."
                if lb_affection_points >= 2:
                    text "She seems nice."
                else:
                    pass

screen notebook_people_bb:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Bad Boy"
        image "images/badboy.png":
            yalign 0.1
            xpos 0.55
            xzoom 1.6
            yzoom 1.6
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 20
                text "Info:":
                    xoffset -50
                if understanding_bb == True:
                    text "Seems grumpy at first glance."
                else:
                    text "Grumpy."
                if bb_interests == True:
                    text "Likes classical music and literature."
                else:
                    pass


screen notebook_info:
    modal True
    frame:
        vbox:
            xoffset 40
            yoffset 20
            spacing 20
            textbutton "another hit novel":
                action [Show("notebook_info_hitnovel"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide("notebook_info_restroombreaks"),  Hide ("notebook_info_expensivedress"), Hide ("notebook_info_businessmeeting"), Hide ("notebook_info_adoctorstrauma")], Play ("sound", "audio/notebook_sounds_button.wav")
            showif cc_dream_info == True:
                vbox:
                    textbutton "cafe dream":
                        action [Show("notebook_info_cafedream"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide("notebook_info_restroombreaks"),  Hide ("notebook_info_expensivedress"), Hide ("notebook_info_businessmeeting"), Hide ("notebook_info_adoctorstrauma")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
                        #action [Show("notebook_info_cafedream")], Play ("sound", "audio/notebook_sounds_button.wav")
            showif bm_meeting_info == True:
                vbox:
                    textbutton "business meeting":
                        action [Show("notebook_info_businessmeeting"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide("notebook_info_restroombreaks"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_adoctorstrauma")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_dress == True:
                vbox:
                    textbutton "an expensive dress":
                        action [Show("notebook_info_expensivedress"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif d_fear == True:
                vbox:
                    textbutton "a doctor's trauma":
                        action [Show("notebook_info_adoctorstrauma"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide("notebook_info_restroombreaks"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_restroom == True:
                vbox:
                    textbutton "restroom breaks":
                        action [Show("notebook_info_restroombreaks"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif bb_badbreakup == True:
                vbox:
                    textbutton "nice boy, bad breakup":
                        action [Show("notebook_info_badbreakup"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif albino_undead == True:
                vbox:
                    textbutton "fear of the undead":
                        action [Show("notebook_info_undead"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif braids_goryart == True:
                vbox:
                    textbutton "gory art":
                        action [Show("notebook_info_goryart"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif gg_gentlegarden == True:
                vbox:
                    textbutton "gentle garden":
                        action [Show("notebook_info_gentlegarden"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif lbguy_datingsmart == True:
                vbox:
                    textbutton "dating the smart girl":
                        action [Show("notebook_info_datingsmart"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif lbgirl_distress == True:
                vbox:
                    textbutton "damsel causes distress":
                        action [Show("notebook_info_distress"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_wealthyfamily == True:
                vbox:
                    textbutton "wealthy family":
                        action [Show("notebook_info_wealthyfamily"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_obsessions == True:
                vbox:
                    textbutton "obsessions":
                        action [Show("notebook_info_obsessions"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_poison == True:
                vbox:
                    textbutton "powder":
                        action [Show("notebook_info_poison"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
            showif pg_inheritance == True:
                vbox:
                    textbutton "inheritance":
                        action [Show("notebook_info_inheritance"), Hide ("notebook_info_hitnovel"), Hide("notebook_info_poison"), Hide("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_badbreakup"), Hide ("notebook_info_restroombreaks"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                pass
        hbox:
                xpos 0.9
                xoffset -5
                yoffset 20
                textbutton "return":
                    text_size 40
                    action [Hide("notebook_info"), Hide ("notebook_info_hitnovel"), Hide ("notebook_info_inheritance"), Hide ("notebook_info_poison"), Hide ("notebook_info_obsessions"), Hide ("notebook_info_wealthyfamily"), Hide ("notebook_info_distress"), Hide ("notebook_info_datingsmart"), Hide ("notebook_info_gentlegarden"), Hide ("notebook_info_goryart"), Hide ("notebook_info_undead"), Hide ("notebook_info_restroombreaks"), Hide("notebook_info_restroombreaks"), Hide ("notebook_info_expensivedress"), Hide ("notebook_info_adoctorstrauma"), Hide ("notebook_info_cafedream"), Hide ("notebook_info_businessmeeting"), Show("notebook_inside")], Play ("sound", "audio/notebook_sounds_onepage.wav")

screen notebook_info_hitnovel:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Another Hit Novel" 
        hbox:
            image "images/player.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Off to write another hit novel!{p}... or die trying."

screen notebook_info_cafedream:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Cafe dream"
        if cc_name == True:
            image "images/cutecook.png":
                yalign 0.5
                xpos 0.55
                xzoom 1.6
                yzoom 1.6
        else: 
            pass
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                #spacing 20
                #xmaximum 720
                #hbox:
                #    textbutton "Cute Cook":
                #        yoffset -6.8
                #        xoffset -8
                #        #clicking name should bring you to character info screen
                #        action Play ("sound", "audio/notebook_sounds_onepage.wav"), NullAction()
                #    text "dreamed of opening a Cafe in"
                #hbox:
                #    text "the city, but"
                #    textbutton "his mother":
                #        yoffset -6.8
                #        #clicking name should bring you to character info screen
                #        action Play ("sound", "audio/notebook_sounds_onepage.wav"), NullAction()
                #    text"convinced him to"
                #text "stay managing the diner with her."
                #spacing 10
                spacing 30
                xmaximum 720
                if cc_name == True:
                    text "Cute Cook dreamed of opening a Cafe in the city, but his mother convinced him to stay managing the diner."
                else: 
                    text "The owner's son dreamed of opening a Cafe in the city, but his mother convinced him to stay managing the diner."
        hbox:
            #yoffset 250
            xalign 0.35
            spacing 5
            xmaximum 1000
            yalign 0.9  
            text "Heard from:"
                #xoffset 50
            textbutton "Barista Lady":
                #xoffset 50
                yoffset -6.8
                #clicking name should bring you to character info screen
                action Play ("sound", "audio/notebook_sounds_onepage.wav"), [Hide ("notebook_info_cafedream"), Show ("notebook_people"), Show ("notebook_people_bl")]
                
screen notebook_info_businessmeeting:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Business Meeting"
        hbox:
            spacing -20
            image "images/businessman1.png":
                ypos 0.2
                xpos 2.05
                xzoom 1.0
                yzoom 1.0
            image "images/businessman2.png":
                ypos 0.2
                xpos 2.05
                xzoom 1.0
                yzoom 1.0
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                if bm1_name == True and bm2_name == True:
                    text "Bm1 and Bm2 were having a private business meeting; in a Cafe, in the middle of nowhere."
                    text "They either don't have an office or the coffee here is expectacular."
                else: 
                    text "Two men having a private business meeting in a Cafe in the middle of nowhere."
                    text "They either don't have an office or the coffee here is expectacular."

screen notebook_info_adoctorstrauma:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "A doctor's trauma"
        hbox:
            image "images/doctor.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                if d_fear == True and d_fear_revealed == True:
                    text "Jay Wallace confided in me his paralyzing fear of thunderstorms due to childhood trauma."
                else: 
                    text "Jay Wallace confided in me his paralyzing fear of thunderstorms"

screen notebook_info_expensivedress:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "An Expensive Dress"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "A woman wearing an expensive dress to a diner in the middle of nowhere."
                
screen notebook_info_restroombreaks:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Restroom Breaks"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "According to BB, she repeteadly went to the restroom."

screen notebook_info_badbreakup:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Nice boy, Bad break up"
        hbox:
            image "images/badboy.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "According to BL he's a sweet boy who's going through a bad breakup."

screen notebook_info_undead:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Fear of the Undead"
        hbox:
            image "images/businessman2.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Albino is terrified of zombies, ghosts, and gore apparently."

screen notebook_info_goryart:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Gory Art"
        hbox:
            image "images/businessman1.png":
                yalign 0.0
                xpos 2.7
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Braids loves drawing gory art."

screen notebook_info_gentlegarden:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Gory Art"
        hbox:
            image "images/gentlegiant.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Loves gardening and dreams of opening up a flower shop."

screen notebook_info_datingsmart:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Dating te Smart Girl"
        hbox:
            image "images/lovebirdguy.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "This man had to study a lot for his girlfriend to notice him."

screen notebook_info_distress:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Damsel causing Distress"
        hbox:
            image "images/lovebirdgirl.png":
                yalign 0.0
                xpos 1.45
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "She protects her boyfriend from persistent women."

screen notebook_info_wealthyfamily:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Wealthy Family"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "She comes from very old money."

screen notebook_info_obsessions:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Obsessions"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Unhealthy obsession with lbguy."

screen notebook_info_poison:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Poison"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "Brown powder was found on her finger tips."

screen notebook_info_inheritance:
    fixed:
        vbox:
            xalign 0.48
            yalign 0.07
            text "Inheritance"
        hbox:
            image "images/prettygirl.png":
                yalign 0.0
                yoffset 25
                xpos 3.2
                xzoom 1.5
                yzoom 1.5
        vbox:
            #xoffset 200
            yoffset 250
            xpos 0.265
            #xalign 0.35
            spacing 65
            xmaximum 1000
            vbox:
                spacing 30
                xmaximum 720
                text "From a matriarcal lineage, she's about to inherit her whole family fortune."


screen notebook_objects:
    modal True
    dismiss action [Hide("notebook_objects"), Show("notebook_inside")]
    frame:
        #background Solid("#7ca397ff")
        background Solid("#0000ff00") # transparent
        #background "images/frame2.png"
        image "images/bag_bg2.png":
            xalign 0.5
            yalign 0.5
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 10 ### temporary
            box_wrap True

            showif clover == True:
                vbox:
                    textbutton "Lucky Clover":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")           

            showif businesscard == True:
                vbox:
                    textbutton "Business Card":
                        if businesscard_object:
                            action [Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")
                        else:
                            action NullAction()
            showif businesscard_bm2 == True:
                vbox:
                    textbutton "Old Business Card":
                        action NullAction()

            showif pamphlet == True:
                vbox:
                    textbutton "Pamphlet":
                        action NullAction()

            showif mc_keys == True:
                vbox:
                    textbutton "Keys and Driver's License":
                        if keys_object:
                            action [Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("mc_keys", False), Jump ("ids")], Play ("sound", "audio/notebook_sounds_button.wav")
                        else:
                            action NullAction()

            showif old_picture == True:
                vbox:
                    textbutton "Old Picture":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif pg_phone == True:
                vbox:
                    textbutton "Victim's Phone":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")
            
            showif note:
                vbox:
                    textbutton "Torn Note":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif charger == True:
                vbox:
                    textbutton "Phone Charger":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif hunting_knife:
                vbox:
                    textbutton "Hunting Blade":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif dagger == True:
                vbox:
                    if empty_sheath:
                        textbutton "Expensive Dagger, Sheated":
                            action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")
                    else:
                        textbutton "Expensive Dagger, Unsheated":
                            action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")
            else:
                if empty_sheath == True:
                    vbox:
                        textbutton "Empty Sheath":
                            action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif umbrella == True:
                vbox:
                    textbutton "Umbrella":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif wirecutters == True:
                vbox:
                    textbutton "Wirecutters":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif poison_bottle == True:
                vbox:
                    textbutton "Poison bottle":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif peanutbutter == True:
                vbox:
                    textbutton "Peanut Butter":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif sardines == True:
                vbox:
                    textbutton "Sardines":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif cat_object == True:
                vbox:
                    textbutton "CAT":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif cat_accessory_1 == True:
                vbox:
                    textbutton "Tiny Bow":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

            showif cat_accessory_2 == True:
                vbox:
                    textbutton "Cat Glasses":
                        action NullAction() #[Hide ("notebook_objects"), Hide ("notebook_inside"), SetVariable("businesscard", False), Jump ("businesscard")], Play ("sound", "audio/notebook_sounds_button.wav")

        #hbox:
                #xpos 0.9
                #xoffset -5
                #yoffset 20
                #textbutton "return":
                #    text_size 40
                #    action Hide("notebook_objects"), Play ("sound", "audio/notebook_sounds_onepage.wav")


## interrogation stuff

screen interrogation_options:
    modal True
    if act > 0:
        imagebutton: 
            xalign 0.17
            yalign 0.93
            idle "images/mbttn.png" 
            action [Hide("interrogation_options"), Jump("interrogation_questions")], Play("sound", "audio/notebook_sounds_button.wav")

        imagebutton: 
            xalign 0.35
            yalign 0.9
            idle "images/nbttn.png" 
            action [Hide("interrogation_options"), Show("people_interrogation")], Play ("sound", "audio/notebook_sounds_button.wav")

        imagebutton: 
            xalign 0.635
            yalign 0.89
            idle "images/bbttn.png" 
            action [Hide("interrogation_options"), Show("objects_interrogation")], Play ("sound", "audio/notebook_sounds_button.wav")
    
        imagebutton: 
            xalign 0.83
            yalign 0.93
            idle "images/babttn.png" 
            action [Hide("interrogation_options"), Jump("investigation_middle")], Play ("sound", "audio/notebook_sounds_button.wav")
    else: 
        imagebutton: 
            xalign 0.635
            yalign 0.89
            idle "images/bbttn.png" 
            action [Hide("interrogation_options"), Show("objects_interrogation")], Play ("sound", "audio/notebook_sounds_button.wav")

    image "images/nb.png":
        xalign 0.5
        yalign 1.0            

screen people_interrogation:
    modal True
    #image "images/colors_dark.png"
    #grid 5 2:
    frame:
        background Solid("#0000ff00")
        align (0.5, 0.2)
        hbox:
            xalign 0.5
            ypos 0.55
            yanchor 0.5
            spacing 50
            box_wrap True
            imagebutton:
                idle "images/side/side mc.png"
                hover "images/side/side mc h.png" 
                action [SetVariable ("people_mc", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif bb_interrogation == False:
                imagebutton:
                    idle "images/side/side bb.png"
                    hover "images/side/side bb h.png" 
                    action [SetVariable ("people_bb", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif dd_interrogation == False:
                imagebutton:
                    idle "images/side/side d.png"
                    hover "images/side/side d h.png" 
                    action [SetVariable ("people_dd", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif gg_interrogation == False:
                imagebutton:
                    idle "images/side/side gg.png"
                    hover "images/side/side gg h.png" 
                    action [SetVariable ("people_gg", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif cc_interrogation == False:
                imagebutton:
                    idle "images/side/side cc.png"
                    hover "images/side/side cc h.png" 
                    action [SetVariable ("people_cc", True), Hide("people_interrogation"), Jump("people_interrogation")]
            imagebutton:
                idle "images/side/side pg.png"
                hover "images/side/side pg h.png" 
                action [SetVariable ("people_pg", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif bl_interrogation == False:
                imagebutton:
                    idle "images/side/side bl.png"
                    hover "images/side/side bl h.png" 
                    action [SetVariable ("people_bl", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif lbgirl_interrogation == False:
                imagebutton:
                    idle "images/side/side lbgirl.png"
                    hover "images/side/side lbgirl h.png" 
                    action [SetVariable ("people_lbgirl", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif lbguy_interrogation == False:
                imagebutton:
                    idle "images/side/side lbguy.png"
                    hover "images/side/side lbguy h.png" 
                    action [SetVariable ("people_lbguy", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif albino_interrogation == False:
                imagebutton:
                    idle "images/side/side bm1.png"
                    hover "images/side/side bm1 h.png" 
                    action [SetVariable ("people_albino", True), Hide("people_interrogation"), Jump("people_interrogation")]
            showif braids_interrogation == False:
                imagebutton:
                    idle "images/side/side bm2.png"
                    hover "images/side/side bm2 h.png" 
                    action [SetVariable ("people_braids", True), Hide("people_interrogation"), Jump("people_interrogation")]
    frame:
        xalign 0.97
        yalign 0.0
        yoffset 30
        vbox:
            textbutton "return":
                text_size 39
                action [Hide("people_interrogation"), Jump ("interrogation_screen")]

screen objects_interrogation:
    modal True
    dismiss action [Hide("objects_interrogation"), Play ("sound", "audio/notebook_sounds_onepage.wav"), Jump ("interrogation_screen")]
    frame:
        #background Solid("#7ca397ff")
        background Solid("#0000ff00") # transparent
        #background "images/frame2.png"
        image "images/bag_bg2.png":
            xalign 0.5
            yalign 0.5
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 490 ### temporary
            box_wrap True
            
            showif clover == True:
                vbox:
                    textbutton "Lucky Clover":
                        action [SetVariable ("clover_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif businesscard == True:
                vbox:
                    textbutton "Business Card":
                        action [SetVariable ("businesscard_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif businesscard_bm2 == True:
                vbox:
                    textbutton "Old Business Card":
                        action [SetVariable ("businesscard_bm2_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif pamphlet == True:
                vbox:
                    textbutton "Pamphlet":
                        action [SetVariable ("pamphlet_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif mc_keys == True:
                vbox:
                    textbutton "Keys and Driver's License":
                        action [SetVariable ("mc_keys_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif old_picture == True:
                vbox:
                    textbutton "Old Picture":
                        action [SetVariable ("old_picture_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif pg_phone == True:
                vbox:
                    textbutton "Victim's Phone":
                        action [SetVariable ("pg_phone_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]
            
            showif note:
                vbox:
                    textbutton "Torn Note":
                        action [SetVariable ("note_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif charger == True:
                vbox:
                    textbutton "Phone Charger":
                        action [SetVariable ("charger_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif hunting_knife:
                vbox:
                    textbutton "Hunting Blade":
                        action [SetVariable ("hunting_knife_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif dagger == True:
                vbox:
                    if empty_sheath:
                        textbutton "Expensive Dagger, Sheated":
                            action [SetVariable ("sheathed_dagger_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]
                    else:
                        textbutton "Expensive Dagger, Unsheated":
                            action [SetVariable ("dagger_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]
            else:
                if empty_sheath == True:
                    vbox:
                        textbutton "Empty Sheath":
                            action [SetVariable ("empty_sheath_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif umbrella == True:
                vbox:
                    textbutton "Umbrella":
                        action [SetVariable ("umbrella_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif wirecutters == True:
                vbox:
                    textbutton "Wirecutters":
                        action [SetVariable ("wirecutters_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif poison_bottle == True:
                vbox:
                    textbutton "Poison bottle":
                        action [SetVariable ("poison_bottle_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif peanutbutter == True:
                vbox:
                    textbutton "Peanut Butter":
                        action [SetVariable ("peanutbutter_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif sardines == True:
                vbox:
                    textbutton "Sardines":
                        action [SetVariable ("sardines_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif cat_object == True:
                vbox:
                    textbutton "CAT":
                        action [SetVariable ("cat_object_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif cat_accessory_1 == True:
                vbox:
                    textbutton "Tiny Bow":
                        action [SetVariable ("cat_accessory_1_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]

            showif cat_accessory_2 == True:
                vbox:
                    textbutton "Cat Glasses":
                        action [SetVariable ("cat_accessory_2_i", True), Hide("objects_interrogation"), Jump("objects_interrogation")]


### objects screens

screen car_door_wait:
    imagebutton:
        xanchor 2.0
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_left_%s.png"
        action Return() 

screen car_door:
    imagebutton:
        xanchor 2.0
        yanchor 0.5
        xpos 0.5
        ypos 0.85
        auto "gui/arrow_left_%s.png"
        action Jump("outside_intro") 

screen brokenstool:

    #$ broken_flag = True

    imagebutton:
        xpos 0.69
        yanchor -2.5
        auto "brokenstool_%s.png"
        #action NullAction()
        #action Call("broken_dialogue")
        #$ broken_flag = True
        action Jump("broken_dialogue")

screen idcards:
    imagebutton:
        xanchor 2.7
        yanchor 1.25
        xpos 0.5
        ypos 0.85
        auto "gui/testbutton_%s.png"
        action Jump("idcards_taken") 

screen deadbody:
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "gui/testbutton_%s.png"
        action Jump("deadbody")       
    
screen deadbody_close: 
    hbox:
        xalign 0.5
        yalign 0.5
        imagebutton:
            auto "gui/testbutton_%s.png"
            action Jump("deadbody_wound")
        imagebutton:
            auto "gui/testbutton_%s.png"
            action Jump("deadbody_dress") 
        imagebutton:
            auto "gui/testbutton_%s.png"
            action Jump("deadbody_hands") 
        imagebutton:
            auto "gui/testbutton_%s.png"
            action Jump("deadbody_purse") 

screen deadbody_purse:
    hbox:
        xalign 0.5
        yalign 0.5
        showif empty_sheath == False:
            imagebutton:
                auto "gui/testbutton_%s.png"
                action Jump("deadbody_sheath")
        else:
            pass
        showif pg_phone == False:
            imagebutton:
                auto "gui/testbutton_%s.png"
                action Jump("deadbody_phone")
        else:
            pass
        imagebutton:
            auto "gui/testbutton_%s.png"
            action Jump("deadbody_id") 
        imagebutton:
            auto "gui/testbutton_%s.png"
            action NullAction()

#screen dagger:

#screen poison bottle:

screen pg_phone_locked:
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "gui/testbutton_%s.png"
        action Jump("deadbody_phone_locked")

#screen pg_phone_open:

#screen sardines:        


### characters screens

screen cat:
    imagebutton:  
        #focus_mask True 
        xanchor 0.5
        yanchor 1.5
        xpos 0.5
        ypos 0.85
        auto "images/cat_%s.png"
        action Hide("cat", transition=Dissolve(0.5))
        #Play("sound", "audio/bell.wav")

screen cat_door:
    imagebutton:  
        xpos 0.13
        ypos 0.58
        auto "images/cat_%s.png"
        action Hide("cat_door", transition=Dissolve(0.5))

screen response1(who,what):
    style_prefix "say"
    window id "window":         
        has vbox
        #    spacing 10
        if who:
            text who id "who"
        text what id "what"

screen response:
    textbutton "here":
        xalign 0.5
        yalign 0.5
        #action Show("response1")
        action NullAction()

screen bm_sitting:

    imagebutton:
        xpos 0.6
        #yanchor -2.5
        idle "businessman1.png"
        #action NullAction()
        action Jump("business_dialogue")
    imagebutton:
        xpos 0.15
        #yanchor -2.5
        idle "businessman2.png"
        #action NullAction()
        action Jump("business_dialogue")

screen d_description:
    frame:
        yalign 0.0
        xalign 0.5
        yoffset 20
        xminimum 1000
        yminimum 70
        text "Hadn't noticed that guy sitting there before.":
            xalign 0.5
            yalign 0.7

screen doctor_sitting:
    #image top_text = ParameterizedText (xalign=0.5, yalign=0.5)
    if ask_flag == True:
        imagebutton:
            yanchor -0.935
            auto "doctor_sitting_small_%s.png"
            hovered Show ("d_description")
            unhovered Hide ("d_description")
            #Show (top_text "hello tere obi wan")
            action Jump("doctor_intro")

    else:
        imagebutton:
            yanchor -0.935
            auto "doctor_sitting_small_%s.png"
            hovered Show ("d_description")
            unhovered Hide ("d_description")
            #Show (top_text "hello tere obi wan")
            action NullAction()

screen doctor_sat:
    imagebutton:
        xpos 0.2
        ypos 0.0
        idle "doctor.png"
        action NullAction()

screen prettygirl_sitting:
    imagebutton:
        xpos 0.65
        yanchor -0.43
        auto "prettygirl_sitting_small_%s.png"
        #action Show("say", "jijij")
        action [SetVariable("pg_dress", True), Jump("pg_dialogue")]

screen gg_sitting:
    imagebutton:
        xpos 0.74
        yanchor -0.5
        auto "gg_%s.png"
        action Jump("gg_dialogue")

screen l_description:
    frame:
        yalign 0.0
        xalign 0.5
        yoffset 20
        xminimum 1000
        yminimum 70
        #I should ask the lady behind the bar
        text "Feels like the only option...":
            xalign 0.5
            yalign 0.7

screen old_lady:
    imagebutton:
        xalign 0.1
        idle "baristalady.png"
        hovered Show ("l_description")
        unhovered Hide ("l_description")
        action SetVariable("ask_flag",True), Jump("this_is_it")   
        #SetVariable("old_lady_flag",True), 
        #SetVariable("ask_flag",True),

screen l2_description:
    frame:
        yalign 0.0
        xalign 0.5
        yoffset 20
        xminimum 1000
        yminimum 70
        text "She said this is the place.":
            xalign 0.5
            yalign 0.7    

screen old_lady2:
    imagebutton:
        xalign 0.1
        idle "baristalady.png"
        hovered Show ("l2_description")
        unhovered Hide ("l2_description")
        action SetVariable("asked_flag", True), Jump("this_is_it_done") 

screen interrogation_bl:
    imagebutton:
        xalign -0.05
        idle "baristalady.png"
        action Jump ("interrogation_bl")
        
screen interrogation_cc:
    imagebutton:
        xalign 0.1
        idle "cutecook.png"
        action Jump ("interrogation_cc")

screen interrogation_gg:
    imagebutton:
        xalign 0.3
        idle "gentlegiant.png"
        action Jump ("interrogation_gg")

screen interrogation_bb:
    imagebutton:
        xalign 0.5
        idle "badboy.png"
        action Jump ("interrogation_bb")

screen interrogation_albino:
    imagebutton:
        xalign 0.65
        idle "businessman2.png" 
        action Jump ("interrogation_albino")

screen interrogation_braids:
    imagebutton:
        xalign 0.8
        idle "businessman1.png"
        action Jump ("interrogation_braids")
        #action SetVariable("ask_flag",True), Jump("this_is_it")   

screen interrogation_lbguy:
    imagebutton:
        xalign 0.95
        idle "lovebirdguy.png"
        action Jump ("interrogation_lbguy")

screen interrogation_lbgirl:
    imagebutton:
        xalign 1.08
        idle "lovebirdgirl.png"
        action Jump ("interrogation_lbgirl")


#screen hide:
    #action HideInterface()

### python functions

init python: #objectsInterrogation
    def objectsInterrogation(act = 0, level = 0, businesscard_i = False, pamphlet_i = False, clover_i = False, umbrella_i = False, mc_keys_i = False, shovel_i = False, pg_phone_i = False, pg_picture_i = False, charger_i = False, old_picture_i = False, note_i = False, cat_object_i = False, keys_object_i = False, wirecutters_i = False, businesscard_bm2_i = False, hunting_knife_i = False, empty_sheath_i = False, poison_bottle_i = False, dagger_i = False, sheathed_dagger_i = False, peanutbutter_i = False, sardines_i = False, cat_accessory_1_i = False, cat_accessory_2_i = False, dd_interrogation = False, bb_interrogation = False, gg_interrogation = False, cc_interrogation = False, albino_interrogation = False, braids_interrogation = False, bl_interrogation = False, lbguy_interrogation = False, lbgirl_interrogation = False):
        if act > 0:
            act -= 1
        level -= 1

        if bb_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = bb

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif dd_interrogation:
            
            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = d

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif cc_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = cc

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif gg_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = gg

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif albino_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = bm2

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif braids_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = bm1

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif bl_interrogation:

            businesscard = ["You're a writer?{p}That's quite something, sweatheart."],["act 2. ob"],["act 3. ob"]
            pamphlet = ["That's the pamphlet for our Diner."],["act 2. ob"],["act 3. ob"]
            clover = ["A lucky charm, very pretty!"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["I don't know what you want me to do with this."],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = bl

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                if act > 0:
                    renpy.say(p, pamphlet[act][level])
                else:
                    renpy.show_screen("notebook_button")
                    renpy.say(p, "Yep, right there, that's our diner!{p}Well... Not quite.")
                    renpy.say(p, "We're turning it into a Cafe now...{p=0.1}. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
                    renpy.jump("why")

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif lbguy_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = lbguy

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

        elif lbgirl_interrogation:

            businesscard = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pamphlet = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            clover = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            umbrella = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            mc_keys = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            shovel = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_phone = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            pg_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            charger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            old_picture = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            note = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            keys_object = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            wirecutters = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            businesscard_bm2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            hunting_knife = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            empty_sheath = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            poison_bottle = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sheathed_dagger = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            peanutbutter = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            sardines = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_1 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]
            cat_accessory_2 = ["act 1. ob"],["act 2. ob"],["act 3. ob"]

            p = lbgirl

            if businesscard_i:
                renpy.say(p, businesscard[act][level])

            elif pamphlet_i:
                renpy.say(p, pamphlet[act][level])

            elif clover_i:
                renpy.say(p, clover[act][level])

            elif umbrella_i:
                renpy.say(p, umbrella[act][level])

            elif mc_keys_i:
                renpy.say(p, mc_keys[act][level])
                
            elif shovel_i:
                renpy.say(p, shovel[act][level])

            elif pg_phone_i:
                renpy.say(p, pg_phone[act][level])

            elif pg_picture_i:
                renpy.say(p, pg_picture[act][level])

            elif charger_i:
                renpy.say(p, charger[act][level])
                
            elif old_picture_i:
                renpy.say(p, old_picture[act][level])
                
            elif note_i:
                renpy.say(p, note[act][level])

            elif cat_object_i:
                renpy.say(p, cat_object[act][level])

            elif keys_object_i:
                renpy.say(p, keys_object[act][level])

            elif wirecutters_i:
                renpy.say(p, wirecutters[act][level])

            elif businesscard_bm2_i:
                renpy.say(p, businesscard_bm2[act][level])
                
            elif hunting_knife_i:
                renpy.say(p, hunting_knife[act][level])

            elif empty_sheath_i:
                renpy.say(p, empty_sheath[act][level])

            elif poison_bottle_i:
                renpy.say(p, poison_bottle[act][level])

            elif dagger_i:
                renpy.say(p, dagger[act][level])
                
            elif sheathed_dagger_i:
                renpy.say(p, sheathed_dagger[act][level])

            elif peanutbutter_i:
                renpy.say(p, peanutbutter[act][level])

            elif sardines_i:
                renpy.say(p, sardines[act][level])

            elif cat_accessory_1_i:
                renpy.say(p, cat_accessory_1[act][level])
                
            elif cat_accessory_2_i:
                renpy.say(p, cat_accessory_2[act][level])
    
            else:
                renpy.say(p, "...")

init python: #peopleInterrogation
    def peopleInterrogation(act = 0, level = 0, people_mc = False, people_dd = False, people_bb = False, people_gg = False, people_cc = False, people_pg = False, people_albino = False, people_braids = False, people_bl = False, people_lbguy = False, people_lbgirl = False, dd_interrogation = False, bb_interrogation = False, gg_interrogation = False, cc_interrogation = False, albino_interrogation = False, braids_interrogation = False, bl_interrogation = False, lbguy_interrogation = False, lbgirl_interrogation = False):
        act -= 1
        level -= 1

        if bb_interrogation:

            mc_opinion = ["You're asking me about yourself?{p}Well, yeah I saw you come into the cafe."], ["act2."], ["act3."]
            #bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["He arrived a bit earlier than you did,{p}a bit before the rain got worse."], ["act2."], ["act3."]
            gg_opinion = ["He's been at his seat for a while."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = bb

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif dd_interrogation:
            
            mc_opinion = ["act 1. dd"], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            #dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = d

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif cc_interrogation:

            mc_opinion = ["act 1 cc."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            #cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = cc

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif gg_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            #gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = gg

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif albino_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            #albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = bm2

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif braids_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            #braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = bm1

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif bl_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            #bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = bl

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif lbguy_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            #lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = lbgirl

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(p, "...")

        elif lbgirl_interrogation:

            mc_opinion = ["act 1."], ["act2."], ["act3."]
            bb_opinion = ["act 1."], ["act2."], ["act3."]
            dd_opinion = ["act 1."], ["act2."], ["act3."]
            gg_opinion = ["act 1."], ["act2."], ["act3."]
            cc_opinion = ["act 1."],["act 2."],["act 3."]
            pg_opinion = ["act 1."],["act 2."],["act 3."]
            albino_opinion = ["act 1."],["act 2."],["act 3."]
            braids_opinion = ["act 1."],["act 2."],["act 3."]
            bl_opinion = ["act 1."],["act 2."],["act 3."]
            lbguy_opinion = ["act 1."],["act 2."],["act 3."]
            #lbgirl_opinion = ["act 1."],["act 2."],["act 3."]

            p = lbgirl

            if people_mc:
                renpy.say(p, mc_opinion[act][level])

            elif people_bb:
                renpy.say(p, bb_opinion[act][level])

            elif people_dd:
                renpy.say(p, dd_opinion[act][level])

            elif people_gg:
                renpy.say(p, gg_opinion[act][level])

            elif people_cc:
                renpy.say(p, cc_opinion[act][level])

            elif people_pg:
                renpy.say(p, pg_opinion[act][level])
                
            elif people_albino:
                renpy.say(p, albino_opinion[act][level])

            elif people_braids:
                renpy.say(p, braids_opinion[act][level])

            elif people_bl:
                renpy.say(p, bl_opinion[act][level])

            elif people_lbguy:
                renpy.say(p, lbguy_opinion[act][level])
                
            elif people_lbgirl:
                renpy.say(p, lbgirl_opinion[act][level])
            
            else:
                renpy.say(mc, "...")

init python: 
    def  hidePeopleInterrogation():                 
        renpy.hide_screen("interrogation_gg")
        renpy.hide_screen("interrogation_bb")
        renpy.hide_screen("interrogation_cc")
        renpy.hide_screen("interrogation_albino")
        renpy.hide_screen("interrogation_braids")
        renpy.hide_screen("interrogation_bl")
        renpy.hide_screen("interrogation_lbguy")
        renpy.hide_screen("interrogation_lbgirl")
        ## add doctor later

init python:
    def hidePeopleEating():
        renpy.hide_screen("doctor_sitting")
        renpy.hide_screen("prettygirl_sitting")
        renpy.hide_screen("doctor_sat")
        renpy.hide_screen("gg_sitting")
        renpy.hide_screen("brokenstool")


##################################################################3

label start:

    ### flag variables ###
    #$ broken_flag = False
    $ interrogation_flag = False 
    $ interrogation_start = False 
    $ b_dialogue = False
    $ sitting_dialogue = False
    $ interrogation_continue = 0
    $ walkback_flag = False
    $ novel_ending = False
    $ novel_what = False
    $ novel_like = False

    ### map variables ###
    $ entrance_scene = False
    $ entrance_scene_dialogue = False
    $ click_flag = 0
    $ cat_flag = False
    $ outsidecar_flag = 0
    $ ask_flag = False
    $ asked_flag = False
    $ restroom_intro = False
    $ kitchen_intro = False
    $ hallway_intro = False
    $ freedom_flag = False

    ### point variables ###
    $ d_attraction_points = 0
    $ gg_attraction_points = 0
    $ bb_attraction_points = 0
    $ cc_attraction_points = 0
    $ albino_attraction_points = 0    
    $ braids_attraction_points = 0
    $ lbguy_affection_points = 0
    $ lbgirl_affection_points = 0
    $ lb_affection_points = 0

    ### story variables ###    
    $ act = 0

    $ tutorial_bag = False

    $ dd_closed = False
    $ bb_closed = False
    $ cc_closed = False
    $ gg_closed = False
    $ albino_closed = False
    $ braids_closed = False
    $ bl_closed = False
    $ lbguy_closed = False    
    $ lbgirl_closed = False

    $ dd_interrogation = False
    $ bb_interrogation = False
    $ gg_interrogation = False
    $ cc_interrogation = False
    $ albino_interrogation = False
    $ braids_interrogation = False
    $ bl_interrogation = False
    $ lbguy_interrogation = False
    $ lbgirl_interrogation = False

    $ people_mc = False
    $ people_dd = False
    $ people_bb = False    
    $ people_gg = False
    $ people_cc = False
    $ people_pg = False
    $ people_albino = False
    $ people_braids = False
    $ people_bl = False
    $ people_lbguy = False
    $ people_lbgirl = False

    ### interrogation variables ###
    $ businesscard_i = False
    $ pamphlet_i = False
    $ clover_i = False
    $ mc_keys_i = False
    $ umbrella_i = False     
    $ shovel_i = False
    $ pg_phone_i = True
    $ pg_picture_i = False
    $ charger_i = False      
    $ old_picture_i = False
    $ note_i = False
    $ cat_object_i = False   
    $ keys_object_i = False
    $ wirecutters_i = False
    $ businesscard_bm2_i = False
    $ hunting_knife_i = False
    $ empty_sheath_i = False
    $ poison_bottle_i = False
    $ dagger_i = False
    $ sheathed_dagger_i = False
    $ peanutbutter_i = False      
    $ sardines_i = False          
    $ cat_accessory_1_i = False   
    $ cat_accessory_2_i = False   

    $ where_bb = True
    $ unusual_bb = False
    $ butt_bb = True
    $ know_bb = True
    $ understanding_bb = False

    ### notebook variables ###

    $ objects_notebook = True
    $ info_notebook = False
    $ clues_notebook = False

    ### jukebox variables ###

    #$ music_button = False

    ### info variables ###
    $ cc_dream_info = False
    $ bm_meeting_info = False
    $ pg_dress = False
    $ d_fear = False
    $ pg_restroom = False
    $ bb_badbreakup = False
    $ albino_undead = False
    $ braids_goryart = False
    $ gg_gentlegarden = False
    $ lbguy_datingsmart = False
    $ lbgirl_distress = False
    $ pg_wealthyfamily = False
    $ pg_obsessions = False
    $ pg_poison = False
    $ pg_inheritance = False

    ### deep info variables ###
    $ d_fear_revealed = False
    $ bb_interests = False

    ### name variable ###
    $ name = "Max"
    $ cc_name = False
    $ bb_name = False
    $ gg_name = False
    $ pg_name = False
    $ bl_name = False
    $ dd_name = False
    $ bm1_name = False
    $ bm2_name = False
    $ lbguy_name = False
    $ lbgirl_name = False

    ### age variable ###
    $ cc_age = False
    $ bb_age = False
    $ gg_age = False
    $ pg_age = False
    $ bl_age = False
    $ dd_age = False
    $ bm1_age = False
    $ bm2_age = False
    $ lbguy_age = False
    $ lbgirl_age = False

    ### object variables ###
    $ businesscard_object = False
    $ businesscard = True
    $ pamphlet = True
    $ clover = True
    $ mc_keys = True
    $ umbrella = False     # given by bl to check out cars {?}
    $ shovel = False
    $ pg_phone = False
    $ pg_picture = False
    $ charger = False      # draggable unto phone or wall outlet ?
    $ old_picture = False
    $ note = False
    $ cat_object = False   # idk, dont like this
    $ keys_object = False
    $ wirecutters = False
    $ businesscard_bm2 = False
    $ hunting_knife = False
    $ empty_sheath = False
    $ poison_bottle = False
    $ dagger = False
    $ sheathed_dagger = False
    $ peanutbutter = False      # allergen
    $ sardines = False          # draggable onto cat
    $ cat_accessory_1 = False   # draggable onto cat
    $ cat_accessory_2 = False   # draggable onto cat
    

    ### ending variables ###
    define persistent.rudeending = False




    ####################################################### S T A R T ################################################################
    

    #show screen mask
    
    scene diner_lowangle_bg
    #show screen mask
    with fade

    show screen qmenu_button
    show screen notebook_button    

    #show player at textbox

    smc "{b}Coffee Date Murders{/b} {p}-a Murder Mystery Otome game-"

    #show screen test

    #smc "Jump to end?"

    #hide screen test

    hide screen notebook_button   

label road:

    play music "audio/maintune_happy2.wav" fadein 8.0 #volume 0.6

    scene car_road_bg  

    #"screen car_inside"

    #hide screen mask

    with fade
    
    #play sound

    #image top_text = ParameterizedText (xalign=0.5, yalign=0.5)

    #show top_text "a bargain or somtin"

    smcs "What am I doing here again?"

    e "You're on a writer's retreat."

    smcs "Right, {w}but why am I driving to the middle of nowhere?"

    e "My husband recommended it."
    
    e "Before moving to the city, he'd go to that diner to disconnect and he would suddenly be inspired with new ideas."
    
    smcs "And by \"disconnect\" you mean that no type of cell signal reaches the place."
    
    e "And so, you will be doing the same." 

    smcs "What if something happens to me? {w}I won't be able to reach you.{p}Will you be able to handle the shock? {w}{b}Think about your baby!{/b}"

    e "I'm your editor, not your bodyguard. If something happens to you I'll probably sell more books, so get on with it."

    #smcs "But-" with hpunch 

    smcs "Geez,{w} talk about client loyalty!{p}You wound me, madame!" with hpunch

    #play sound "audio/lasershot.wav"

    stop music

    play sound "audio/pulse.wav" volume 0.5 loop
    
    smcs "I-" with vpunch

    #glitches/signal lost

    smcs "Hello? {w} Miriam?"
    
    "....................................................................................."

    smcs "Yep, {w}signal's lost." 

    stop sound

    queue sound "audio/click2.wav" 
    
    queue music "audio/restingsuspicion.wav" fadein 0.5

    smcs "Looks like I've entered the dead zone."

    smcs "I'm glad her husband stopped her from coming with me.{p}She's due in a few weeks for her first child..."
    
    smcs "{cps=150}...or am I her first child? {w=0.6}{cps=70}With the way she scolds me for not writing all my abc's...{/cps}"

    smcs "If she wasn't 8 months pregnant she would've {b}definitely{/b} followed me. {w}Honestly, I decided to take this this trip to {b}escape{/b} from her."
    
    smcs "{cps=50}Mark my words, {w}{cps=350}that woman wants to squeeze another prize-winning story out of me with her own two hands,{w} around my neck.{/cps}"

    smcs "..."

    # sighing sound

    smcs "haaaa...{p}I hope I can write something good soon..."

    scene car_caferoad_bg

    smcs "Ah! {w}That must be the place!"

    smcs "Or... {w} is it? {p}The sign says \"Cafe\", but it looks like the diner in the picture."

    #call screen diner_picture

    smcs "Aren't Cafe and Diner are different things?{p}Might as well stop here and ask."

label parked:

    scene car_parked_bg

    #screen car_inside

    #smcs"Alright, lets go."

    call screen car_door_wait

    smcs"Wait! {w}{b}Can't leave my writing journal!{/b}{p}{cps=350}Pretty sure Miriam would murder me if I did.{/cps}" with vpunch

    smc "{cps=70}But,{/cps}{w=0.5} {cps=60}where did I leave it{/cps}?"

    call screen notebook_object

label name:

    smcs "{cps=150}Brand new{/cps}{w=0.3}{cps=30}... from my grandma's attic.{/cps}{p}Don't you just love the smell of old books?"

    smcs "{cps=150}And I can write{/cps} {w=0.3}{cps=20}{b}anything{/b}{/cps}{w=0.5} in this bad boy{w=1.0}{cps=40}- or girl?{/cps} {p=0.8}{cps=80}I feel like journals are girls.{/cps}"

    smcs "I should probably start by writing my name here." #on this
    
    call screen notebook_intro

label named:

    $ name = name.strip()

    show screen notebook_people_intro #maybe make it so that you can skip it with the space bar or smthng

    smcs "We're all protagonists of our own story."

    show screen notebook_button with dissolve

    smcs "Now, let's get out of here."

    #stop music fadeout 3.0
    
    call screen car_door

label outside_intro:

    #play music "audio/morning_stroll.wav" if_changed fadein 2.5 volume 0.001

    play music "audio/maintune_og2.wav" if_changed fadein 0.5 volume 1.1

    scene outside_parkinglot_bg
    
    hide screen cat

    hide screen cat_door

    with fade

    if outsidecar_flag == 0:

        smc "Alright."

    else:

        pass

    #play music "audio/maintune_og2.wav" if_changed fadein 0.5 volume 1.1 

    $ outsidecar_flag += 1

    call screen parkinglot_intro

label cars:

    scene outside_backroad_bg

    hide screen cat

    hide screen cat_door

    with fade

    call screen cars

label trash:

    scene outside_backcafe_bg

    if cat_flag == False and cat_object == False:

        show screen cat

        with fade

        $ cat_flag = True
    
    else:

        $ cat_flag = True

        pass

        with fade

    call screen trash

label diner_back:

    scene outside_door_bg

    if cat_flag == True and cat_object == False:

        show screen cat_door

        with fade
    
    else:

        $ cat_flag = False

        pass

        with fade

    $ cat_flag = False

    call screen diner_back

label entrance:

    #stop music

    hide screen cat_door

    play music "audio/maintune_og2.wav" if_changed fadein 0.5 volume 1.1

    $ sitting_dialogue = False


    if entrance_scene == True and entrance_scene_dialogue == False:
        smc "Round and round we go."
        $ entrance_scene_dialogue = True
    else:
        pass

    $ hidePeopleEating()

    if asked_flag == True:
        scene entrance_bg

    else:
        scene entrance_bg
        with fade

    #show screen response

    if ask_flag == False:

        show screen old_lady
        
        smcs "There should be someone I can ask here."

        call screen old_lady

    else:

        show screen old_lady2
        
        call screen middle1


label this_is_it:

    hide screen old_lady

    hide screen old_lady2

    hide screen l_description

    hide screen l2_description

    scene the_bar

    show baristalady at slightleft

    with fade

    $ evening_bl = True
    $ weather_bl = True
    $ how_old = False

label is_it:

    menu:

        "Good evening ma'am!" if evening_bl:

            $ evening_bl = False
            
            sbl "Aweful chirpy, aint you, love?"

            smcs "I try to be!"

            $ lb_affection_points += 1

            jump is_it

        "Horrible weather isn't it?" if weather_bl:

            $ weather_bl = False

            sbl "Say less! My bones are creaking."

            $ lb_affection_points += 1

            jump is_it

        "Is this the diner from the brochure?" if evening_bl and weather_bl:

            #call screen diner_picture

            sbl "Brochure? Show me."

            jump interrogationTutorial

        "May I ask if this is the diner from this brochure?" if evening_bl == False or weather_bl == False:

            #call screen diner_picture

            sbl "A brochure? May I see it?"

            jump interrogationTutorial

    label interrogationTutorial:

        smcs "I should show her the brochure in my bag..."

        hide screen notebook_button

        $ bl_interrogation = True

        call screen interrogation_options

        $ bl_interrogation = False

    label why:

        $ pamphlet_i = False

        menu:
            
            "That's all I need to know.":

                jump this_is_it_done

            "Alright, thank you!":

                jump this_is_it_done

            "You don't seem very happy about it." if how_old == False:

                $ how_old = True
                
                sbl "It was my son's idea, such a darling, {w}he wanted to go to all the way to the city to open up a Cafe."
                
                sbl "{cps=90}{size=+5}But we mom's know what's best for our little ones!{/size}{/cps}"

                sbl "I convinced him to stay here and give this old place a make over!{p}We're currently under reconstruction."
                
                $ cc_dream_info = True

                jump why

            "...how old is your son?" if how_old:

                sbl "21{w},  why do you ask?"

                $ cc_age = True

                jump toxic          
    
    label toxic:

        menu:

            "Maybe it's time you let him spread his wings.":

                $ lb_affection_points -= 2

                sbl "{cps= 200}{b}Awful rude you are.{/b}{/cps}{p=1.0}{cps= 90}You know nothing about me or my son to say such things.{/cps}{w=3.5}{nw}"

                sbl "{cps= 50}I don't want you in my diner{/cps}{nw}"

                sbl "{s}I don't want you in my diner{/s}{cps= 90}- {p=0.2}{size=-10}I mean, {/size}{b}{size=+10}{w=0.5}{space=10}our Cafe{space=10}{/size}{w=0.5} any longer!{/b}{/cps}{w=1.5}{nw}" 
                
                sbl "{size=+5}{k=+10}{b}You know the way out.{/b}{/k}{/size}"

                #sbl "{cps= 90}I mean Cafe,{/cps} you know the way out."

                $ persistent.rudeending = True  

                jump rude_ending

            "You just don't look your age ma'am!":

                $ lb_affection_points += 2

                sbl "{size=+8}{k=+5}Oh you flatterer!{/k}{/size}"

                jump this_is_it_done
            
            "No reason.":

                sbl "Well, then."

                jump this_is_it_done

    label this_is_it_done:

        if lb_affection_points == 0:
            
            sbl "Sit wherever you like.{p}I'll get to you in a moment."

        else:
            
            sbl "Sit wherever you like, sweatheart.{p}I'll get to you in a moment."

    $ bl_name = True

    jump entrance

label middle1:

    $ entrance_scene = True
    $ asked_flag = False

    hide screen old_lady

    hide screen old_lady2

    #if b_dialogue >= 0:
    if b_dialogue:

        scene entrance_middle_bg

    else:

        scene entrance_middle_bg

        with fade

    show screen bm_sitting

    call screen middle2


    label business_dialogue:

        $ albino_attraction_points += 1    
        $ braids_attraction_points -= 1

        hide screen bm_sitting

        show businessman2 at slightleft

        show businessman1  at slightright

        sbm2 "This is an important business meeting."

        $ bm_meeting_info = True

        sbm1 "We would like some privacy."

        if b_dialogue == True:
            pass
        
        else:
            smc "Why would you have a private business meeting in a public cafe?"
            
            $ b_dialogue = True

        jump middle1

label middle2:

    #$ b_dialogue -= 1
    $ b_dialogue = False

    scene exit_middle_bg 

    hide screen bm_sitting

    with fade
    
    if walkback_flag:
        pass
    else:
        smc "A 180 and a walk back..."

    call screen exit

label hallway_intro:

    scene hallway_intro 

    hide screen bm_sitting

    hide screen cat

    hide screen trash

    with fade
    
    if freedom_flag == False and hallway_intro == False:
        smc "I don't think the hallway floor was included in the \"wherever\" she said I could sit, {p} or do I suddenly need to use the restroom?"
        $ hallway_intro = True
    else:
        pass
    call screen hallway

label kitchen:

    scene kitchen with fade

    if freedom_flag == False:
        smc "Just having a looksie, because I'm definitely {b}not{/b} supposed to go in there."
        $ kitchen_intro = True
    else:
        pass

    call screen kitchen

label restroom:

    if freedom_flag == False and restroom_intro == False:
        smc "Well here I am. {p}I don't suppose they'll bring me my coffee to the restroom, right?"
        $ restroom_intro = True
    else:
        pass

    scene restroom with fade

    call screen restroom

label exit:

    $ walkback_flag = True

    if sitting_dialogue:

        scene exit_bg

    else:

        scene exit_bg
        with fade 

    show screen doctor_sitting

    show screen prettygirl_sitting

    show screen brokenstool

    show screen gg_sitting

    if click_flag == 0:

        smc "Hadn't noticed that guy sitting there before."  
    else:
        pass

    call screen entrance

    label broken_dialogue:

        scene exit_bg

        $ sitting_dialogue = True
        $ click_flag += 1

        show screen brokenstool

        sbl "Sorry, hun, that stool is broken."
        
        smc "Noted."

        jump exit

    label pg_dialogue:

        scene exit_bg

        $ sitting_dialogue = True
        $ click_flag += 1
        #$ click_flag = True
        show screen prettygirl_sitting

        spg  "..."

        smc  "Whats her deal?"

        jump exit


    label gg_dialogue:

        scene exit_bg

        $ sitting_dialogue = True
        $ click_flag += 1
        #$ click_flag = True

        show screen gg_sitting

        smc "..."

        jump exit

label doctor_intro: 

    $ click_flag += 1
    #$ click_flag = True

    $ hidePeopleEating()  

    hide screen interrogation_leave

    #hide screen notebook_button

    hide screen d_description

    scene doctor_seat

    show doctor at sitting
    
    with fade

    smc "Another booth, another probable rejection..."
    
    menu:

        smc "Another booth, another probable rejection..."

        "Mind if I sit with you?":
            
            d "Not at all, make yourself comfortable."

        "Is this side available?":

            d "It is, make yourself comfortable."

    label doctor_done:

    smcs "Thank you!"

    d "Of course."

    ## should have screen to click on book and comic-like scenes that show a close up so she can realize it's her book.

    smc "!!!"

    smc "He's holding my novel!"

    smc "Should I say something?"

    $ novel_quiet = True 
    $ novel_stare = True

    label say_something:

        menu:

            "What are you reading?":    

                $ d_attraction_points += 1

                d "This?{w} Glad you asked!"

                d "The novel's titled -Atonement of the Moon-.{p}It's the best mystery I've ever read."

                d "My brother bought it for me five years ago, and I have brought it with me on every long trip since then."
                
                d "Supposedly the author was in highschool when she wrote this,{p}and had plans of joining the police force right after."

                d "But aside from that, there is nothing much known about her.{p}The novel doesn't even have her portrait."
                
                d "The name's probably an allias too. Written by \"L. Mendez\"."

                smc "{cps=90}\"Lucky\", {w=0.2}it's my middle name.{/cps} {w}[name] Lucky Mendez.{p}{b}I hate it,{/b} but I feel it suits me."

                jump novel_ask  

            "(Keep quiet.)" if novel_quiet:

                $ novel_quiet = False 

                smc "Better not..."

                jump storm

            "(Keep quiet.)" if novel_quiet == False:

                d "{cps=20}...alright...{/cps}"

                $ d_attraction_points -= 2

                jump storm
            
            "(Stare.)" if novel_stare:

                $ novel_stare = False
                $ novel_quiet = False 

                d "..." 
            
                d "Is something the matter?"

                jump say_something

    label novel_ask:

        $ novel_what = True
        $ novel_like = True
        $ novel_ending = True

    label novel_questions:

        menu:
            
            "What's the novel about?" if novel_what:

                $ novel_what = False

                d "Four friends in a small countryside town find a dead stranger in an abandoned barn."
            
                d "They go around interrogating their neighbors, while trying not to let on that they know about the murder."

                jump novel_questions

            "What did you like about it?" if novel_like:

                $ novel_like = False

                d "That it's not really about the mystery, {w}it's about the relationships between the characters."

                d "{cps=100}And you'd never guess who the culpri{/cps}—{w=0.5} ah,{w=0.2} {cps=100}sorry. {w=2}Spoilers.{/cps}"

                jump novel_questions

            "What did you think of the ending?" if novel_ending:

                $ novel_ending = False

                d "I didn't really expect it, {w}but all the clues where there.{p}I'm really looking forward to her next work."

                smc "{cps=40}...{w}we all are.{/cps}"

                d "I guess she must be a cop by now or maybe a full fledged doctor."

                smcs "She isn't."

                if d_attraction_points >= 1:

                    d "Sorry?"
                
                else:

                    d "Pardon?"

                smc "Oh no! Did I say that out loud?{p}{cps=150}This is what happens when you have an internal monologue!{/cps}" with hpunch

                #smc "This is what happens when you have an internal monologue in your head!"

                smcs "Um..."

                jump novel_ending

        label novel_ending:

            menu:

                "Tell him.":

                    smcs "She didn't pass the final exam. Health problems, or such." ###I feel like changing this, sounds dumb.

                    jump tell_him

                "Don't tell him.":

                    smcs "She wrote a hit novel in her teens.{p}Why would she risk a career as an award-winning author?"

                    d "Maybe so."

                    jump storm
        
        label tell_him:
            
            d "Hmm...{w} You seem to know more than you let on, {w=0.7}{cps=150}could it be...{/cps}"

            smc "He can't possibly guess it, right?"

            d "{w=0.3}{cps=130}Are you actually a fan of the author?{/cps}" #with vpunch 

            smc "{cps=50}Phew!{/cps}"

            menu:
                    
                "\"Fan\" isn't the word I would use.":

                    $ d_attraction_points -= 1

                    d "{cps=20}I see... {w=0.6}Then?{/cps}"

                    smcs "I'm-"
                    
                    #I hope my recommendation is sufficient for you to give it a read someday.

                    jump storm

                "Actually, yes.":

                    $ d_attraction_points += 2

                    d "Fantastic! {w}A pleasure meeting you." 

                    smcs "Likewise. {w}I'm-"

                    jump storm                    

                "I just wanted to get to know you.":

                    #probs change this option

                    $ d_attraction_points += 1

                    d "Oh! {w}I see..." #blushing or happy

                    jump storm

#label novel:

label doctor_after:
    
    scene doctor_seat

    show screen notebook_button  
    #show screen test 

    show doctor at sitting


    d "That was wild."

    smcs "Sure was."

    jump storm 

label storm:

    $ act = 1

    #music change

    scene blackout

    hide doctor at sitting

    with flash     

    stop music

    play sound click #should be thunder sound

    #blackout
    #scene of him holding her hand
    #scene of outside the diner in darkness
    #steps
    #scream
    #thud
    #grunt
    #sliding metal

    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" with hpunch

    "{b}AHHHHHHHHHHHHHHHHHHHHHHH!!!{/b}" with hpunch

    u "{cps=150}Remain calm everyone.{p}The backup generator will start up in a few seconds.{/cps}"

label murder1:

    scene entrance_bg

    #scene body_floor

    "" #pretty girl murdered

    u "{b}AHHHHHHHHHHHHHHHHHHHHHHH!!!{/b}" with vpunch

    u "{b}How did this happen??{/b}" with vpunch

    u "{b}Who did this??{/b}" with vpunch

    u "{b}Someone call the police!!{/b}" with vpunch

    # it'd be pretty cool if the text got bigger and bigger with each scream

    sd "Everyone stay right where you are!" with hpunch

    #cooler animation or smtin is in order up here

    scene diner_lowangle_bg

    with fade

    ""

    sd "{b}{w=0.1}.  {w=0.4}.  {w=0.4}.{/b}"

    # he goes to the body and takes pulse

    #sbl "What is going on here?"

    scene exit_bg

    hide doctor

    show doctor

    with fade

    play music "audio/restingsuspicion.wav" fadein 0.5

    $ dd_name = True
    $ d_fear = False #take out later

    d "I'm doctor Jay Wallace from the FBI.{p}Everyone here is under investigation from this moment on."

    # show cop id
    
    d "There's no cell reception here, so I will ask all of you to remain seated, until further notice."

    scene entrance_middle_bg

    show lovebirdgirl
    show lovebirdguy at slightleft 

    lbgirl "What do you mean remain seated???{p}My boyfriend has blood splattered all over his clothes!!" with hpunch

    #show lovebirdguy at center 
    #show lovebirdgirl at slightright 

    #with ease
    
    #lbguy "I'd like to at least wash up, please."

    hide lovebirdgirl
    hide lovebirdguy
    show baristalady

    bl "Such a young life taken so soon...{p}I need to sit down." with hpunch

    hide baristalady
    show businessman2

    bm2 "Ugh, this is terrifying,{p}I don't want to be anywhere near a corpse." with hpunch

    hide businessman2 
    show businessman1 at newcenter

    bm1 "It's certainly difficult to be so near a murder scene.{p}More so when the murderer is in the room with us." with hpunch
    ## idk if to change the second part of this dialogue, it sounds odd and unnecessary.
    hide businessman1
    show cutecook

    cc "This is no good for business...{p}Can I at least mop up?" with hpunch  

    hide cutecook
    show bb_neutral #badboy

    bb "{b}I swear it wasn't me!{/b}{p}What kind of sick person would do something like this???" with hpunch   

    hide bb_neutral
    show gentlegiant

    gg "{w}................................................................................................" with hpunch
    #gg "She was alive just moments before...{p}....................................." with hpunch

    scene exit_bg

    hide gentlegiant 
    show player

    with fade

    mc "...{w}{cps=50}I don't know what to say.{/cps}"

    show player at completeleft with ease
    show doctor 

    d "Everyone place their ids and car keys on the table.{p}No one will leave any time soon."

    #menu:

    #    "Put them on the table.":
            #animate everyone's ids and cards on table
    #        pass

    smc "Believe it or not, I think I threw my things in between the pages of the notebook... "
    
    $ keys_object = True

    call screen notebook_button

label ids:

    scene entrance_bg with fade

    #animate doctor taking mc's id

    sd "..."

    scene exit_bg
    show doctor
    with fade

    d "May I talk to you for a moment?"

    menu:

        "Of course...":

            jump author

        "I didn't do it.":

            d "I believe you,{w} come with me."

            jump author

label author:

    scene doctor_seat

    show doctor at sitting
    
    with fade

    d "So...{p}[name] L. Mendez?"

    smcs "{cps=50}...{w}yes.{/cps}"

    d "Any relation to the author?"

    smcs "{cps=50}...{w}{/cps}"

    menu:

        smcs "..."

        "I am her.":
            pass
        
        "She is me.":
            pass

    #smcs "Yes,{w} I'm the author of Atonement of th Moon."

    d "Anyway to prove it?"

    $ objects_notebook = True
    #$ businesscard = True

    smc "...{w}{cps=150}I'm sure I left my business card between the pages of my journal...{/cps}"

    $ businesscard_object = True

    hide screen notebook_button
    call screen notebook_button

label businesscard:

    hide screen notebook_button
    # animation?
    show screen notebook_button

    $ d_attraction_points += 5

    d "...{p}{cps=150}So its true...{w} {cps=80}Miss Mendez, {w=0.5}I have a favor to ask of you.{/cps}"

    d "I have mustered enough bravado to control the situation,{p}but the truth is I'm in the lasts of my strenghts."

    menu:

        "What do you mean?":
            pass

    d "I-"

    show doctor at sitting with flash

    # animation of him scared

    $ d_fear = True

    d "...{p}As you can see,{w} I don't do well with thunderstorms."

    $ fear_how = True

label fears:

    menu:

        "What does that have to do with me?":
            $ d_attraction_points -= 3
            d "{cps=10}...{w=0.5}{cps=100}they do say never to meet your heroes..{/cps}."
            jump doctor
        
        "What can I do to help?":
            jump doctor
                
        "May I ask, how that happened?" if fear_how:

            $ fear_how = False

            if d_attraction_points >= 8:
                $ d_fear_revealed = True
                d "It's an old wound from my childhood,{w} of no importance at the moment."
                jump fears

            else:
                $ d_fear_revealed = False #delete later
                d "It's of no importance at the moment."
                jump fears
    
    label doctor:

        d "I need you to investigate this case in my place."

        play music "audio/maintune_happy2.wav"

        smcs "{b}What???{/b}" with hpunch

        d "{cps=150}A small diner, {w}one quick murder,{w} 8 suspects,{w} no cell reception.{/cps}"
        
        d "{cps=200}If there's anyone that kind find the truth, it's the mystery novelist with police training and a background in criminal studies.{/cps}"

        menu:

            "How do you know I'm not the murderer?":

                pass

            "Alright, leave it to me.":

                d "My thanks, {w}and my apologies for relaying my responsabilities on to you."

                d "Please take a look at the id cards on the table to help identify everyone."

                call screen leave_doctor

        d "We were both seated the farthest from where the incident took place, time-wise it would have taken you a longer time to stand up,"
        
        d "stab the victim, and sit back down, than the amount of time the lights were out.{w} {b}{cps=150}Plus I was holding your hand the entire time.{/cps}{/b}"

        d "I also heard you asking the ma'am if this was the establishment you were looking for,{w} you weren't even sure where you were."

        d "While neither you nor the victim seemed to recognized or acknowledged each other in anyway."

        d "This was more planned than that. {p}Crimes of passion rarely ever have such precise timing."

        d "And-"

        d "Whoa!" with flash #maybe so maybe not

        #animation?

        d "{w=0.5}{cps=80}...sorry about that{cps=8}...{/cps}"

        menu:

            "Alright, leave it to me.":

                d "My thanks, {w}and my apologies for relaying my responsabilities on to you."

                d "Please take a look at the id cards on the table to help identify everyone."

                call screen leave_doctor

label idcards_take:

    scene entrance_bg
    hide doctor
    with fade

    smc "Idcards..."

    call screen idcards #these should open up and show the cards
    
label idcards_taken:

    $ cc_name = True
    $ bb_name = True
    $ gg_name = True
    $ bl_name = True
    $ dd_name = True
    $ bm1_name = True
    $ bm2_name = True
    $ lbguy_name = True
    $ lbgirl_name = True
    $ cc_age = True
    $ bb_age = True
    $ gg_age = True
    $ bl_age = True
    $ bm1_age = True
    $ bm2_age = True
    $ lbguy_age = True
    $ lbgirl_age = True

    smc "Alright let me write those down{cps=10}...{/cps}"
    smc "{cps=30}Hmm,{w} {cps=150}I'm missing {b}one{/b} person{w}:{/cps}{/cps} the victim.{p}I should discuss this with doctor Wallace." 

    call screen go_doctor with flash

label identify_body: 

    scene doctor_seat

    show doctor at sitting
        
    with fade

    smcs "Problem.{w} {cps=350}We're missing the victim's id.{/cps}"

    d "{w}You'll have to search the body."
        
    d "I would do it myself,{w} {cps=180}but I think my legs gave out with that last lightning...{/cps}"

    menu:
            
        "I don't think I'm qualified for this.":

            d "You know criminal science, and went through police training.{p}You can do this."

            smcs "Are you sure you're not biased towards me since I'm your favorite author?"

            d "{cps=10}...{/cps}{w}{cps=200}I have the right to remain silent.{/cps}" #laughs

            $ d_attraction_points += 2

            call screen leave_doctor_2

        "Got it.":

            call screen leave_doctor_2
        
label identify_body_2:

    scene entrance_bg
    hide doctor
    with fade

    smcs "I'm so not ready for this."

    call screen deadbody

label deadbody:

    scene diner_lowangle_bg
    with fade

label deadbody_close:
    
    call screen deadbody_close

label deadbody_wound:

    smc "A backstab definitely rules out suicide.{p}Who could've done this?"

    jump deadbody_close

label deadbody_dress:

    if pg_dress:
        smc "I had already noticed this, but her dress looks too expensive to be wearing it to the middle of nowhere."
        smc "Maybe she had been waiting for her date to arrive?{p}No clue how this place could be a popular dating spot,"
        smc "but the love birds over there had seemed very entertained, so I can't rule that out."
        smc "I'll just have to wait and see if a handsome stranger enters the cafe looking for her."
    else:
        $ pg_dress = True
        smc "Her dress looks too expensive to be wearing it to the middle of nowhere."
        smc "Maybe she had been waiting for her date to arrive?{p}No clue how this place could be a popular dating spot,"
        smc "but the love birds over there had seemed very entertained, so I can't rule that out."
        smc "I'll just have to wait and see if a handsome stranger enters the cafe looking for her."
    jump deadbody_close

label deadbody_hands:

    smc "Strange...{p}There's some sort of brown powder on her finger tips."

    $ pg_poison = True

    jump deadbody_close

label deadbody_purse:

    scene entrance_bg
    hide doctor
    with fade

    smc "{cps=100}Wonderful!{w}{/cps} I had always wanted to search through a dead person's belongings{cps=8}...{/cps}"
    
    #smc "{cps=28}Sorry,{w} {cps=150}they do say sarcasm is a trauma response...{/cps}" 

label deadbody_purse_continue:

    call screen deadbody_purse

label deadbody_phone:

    show screen pg_phone_locked

    smcs "The victim's phone."

    jump deadbody_phone_locked

label deadbody_phone_locked:

    smcs "It's locked." with hpunch

    $ pg_phone = True

    hide screen pg_phone_locked

    jump deadbody_purse_continue

label deadbody_sheath:

    $ empty_sheath = True 

    smc "A small empty sheath...{p}Could it possibly fit the knife on her back?"
    smc "Pulling that out would further contaminate the crime scene.{p}So maybe I should put a pin on that..."

    jump deadbody_purse_continue

label deadbody_id:

    $ pg_name = True
    $ pg_age = True

    smc "Got it!"

    #this should automatically open her description page

    smc "I'd had thought she was older, but she was so young{cps=8}...{/cps}"

    smc "What should I do now?"

    call screen middle1

label deadbody_3:
    scene doctor_seat

    show doctor at sitting
        
    with fade

    smcs "..."

    menu:
        
        "What now?":
            d "You'll have to investigate by yourself.{p=0}I can't help you anynmore."
            d "Ask questions.{w} Look for evidence.{p}You have all the authority now."
            #d "You have all the authority now."
            call screen leave_doctor_3

        "I'll leave.":
            jump investigation_starts

label investigation_starts:

    scene entrance_bg
    hide doctor
    with fade

    $ interrogation_start = True

    call screen middle1

label jukebox:

    scene jukebox

    with fade

    call screen jukebox

label jukebox_closeup:
    
    scene jukebox_closeup

    with fade

    call screen jukebox_closeup

    jump jukebox

label jukebox_dagger:

    scene jukebox

    with fade

    show screen dagger_closeup

    smc "Another knife?" with vpunch

    smc "It's so beautiful and intricate.{p}Really more of an expensive dagger than anything else."

    smc "...but how did it get here?"

    hide screen dagger_closeup

    jump jukebox

label investigation_hallway:

    scene hallway

    call screen hallway

label investigation_backdoor:

    if freedom_flag:
        
        #scene dinerback

        pass

    else:
        
        smc "A back door.{w} I guess it leads to the back of the diner."

        jump investigation_hallway

label investigation_restroom:

    scene restroom

    call screen restroom

    with fade

label poison_bottle:

    show screen bottle_closeup

    smc "Brown powder in a small bottle{p=0.5}...what could it be?"
    
    smc "Who am I kidding? {p}This is deffinetly somekind of drug.{w} Which drug is brown though?" with hpunch

    smc "One does come to mind, but I have no test kit for this.{p}Maybe there's someone I can ask."

    hide screen bottle_closeup

    $ poison_bottle = True

    jump investigation_restroom

############################################################ investigation starts ###

label investigation_kitchen:

    $ dd_interrogation = False
    $ bb_interrogation = False
    $ cc_interrogation = False
    $ gg_interrogation = False
    $ albino_interrogation = False
    $ braids_interrogation = False
    $ bl_interrogation = False
    $ lbguy_interrogation = False
    $ lbgirl_interrogation = False

label investigation_bar:

    $ dd_interrogation = False
    $ bb_interrogation = False
    $ cc_interrogation = False
    $ gg_interrogation = False
    $ albino_interrogation = False
    $ braids_interrogation = False
    $ bl_interrogation = False
    $ lbguy_interrogation = False
    $ lbgirl_interrogation = False

    scene coffee_bar
    
    #show screen interrogation_bl
    #show screen interrogation_cc

    call screen bar_interrogation

    with fade

label investigation_middle:

    play music "audio/restingsuspicion.wav" 

    $ dd_interrogation = False
    $ bb_interrogation = False
    $ cc_interrogation = False
    $ gg_interrogation = False
    $ albino_interrogation = False
    $ braids_interrogation = False
    $ bl_interrogation = False
    $ lbguy_interrogation = False
    $ lbgirl_interrogation = False

    scene entrance_middle_bg

    show screen notebook_button

    show screen interrogation_gg
    show screen interrogation_bb
    show screen interrogation_albino
    show screen interrogation_braids
    show screen interrogation_lbguy
    show screen interrogation_lbgirl

    with fade

    ###############################
    $ gg_attraction_points = 0
    $ bb_attraction_points = 0
    $ cc_attraction_points = 0
    $ albino_attraction_points = 0    
    $ braids_attraction_points = 0
    $ lbguy_affection_points = 0
    $ lbgirl_affection_points = 0

    $ dd_closed = False
    ## delete all later ###########

    call screen middle2


label interrogation_gg:

    $ gg_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    show gentlegiant
    
    with fade

    
    if gg_closed:
        gg "(angry)......"
        jump investigation_middle

    else:
        gg "{cps=50}.........................................................................................................{/cps}"

    $ gg_closed = False

    jump interrogation_screen

label interrogation_bb:

    
    $ bb_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()
    
    show bb_neutral #at bbcenter

    with fade    

    hide screen notebook_button

label interrogation_bb_start:

    if bb_closed == True:
        bb "Get out of my face."
        jump investigation_middle

    elif understanding_bb == True:
        bb "Something else?"

    else:
        bb "{b}What do you want?{/b}"

    jump interrogation_screen

label interrogation_cc:

    $ cc_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    show cutecook_closeup

    with fade

    if cc_closed:
   
        cc "Leave me alone."
        jump investigation_bar

    else:

        cc "This is bad for business..."
    
    $ cc_closed = False

    jump interrogation_screen

label interrogation_albino:

    $ albino_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    show businessman2

    with fade

    if albino_closed:
        bm2 "I'll sue you when I get out of here."
        jump investigation_middle
    
    else:
        bm2 "The moment I get out of here I'm suing all of you."
    
    $ albino_closed = False

    jump interrogation_screen

label interrogation_braids:

    $ braids_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    show businessman1 at newcenter

    with fade

    if braids_closed:
        
        bm1"Please, {w}give me time to compose myself."
        jump investigation_middle

    else:
        bm1 "I'll help however I can."

    $ braids_closed = False

    jump interrogation_screen

label interrogation_bl:

    $ bl_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    with fade

    show baristalady with vpunch

    
    if bl_closed:

        bl "Go fix your manners elsewhere."
        jump investigation_bar
    
    else:
        bl "Horrible! This is horrible!" with vpunch

    $ bl_closed = False

    jump interrogation_screen

label interrogation_lbguy:

    $ lbguy_interrogation = True

    scene doctor_seat

    $ hidePeopleInterrogation()

    show lovebirdguy at slightleft
    show lovebirdgirl at slightright

    with fade

    if lbgirl_closed or lbguy_closed == True:
        
        lbguy "Leave us alone."
        jump investigation_middle

    else:
        lbgirl "This is all very disturbing."

    $ lbgirl_closed = False
    $ lbguy_closed = False

    jump interrogation_screen

label interrogation_lbgirl:

    $ lbgirl_interrogation = True

    scene doctor_seat 

    $ hidePeopleInterrogation()

    show lovebirdguy at slightleft
    show lovebirdgirl at slightright

    with fade

    if lbgirl_closed or lbguy_closed == True:
        
        lbgirl "Leave us alone."
        jump investigation_middle

    else:
        lbgirl "This is all very disturbing."

    $ lbgirl_closed = False
    $ lbguy_closed = False
    
    jump interrogation_screen


## interrogation stuff ##

label objects_interrogation: 
    
    $ level = 1

    $ objectsInterrogation(act, level, businesscard_i, pamphlet_i, clover_i, umbrella_i, mc_keys, shovel_i, pg_phone_i, pg_picture_i, charger_i, old_picture_i, note_i, cat_object_i, keys_object_i, wirecutters_i, businesscard_bm2_i, hunting_knife_i, empty_sheath_i, poison_bottle_i, dagger_i, sheathed_dagger_i, peanutbutter_i, sardines, cat_accessory_1_i, cat_accessory_2_i, dd_interrogation, bb_interrogation, gg_interrogation, cc_interrogation, albino_interrogation, braids_interrogation, bl_interrogation, lbguy_interrogation, lbgirl_interrogation)

    $ businesscard_i = False
    $ pamphlet_i = False
    $ clover_i = False
    $ mc_keys_i = False
    $ umbrella_i = False    
    $ shovel_i = False
    $ pg_phone_i = True
    $ pg_picture_i = False
    $ charger_i = False     
    $ old_picture_i = False
    $ note_i = False
    $ cat_object_i = False   
    $ keys_object_i = False
    $ wirecutters_i = False
    $ businesscard_bm2_i = False
    $ hunting_knife_i = False
    $ empty_sheath_i = False
    $ poison_bottle_i = False
    $ dagger_i = False
    $ sheathed_dagger_i = False
    $ peanutbutter_i = False     
    $ sardines_i = False          
    $ cat_accessory_1_i = False   
    $ cat_accessory_2_i = False 

    call screen objects_interrogation 


label interrogation_screen:

    hide screen notebook_button ### temporary

    $ people_mc = False
    $ people_dd = False
    $ people_bb = False
    $ people_gg = False
    $ people_cc = False
    $ people_pg = False
    $ people_albino = False
    $ people_braids = False
    $ people_bl = False
    $ people_lbguy = False
    $ people_lbgirl = False

    call screen interrogation_options

label people_interrogation:

    $ peopleInterrogation(act, level, people_mc, people_dd, people_bb, people_gg, people_cc, people_pg, people_albino, people_braids, people_bl, people_lbguy, people_lbgirl, dd_interrogation, bb_interrogation, gg_interrogation, cc_interrogation, albino_interrogation, braids_interrogation, bl_interrogation, lbguy_interrogation, lbgirl_interrogation)

    $ people_mc = False
    $ people_dd = False
    $ people_bb = False
    $ people_cc = False
    $ people_gg = False
    $ people_albino = False
    $ people_braids = False
    $ people_bl = False
    $ people_lbguy = False
    $ people_lbgirl = False
    
    call screen people_interrogation

label interrogation_questions:

    if bb_interrogation == True:

        menu:

            "Where were you when the incident happened?" if where_bb:
                $ where_bb = False
                $ unusual_bb = True
                jump where_bb

            "Did you see anything out of the usual?" if unusual_bb:
                $ unusual_bb = False
                jump unusual_bb
                    
            "What's up your butt?" if butt_bb == True and understanding_bb == False :
                $ butt_bb = False
                jump butt_bb

            "I want to get to know you better." if know_bb:
                $ know_bb = False
                jump know_bb  

            "Nevermind." if understanding_bb == False:
                jump interrogation_screen

            "Thank you for your cooperation." if understanding_bb:
                bb "Well, it was alright."
                jump interrogation_screen

    #jump interrogation_bb

    label where_bb:

        bb "Didn't you see me?{w} {cps=150}I was sitting right in this booth.{/cps}"

        jump interrogation_questions

    label unusual_bb:

        if bm_meeting_info == True and understanding_bb == False:
            bb "{cps=120}Aside from you asking everyone for a seat?{/cps}{p}No.{w=0.4} {cps=60}I wasn't really paying attention.{/cps}"
        elif understanding_bb:
            bb "Just normal people in a cafe doing normal cafe people things."
        else:
            bb "Not really.{w} {cps=150}Wasn't really paying attention.{/cps}"

        jump interrogation_questions

    label butt_bb: 

        $ bb_attraction_points -= 1

        bb "Nothing, what's up yours?"

        smc "It's like talking to a child..."

        smcs "{cps=150}...forget it.{/cps}"

        jump interrogation_questions

    ### use later in the game ###
    label know_bb:

        bb "For better interrogation?"

        menu:
                
            "Of course.":

                $ bb_attraction_points -= 2
                
                bb "Get out of my face."

                $ bb_closed = True

                jump investigation_middle

            "To understand you better.":

                $ understanding_bb = True

                $ bb_attraction_points += 2

                bb "{cps=20}Hmmmm...{/cps}" 

                bb "I like music?"

                smcs "What kind?"

                bb "Classical."

                smc "That's unexpected."

                bb "I know what you might be thinking:{p}I'd look out of place in a concert hall,{w} but music doesn't discriminate."

                bb "Many composers were the punks of their time,{w} the same could be said for Shakespeare, Dostoevsky and other authors."

                smcs "So you also like literature?"
 
                bb "Yes!{w} Once you read a good book, it stays with you forever." 

                smcs "I agree!"

                $ bb_interests = True

                jump interrogation_questions

#label investigation_restroom







    

    
##

label end:

    scene diner_lowangle_bg
    #with fade

    hide player

    #hide screen test
    hide screen notebook_button 
    hide screen qmenu_button

    with fade

    smcs "so they were the killer all along!"

    smcs "...the more you know."

    scene blackout
    with fade 

label rude_ending:

    hide baristalady

    if persistent.rudeending == True:

        call screen rude_ending

    else:
        pass

    


##
    return
