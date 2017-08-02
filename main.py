#!/usr/bin/env python3

import curses, random
from board import Board
from solver import best_placement
import pieces

def main(stdscr):
    h = Board()
    class Data:
        pass
    cursor = Data()
    cursor.focus = 0 # 0: board, 1: pwins
    cursor.pwin = 0 # 0: pwin1, 1: pwin2, 2: pwin3
    cursor.q = 0
    cursor.r = 0
    best = None

    dispframe = stdscr.subwin(11, 19, 0, 0)
    dispframe.box()
    displaywin = dispframe.subwin(10, 18, 1, 1)
    stdscr.addstr(0, 22,  "u i")
    stdscr.addstr(1, 21, "h   k")
    stdscr.addstr(2, 22,  "n m")

    f= Data()
    f.pheight = 4
    f.pwidth = 10
    f.originy = 12
    f.originx = 1
    piecesframe = stdscr.subwin(f.pheight + 2, 3 * f.pwidth + 4, f.originy - 1, f.originx - 1)
    piecesframe.box()
    pieceswin = piecesframe.subwin(f.pheight, 3 * f.pwidth + 2, f.originy, f.originx)
    pieceswin.vline(0, f.pwidth, curses.ACS_VLINE, f.pheight)
    pieceswin.vline(0, 2 * f.pwidth + 1, curses.ACS_VLINE, f.pheight)
    pwin1 = pieceswin.subwin(f.pheight, f.pwidth, f.originy, f.originx)
    pwin2 = pieceswin.subwin(f.pheight, f.pwidth, f.originy, f.originx + f.pwidth + 1)
    pwin3 = pieceswin.subwin(f.pheight, f.pwidth, f.originy, f.originx + 2 * f.pwidth + 2)
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
        elif key == 'b':
            best = best_placement(h, stored)
            if best:
                h.highlight(*best["coord"], best["piece"])
        elif key == 'c':
            # if not best:
            #     best = best_placement(h, stored)
            #     h.highlight(*best["coord"], best["piece"])
            if best:
                h.place(*best["coord"], best["piece"])
                stored.remove(best["piece"])
                stored.append(pieces.randompiece())
                refresh_pwin(0)
                refresh_pwin(1)
                refresh_pwin(2)
                h.clearLines()
                # focus incoming piece for ease of use
                cursor.focus = 1
                cursor.pwin = 2
                best = None
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
                    h.highlight(cursor.q, cursor.r, chpiece)
                    # stored "falls" to the left like in actual game
                    stored.pop(chosen)
                    stored.append(pieces.randompiece())
                    refresh_pwin(0)
                    refresh_pwin(1)
                    refresh_pwin(2)
                    h.clearLines()
                    # focus incoming piece for ease of use
                    cursor.focus = 1
                    cursor.pwin = 2
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
