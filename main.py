def bob():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .""")

def mary():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #""")

def thingy():
    bob()
    mary()

basic.forever(thingy) #Do the function thingy() FOREVER...