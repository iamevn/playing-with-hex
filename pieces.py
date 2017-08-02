#!/usr/bin/env python3

import random

plist = [
# X
[(0, 0)],
# X X X X
[(0, 0), (1, 0), (2, 0), (3, 0)],
#  X .  
# . X . 
#  . X .
# . . X 
[(1, -1), (1, 0), (1, 1), (1, 2)],
#  . X  
# . X . 
#  X . .
# X . . 
[(-1, 2), (0, 1), (1, 0), (2, -1)],
#  X X
# X X .
#  . .
[(0, 0), (1, 0), (1, -1), (2, -1)],
#  X X
# . X X
#  . .
[(1, 0), (2, 0), (1, -1), (2, -1)],
#  X .
# X X .
#  X .
[(0, 0), (1, 0), (0, 1), (1, -1)],
#  X .
# X . .
#  X X
[(0, 0), (1, -1), (0, 1), (1, 1)],
#  X X
# . . X
#  . X
[(2, 0), (1, 1), (1, -1), (2, -1)],
#  X X
# X . .
#  X .
[(0, 0), (1, -1), (2, -1), (0, 1)],
#  . X
# . . X
#  X X
[(2, 0), (2, -1), (0, 1), (1, 1)],
#  . .
# X . X
#  X X
[(0, 0), (2, 0), (0, 1), (1, 1)],
#  X X
# X . X
#  . .
[(0, 0), (2, 0), (1, -1), (2, -1)],
#  X .
# X X .
#  . X
[(0, 0), (1, 0), (1, -1), (1, 1)],
#  X X
# . X .
#  . X
[(2, -1), (1, 0), (1, -1), (1, 1)],
#  . X
# . X X
#  X .
[(1, 0), (2, 0), (2, -1), (0, 1)],
#  X X
# . X .
#  X .
[(1, 0), (1, -1), (2, -1), (0, 1)],
#  . X
# . X .
#  X X
[(1, 0), (2, -1), (0, 1), (1, 1)],
#  . X
# X X .
#  X .
[(1, 0), (2, -1), (0, 1), (0, 0)],
#  X .
# . X .
#  X X
[(1, 0), (1, -1), (0, 1), (1, 1)],
#  X .
# . X X
#  . X
[(1, 0), (1, -1), (2, 0), (1, 1)],
#  . X
# X X X
#  . .
[(0, 0), (1, 0), (2, 0), (2, -1)],
#  . .
# X X X
#  . X
[(0, 0), (1, 0), (2, 0), (1, 1)],
#  X .
# X X X
#  . .
[(0, 0), (1, 0), (2, 0), (1, -1)],
#  . .
# X X X
#  X .
[(0, 0), (1, 0), (2, 0), (0, 1)],
]

def draw(pieceidx, win, ch='#'):
    """piece's 0,0 is on the far left of second line of text"""
    piece = plist[pieceidx]
    for (q, r) in piece:
        y = r + 1
        x = (q * 2 + r)
        win.addch(y, x, ord(ch))

def randompiece():
    return random.randrange(len(plist))

def likelyhood(pieceidx):
    """the likelyhood of given piece coming up.
    assuming all pieces have even chances until I do some testing"""
    return 1 / len(plist)
