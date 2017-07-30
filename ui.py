#!/usr/bin/env python3

import curses
from board import board

def main(stdscr):
    h = board()
    class Data:
        pass
    cursor = Data()
    cursor.q = 0
    cursor.r = 0

    dispframe = stdscr.subwin(11, 19, 0, 0)
    dispframe.box()
    displaywin = dispframe.subwin(10, 18, 1, 1)

    piecesframe = stdscr.subwin(6, 28, 11, 0)
    piecesframe.box()
    pieceswin = piecesframe.subwin(4, 26, 12, 1)
    pieceswin.vline(0, 8, curses.ACS_VLINE, 4)
    pieceswin.vline(0, 17, curses.ACS_VLINE, 4)
    pwin1 = pieceswin.subwin(4, 7, 12, 1)
    pwin2 = pieceswin.subwin(4, 7, 12, 10)
    pwin3 = pieceswin.subwin(4, 7, 12, 19)
    pwins = [pwin1, pwin2, pwin3]
    focusedpiece = 0

    mainfocused = True

    done = False
    key = ''
    while not done:
        if key == 'q':
            done = True
            break
        elif key == '\t':
            mainfocused = not mainfocused
        elif mainfocused:
            if key == 'h' or key == 'KEY_LEFT':
                if h.isValid(cursor.q - 1, cursor.r):
                    cursor.q -= 1
            elif key == 'j' or key == 'KEY_DOWN':
                if h.isValid(cursor.q, cursor.r + 1):
                    cursor.r += 1
            elif key == 'k' or key == 'KEY_UP':
                if h.isValid(cursor.q, cursor.r - 1):
                    cursor.r -= 1
            elif key == 'l' or key == 'KEY_RIGHT':
                if h.isValid(cursor.q + 1, cursor.r):
                    cursor.q += 1
            elif key == ' ':
                h.invert(cursor.q, cursor.r)
            elif key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                h.toggle(cursor.q, cursor.r, int(key))
            else:
                stdscr.addstr(19,0,key)
                stdscr.clrtoeol()
        elif key == 'h' or key == 'KEY_LEFT':
            focusedpiece = (focusedpiece - 1) % 3
        elif key == 'l' or key == 'KEY_RIGHT':
            focusedpiece = (focusedpiece + 1) % 3
        else:
            stdscr.addstr(19,0,key)
            stdscr.clrtoeol()

        h.draw(displaywin)
        displaywin.move(*h.grid2screen(cursor.q, cursor.r))

        stdscr.refresh()
        if mainfocused:
            dispframe.refresh()
            displaywin.refresh()
        else:
            piecesframe.refresh()
            pieceswin.refresh()
            pwins[focusedpiece].refresh()


        key = stdscr.getkey()
    

curses.wrapper(main)
