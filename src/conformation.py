#! /usr/bin/env python3
"""
    Define different movement possible according to user's choice.
    Then, launch the most appropriate movement.
"""

import checkingArgument as cA
import random
import copy
import Residu
import Movement
import End_moves
import Corner_moves
import Crankshaft_moves
import Pull_moves


def vshd_move(index, structure_grid, residues):
    """ Launch a VSHD movement according to the random residu.
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    # If the residu is the first or the last
    if index == 0 or index == (cA.LEN_SEQ - 1):
        move = End_moves.End_moves(residues[index], index)
        mutation_residu = move.mutation(structure_grid)
        # The mutation is possible because a neighbour is free
        if mutation_residu is not None:
            new_conformation = move.changeOneResidu(
                structure_grid, residues, mutation_residu)
    else:
        # Choose randomly between corner or crankshaft movement
        prob = random.random()
        if prob >= 0.5:
            move = Crankshaft_moves.Crankshaft_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            if mutation_residu is not None:
                new_conformation = move.changeTwoResidues(
                    structure_grid, residues, mutation_residu)
        else:
            move = Corner_moves.Corner_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            if mutation_residu is not None:
                new_conformation = move.changeOneResidu(
                    structure_grid, residues, mutation_residu)
    return new_conformation

# PULLMOVE SET


def pullmoves_move(index, structure_grid, residues):
    """ Launch a pull move movement according to the random residu.
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    move = Pull_moves.Pull_moves(residues[index], index)
    mutation_residu = move.mutation(structure_grid, residues)
    if mutation_residu is not None:
        new_conformation = move.changeTwoResidues(structure_grid,
                                                  residues, mutation_residu)
    return new_conformation


# MIXE SET
def mixe_move(index, structure_grid, residues):
    """ Launch a pull move movement or a VSHD move according to the random residu.
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    prob = random.random()
    if index == 0 or index == (cA.LEN_SEQ - 1):
        # if prob <= 0.4:
        #     # pull movement
        #     endpull_moves(residu)
        # else:
        # vshd movement
        move = End_moves.End_moves(residues[index], index)
        mutation_residu = move.mutation(structure_grid)
        # The mutation is possible because a neighbour is free
        if mutation_residu is not None:
            new_conformation = move.changeOneResidu(
                structure_grid, residues, mutation_residu)
    else:
        if prob <= 0.4:
            # pull movement
            return pullmoves_move(index, structure_grid, residues)
        else:
            # vshd movement
            prob = random.random()
            if prob >= 0.5:
                move = Crankshaft_moves.Crankshaft_moves(residues[index],
                                                         index)
                mutation_residu = move.mutation(structure_grid)
                if mutation_residu is not None:
                    new_conformation = move.changeTwoResidues(
                        structure_grid, residues, mutation_residu)
            else:
                move = Corner_moves.Corner_moves(residues[index], index)
                mutation_residu = move.mutation(structure_grid)
                if mutation_residu is not None:
                    new_conformation = move.changeOneResidu(
                        structure_grid, residues, mutation_residu)

    return new_conformation
