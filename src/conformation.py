#! /usr/bin/env python3
'''
    Movement
'''
import checkingArgument as cA
import random
import copy
import Residu
import Movement
import End_moves



def vshd_move(index, structure_grid, residues):
    rep = None
    if index == 0 or index == (cA.LEN_SEQ - 1):
        test = End_moves.End_moves(residues[index], index)
        rep = test.functii(structure_grid)
    else:
        prob = random.random()
        if prob >= 0.5:
            crankshaft_moves(index)
        else:
            corner_moves(index)
    return rep


def crankshaft_moves(residu):
    pass


def corner_moves(residu):
    pass


def countBonds(structure_grid, residues):
    pass


#PULLMOVE SET
def pullmoves_move(residu, structure_grid):
    pull_moves(residu)


def pull_moves(residu):
    pass


# MIXE SET
def mixe_move(residu, structure_grid):
    prob = random.random()
    if residu == 0 or residu == (cA.LEN_SEQ - 1):
        if prob <= 0.4:
            # pull movement
            endpull_moves(residu)
        else:
            # vshd movement
            end_moves(residu)
    else:
        if prob <= 0.4:
            # pull movement
            pull_moves(residu)
        else:
            # vshd movement
            prob = random.random()
            if prob >= 0.8:
                crankshaft_moves(residu)
            else:
                corner_moves(residu)
