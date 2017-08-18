#!/usr/bin/env python3

import random

# I've shifted some of these over to the left by one marked by a < in their comment.
# this was done in order to get the origin (0, 0) for each piece to be contained
# within the bounds of the piece.
plist = [
# X
[(0, 0)],
# X X X X
[(0, 0), (1, 0), (2, 0), (3, 0)],
#< X .
# . X .
#  . X .
# . . X
[(0, -1), (0, 0), (0, 1), (0, 2)],
#< . X
# . X .
#  X . .
# X . .
[(-2, 2), (-1, 1), (0, 0), (1, -1)],
#< X X
# . X X
#  . .
[(0, 0), (1, 0), (0, -1), (1, -1)],
#  X X
# X X .
#  . .
[(0, 0), (1, 0), (1, -1), (2, -1)],
#  X .
# X X .
#  X .
[(0, 0), (1, 0), (0, 1), (1, -1)],
#< X X
# . . X
#  . X
[(1, 0), (0, 1), (0, -1), (1, -1)],
#< . X
# . . X
#  X X
[(1, 0), (1, -1), (-1, 1), (0, 1)],
#  . .
# X . X
#  X X
[(0, 0), (2, 0), (0, 1), (1, 1)],
#  X .
# X . .
#  X X
[(0, 0), (1, -1), (0, 1), (1, 1)],
#  X X
# X . .
#  X .
[(0, 0), (1, -1), (2, -1), (0, 1)],
#  X X
# X . X
#  . .
[(0, 0), (2, 0), (1, -1), (2, -1)],
#< X .
# . X X
#  . X
[(0, 0), (0, -1), (1, 0), (0, 1)],
#< X .
# . X .
#  X X
[(0, 0), (0, -1), (-1, 1), (0, 1)],
#< . X
# . X .
#  X X
[(0, 0), (1, -1), (-1, 1), (0, 1)],
#  . X
# X X .
#  X .
[(1, 0), (2, -1), (0, 1), (0, 0)],
#  . .
# X X X
#  X .
[(0, 0), (1, 0), (2, 0), (0, 1)],
#  X .
# X X X
#  . .
[(0, 0), (1, 0), (2, 0), (1, -1)],
#  X .
# X X .
#  . X
[(0, 0), (1, 0), (1, -1), (1, 1)],
#< X X
# . X .
#  . X
[(1, -1), (0, 0), (0, -1), (0, 1)],
#< X X
# . X .
#  X .
[(0, 0), (0, -1), (1, -1), (-1, 1)],
#< . X
# . X X
#  X .
[(0, 0), (1, 0), (1, -1), (-1, 1)],
#  . X
# X X X
#  . .
[(0, 0), (1, 0), (2, 0), (2, -1)],
#  . .
# X X X
#  . X
[(0, 0), (1, 0), (2, 0), (1, 1)],
]

def draw(pieceidx, win, ch = '#', offset = (0, 0)):
    """piece's 0,0 is two right from the left edge of second line of text"""
    piece = plist[pieceidx]
    for (q, r) in piece:
        y = r + 1
        x = (q * 2 + r) + 2
        win.addch(y + offset[0], x + offset[1], ord(ch))

def randompiece():
    return random.randrange(len(plist))

def likelyhood(pieceidx):
    """the likelyhood of given piece coming up.
    assuming all pieces have even chances until I do some testing"""
    return 1 / len(plist)
