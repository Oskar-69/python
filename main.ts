function bob() {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .`)
}

function mary() {
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #`)
}

basic.forever(function thingy() {
    bob()
    mary()
})
