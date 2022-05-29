
screen info_panel:
    frame:
        padding (10, 10)
        vbox:
            text "Персонажи могут быть не натуралами!"

screen dengi:
    frame:
        xalign 0.99
        padding (15, 10)
        vbox:
            text "Денег:[dengi]"

screen rep:
    frame:
        xalign 0.85
        padding (15, 10)
        vbox:
            text "Репутация:[reputation]"
# Игра начинается здесь:
label start:
    $ dengi = 0
    $ reputation = 10
    show screen info_panel with dissolve
    show screen dengi with dissolve
    show screen rep with dissolve
    stop music fadeout 2.5
    agil "Бля, я долбаёб?"
    hide screen info_panel with dissolve
    play music losbiblicos2 fadein 1.0
    scene bg anime 1 with dissolve
    show 3kuznik pokerface with dissolve:
        xalign 0.5
        yalign 0.1
    islam "Здравствуйте. Вы готовы сделать заказ?"
    hide 3kuznik
    show 3kuznik pokerface with dissolve:
        xalign 0.9
        yalign 0.1

    show jahid normal with dissolve:
        xalign 0.1
        yalign 0.1
    djahid "Мне пожалуйста чашечку кофе и кусок французского сыра."
    islam "Сию минуту, сэр."
    hide 3kuznik pokerface with pixellate
    pause 1.0
    show 3kuznik pokerface with dissolve:
        xalign 0.9
        yalign 0.1
    islam "Вот ваш заказ, сэр."
    show agilpng normal with dissolve:
        xalign 0.5
        yalign 0.1
    agil "Прошу меня извинить, не могу ли я себе позволить спиздить ваш сыр, господин Джахид?"
    djahid "Прошу вас пойти нахуй. Благодарю."
    show uzbekpng normal with dissolve:
        xalign 1.8
        yalign 0.1
    uzbek "Никто не хочет немного узбекского плова, дамы и господа?"
    scene bg anime 1 with fade
    show uzbekpng normal with dissolve:
        xalign 1.8
        yalign 0.1
    uzbek "Вкусный, только что заварил. Ыыэыээыэыыэ *пингует*."
    show agilpng normal with dissolve:
        xalign 0.0
        yalign 0.1
        zoom 0.8
    agil "Мне кажется сей господин должен соизволить провести себе норм интернет."
    uzbek "А, да?"
    show 3kuznik normal at left:
        yalign 0.1
    islam "Нет."
    scene bg anime 1 with fade
    show 3kuznik normal at left:
        yalign 0.1
    islam "Бля, как же хочется снять тикток, вы не представляете."
    menu:
        "Дать леща":
            $ reputation = reputation + 10
            $ dengi = dengi - 10
            "..."
            "Я смачно въебал лещанского тиктокеру. Ну а хули, что я терпеть должен вечно?"
        "Стерпеть выходку":
            $ reputation = reputation - 10
            $ dengi = dengi + 15
            "..."
            "Я всё-таки стерпел очередной высер тиктокера."
            jump situation1


    return
