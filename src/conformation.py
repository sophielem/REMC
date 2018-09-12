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
import Corner_moves
import Crankshaft_moves


def vshd_move(index, structure_grid, residues):
    new_conformation = None
    if index == 0 or index == (cA.LEN_SEQ - 1):
        move = End_moves.End_moves(residues[index], index)
        mutation_residu = move.mutation(structure_grid)
        if mutation_residu != None:
            new_conformation = move.changeOneResidu(structure_grid, residues, mutation_residu)
    else:
        prob = random.random()
        if prob >= 0.5:
            move = Crankshaft_moves.crankshaft_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            new_conformation = move.changeTwoResidues(structure_grid, residues, mutation_residu)
        else:
            move = Corner_moves.Corner_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            if mutation_residu != None:
                new_conformation = move.changeOneResidu(structure_grid, residues, mutation_residu)
    return new_conformation

#PULLMOVE SET
def pullmoves_move(residu, structure_grid):
    pull_moves(residu)


# MIXE SET
def mixe_move(residu, structure_grid):
    prob = random.random()
    if residu == 0 or residu == (cA.LEN_SEQ - 1):
        if prob <= 0.4:
            # pull movement
            endpull_moves(residu)
        else:
            # vshd movement
            move = End_moves.End_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
    else:
        if prob <= 0.4:
            # pull movement
            pull_moves(residu)
        else:
            # vshd movement
            prob = random.random()
            if prob >= 0.5:
                crankshaft_moves(residu)
            else:
                move = Corner_moves.Corner_moves(residues[index], index)
                mutation_residu = move.mutation(structure_grid)
