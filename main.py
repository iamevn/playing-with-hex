#!/usr/bin/env python3

import curses, random
from board import board
import pieces

def main(stdscr):
    h = board()
    class Data:
        pass
    cursor = Data()
    cursor.focus = 0 # 0: board, 1: pwins
    cursor.pwin = 0 # 0: pwin1, 1: pwin2, 2: pwin3
    cursor.q = 0
    cursor.r = 0

    dispframe = stdscr.subwin(11, 19, 0, 0)
    dispframe.box()
    displaywin = dispframe.subwin(10, 18, 1, 1)
    stdscr.addstr(0, 22,  "u i")
    stdscr.addstr(1, 21, "h   k")
    stdscr.addstr(2, 22,  "n m")

    piecesframe = stdscr.subwin(6, 28, 11, 0)
    piecesframe.box()
    pieceswin = piecesframe.subwin(4, 26, 12, 1)
    pieceswin.vline(0, 8, curses.ACS_VLINE, 4)
    pieceswin.vline(0, 17, curses.ACS_VLINE, 4)
    pwin1 = pieceswin.subwin(4, 8, 12, 1)
    pwin2 = pieceswin.subwin(4, 8, 12, 10)
    pwin3 = pieceswin.subwin(4, 8, 12, 19)
    pwins = [pwin1, pwin2, pwin3]
    stored = [pieces.randompiece(), pieces.randompiece(), pieces.randompiece()]

    def refresh_pwin(i):
        w = pwins[i]
        w.clear()
        pieces.draw(stored[i], w)
        w.refresh()

    refresh_pwin(0)
    refresh_pwin(1)
    refresh_pwin(2)

    done = False
    key = ''
    while not done:
        if key == 'q':
            done = True
            break
        elif key == '\t':
            cursor.focus = (cursor.focus + 1) % 2

        elif cursor.focus == 0:
            if key == 'u':
                if h.isValid(cursor.q, cursor.r - 1):
                    cursor.r -= 1
            if key == 'i':
                if h.isValid(cursor.q + 1, cursor.r - 1):
                    cursor.q += 1
                    cursor.r -= 1
            if key == 'h':
                if h.isValid(cursor.q - 1, cursor.r):
                    cursor.q -= 1
            if key == 'k':
                if h.isValid(cursor.q + 1, cursor.r):
                    cursor.q += 1
            if key == 'n':
                if h.isValid(cursor.q - 1, cursor.r + 1):
                    cursor.q -= 1
                    cursor.r += 1
            if key == 'm':
                if h.isValid(cursor.q, cursor.r + 1):
                    cursor.r += 1
            elif key == ' ':
                h.invert(cursor.q, cursor.r)
                h.clearLines()
            elif key in ['1', '2', '3']:
                chosen = int(key) - 1
                chpiece = stored[chosen]
                if h.can_place(cursor.q, cursor.r, chpiece):
                    h.place(cursor.q, cursor.r, chpiece)
                    stored[chosen] = pieces.randompiece()
                    refresh_pwin(chosen)
                    h.clearLines()

            # stored[cursor.pwin] = pieces.randompiece()
            # refresh_pwin(cursor.pwin)
            else:
                stdscr.addstr(19,0,key)
                stdscr.clrtoeol()
        elif key == 'h' or key == 'KEY_LEFT':
            cursor.pwin = (cursor.pwin - 1) % 3
        elif key == 'l' or key == 'KEY_RIGHT':
            cursor.pwin = (cursor.pwin + 1) % 3
        elif key == 'j' or key == 'KEY_DOWN':
            stored[cursor.pwin] = (stored[cursor.pwin] + 1) % len(pieces.plist)
            refresh_pwin(cursor.pwin)
        elif key == 'k' or key == 'KEY_UP':
            stored[cursor.pwin] = (stored[cursor.pwin] - 1) % len(pieces.plist)
            refresh_pwin(cursor.pwin)
        elif key == 'r':
            # randomize piece
            stored[cursor.pwin] = pieces.randompiece()
            refresh_pwin(cursor.pwin)
        else:
            stdscr.addstr(19,0,key)
            stdscr.clrtoeol()

        h.draw(displaywin)
        displaywin.move(*h.grid2screen(cursor.q, cursor.r))

        stdscr.refresh()

        dispframe.refresh()
        displaywin.refresh()
        piecesframe.refresh()
        pieceswin.refresh()

        if cursor.focus == 0:
            displaywin.refresh()
        else:
            pwins[cursor.pwin].move(3, 7)
            pwins[cursor.pwin].refresh()

        key = stdscr.getkey()
    
curses.wrapper(main)
