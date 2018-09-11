#! /usr/bin/env python3
'''
    Movement
'''
import checkingArgument as cA
import random
import copy


def vshd_move(residu, structure_grid, dico_residu):
    if residu == 0 or residu == (cA.LEN_SEQ - 1):
        end_moves(residu, dico_residu, structure_grid)
    else:
        prob = random.random()
        if prob >= 0.8:
            crankshaft_moves(residu)
        else:
            corner_moves(residu)


def end_moves(residu, dico_residu, structure_grid):


def crankshaft_moves(residu):
    pass


def corner_moves(residu):
    pass


def search_freedom_neighbour(residu, structure_grid, dico_residu):



def countBonds(structure_grid, dico_residu):


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
