#!/usr/bin/env python3

from math import floor

class board:
    def __init__(self, width=9):
        """initialize to an empty hex board
           (using Axial coordinate system from
           http://www.redblobgames.com/grids/hexagons/#coordinates 
           with 0,0 in the middle, 0,floor(width/2) in bottom right,
           and floor(width/2),0 on far right)"""
        if width % 2 == 0:
            raise ValueError("width({}) must be odd".format(width))
        # when r is -4, q goes from 0 to 4
        # when r is 0, q goes from -4 to 4
        # when r is 4, q goes from -4 to 0
        self.spaces = {}
        self.width = width
        self.halfwidth = floor(width / 2)
        hw = self.halfwidth
        for r in range(-hw, hw + 1):
            if r < 0:
                qmin = -hw - r
                qmax = hw
            else:
                qmin = -hw
                qmax = hw - r
            for q in range(qmin, qmax + 1):
                self.spaces[q, r] = 0

    def get(self, q, r):
        """"returns current value at q,r coord (may raise KeyError on invalid q/r)"""
        return self.spaces[q, r]

    def set(self, q, r, val):
        """"sets q,r coord to val (may raise KeyError on invalid q/r)"""
        if not (q, r) in self.spaces:
            raise KeyError("({}, {}) not in range".format(q, r))
        self.spaces[q, r] = val

    def clear(self, q, r):
        """sets q,r coord to 0 (may raise KeyError on invalid q/r)"""
        self.set(q, r, 0)

    def invert(self, q, r):
        """sets q,r coord to arithmetic not its current value"""
        self.toggle(q, r, 1)
    def toggle(self, q, r, val):
        if self.get(q, r) != val:
            self.set(q, r, val)
        else:
            self.set(q, r, 0)

    def isValid(self, q, r):
        """True if q,r is in hexagon"""
        return (q, r) in self.spaces

    def grid2screen(self, q, r):
        """given a q and an r, return y,x coordinates for that q and r
        0,0 is the y,x coordinate at the top left outside the hexagon,
        each spot is separated horizontally by a space"""
        y = r + self.halfwidth
        x = ((q + self.halfwidth) * 2) + y - self.halfwidth
        return y, x

    def screen2grid(self, y, x):
        """inverse of grid2screen"""
        q = ((x - y + self.halfwidth) / 2) - self.halfwidth
        r = y - self.halfwidth
        return q, r

    def draw(self, scr):
        chars = ['.', '#', 'O', '+', '*', '@', '$', '%', 'X', ' ']
        for q, r in self.spaces.keys():
            y, x = self.grid2screen(q, r)

            scr.addch(y, x, ord(chars[self.spaces[q, r]]))

    def can_place(self, q, r, piece):
        for (pq, pr) in piece:
            if not self.isValid(q + pq, r + pr):
                return False
            if self.get(q + pq, r + pr) != '.':
                return False
        return True

    def place(self, q, r, piece, val='.'):
        if self.can_place(q, r, piece):
            for (pq, pr) in piece:
                self.set(q + pq, r + pr, val)

    def clearLines(self):
        """check for any completed lines and clear them,
        return how many lines cleared"""
        hw = self.halfwidth
        for r in range(-hw, hw + 1):
            if r < 0:
                qmin = -hw - r
                qmax = hw
            else:
                qmin = -hw
                qmax = hw - r
            for q in range(qmin, qmax + 1):
                if self.get(q, r) == '.':
                    break
                #TODO: stuff

