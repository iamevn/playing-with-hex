#!/usr/bin/env python3

from pieces import plist, likelyhood
from board import Board

def best_placement(board, stored_pieces):
    """return a dict containing "piece", "coord",
    and "score" elements to show the best next move"""
    best = {"piece": None, "coord": None, "score": 0}

    for i in range(len(stored_pieces)):
        pieceidx = stored_pieces[i]
        other_stored = stored_pieces[:i] + stored_pieces[i + 1:]
        for space in board.spaces:
            if board.can_place(*space, pieceidx):
                attempt = whatif_score(board, space, pieceidx, other_stored)
                if attempt > best["score"]:
                    best = {"piece": pieceidx, "coord": space, "score": attempt}
    return best


def whatif_score(board, space, pieceidx, stored):
    """count up possible placements of other two stored pieces
    possibly add in small amount for possible placements of a random other piece"""
    newboard = Board(board)
    newboard.place(*space, pieceidx)
    newboard.clearLines()

    placements = 0
    for pieceidx in stored:
        for space in newboard.spaces:
            if newboard.can_place(*space, pieceidx):
                placements += 1
    otherpiece_placements = 0
    for pieceidx in range(len(plist)):
        for space in newboard.spaces:
            if newboard.can_place(*space, pieceidx):
                otherpiece_placements += likelyhood(pieceidx)

    return placements + otherpiece_placements
    

