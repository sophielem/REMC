#! /usr/bin/env python3
"""
    Define different movement possible according to user's choice.
    Then, launch the most appropriate movement.
"""

import random
import checking_argument as cA
import end_moves
import corner_moves
import crankshaft_moves
import pull_moves


def vshd_move(index, structure_grid, residues):
    """ Launch a VSHD movement according to the random residu.
        @param index: The random index
        @param structure_grid: A list of lists, which contains the
                               conformation of the sequence
        @param residues: A list of residu object
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    # If the residu is the first or the last
    if index == 0 or index == (cA.LEN_SEQ - 1):
        move = end_moves.end_moves(residues[index], index)
        mutation_residu = move.mutation(structure_grid)
        # The mutation is possible because a neighbour is free
        if mutation_residu is not None:
            new_conformation = move.changeOneresidu(
                structure_grid, residues, mutation_residu)
    else:
        # Choose randomly between corner or crankshaft movement
        prob = random.random()
        if prob >= 0.5:
            move = crankshaft_moves.crankshaft_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            if mutation_residu is not None:
                new_conformation = move.changeTworesidues(
                    structure_grid, residues, mutation_residu)
        else:
            move = corner_moves.corner_moves(residues[index], index)
            mutation_residu = move.mutation(structure_grid)
            if mutation_residu is not None:
                new_conformation = move.changeOneresidu(
                    structure_grid, residues, mutation_residu)
    return new_conformation

# PULLMOVE SET


def pullmoves_move(index, structure_grid, residues):
    """ Launch a pull move movement according to the random residu.
        @param index: The random index
        @param structure_grid: A list of lists, which contains the
                               conformation of the sequence
        @param residues: A list of residu object
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    move = pull_moves.pull_moves(residues[index], index)
    mutation_residu = move.mutation(structure_grid, residues)
    if mutation_residu is not None:
        new_conformation = move.changeTworesidues(structure_grid,
                                                  residues, mutation_residu)
    return new_conformation


# MIXE SET
def mixe_move(index, structure_grid, residues):
    """ Launch a pull move movement or a VSHD move according to
    the random residu.
        @param index: The random index
        @param structure_grid: A list of lists, which contains the
                               conformation of the sequence
        @param residues: A list of residu object
        Return a list with the new lattice and the new residues object
    """
    new_conformation = None
    prob = random.random()
    if index == 0 or index == (cA.LEN_SEQ - 1):
        move = end_moves.end_moves(residues[index], index)
        mutation_residu = move.mutation(structure_grid)
        # The mutation is possible because a neighbour is free
        if mutation_residu is not None:
            new_conformation = move.changeOneresidu(
                structure_grid, residues, mutation_residu)
    else:
        if prob <= 0.4:
            # pull movement
            return pullmoves_move(index, structure_grid, residues)
        else:
            # vshd movement
            prob = random.random()
            if prob >= 0.5:
                move = crankshaft_moves.crankshaft_moves(residues[index],
                                                         index)
                mutation_residu = move.mutation(structure_grid)
                if mutation_residu is not None:
                    new_conformation = move.changeTworesidues(
                        structure_grid, residues, mutation_residu)
            else:
                move = corner_moves.corner_moves(residues[index], index)
                mutation_residu = move.mutation(structure_grid)
                if mutation_residu is not None:
                    new_conformation = move.changeOneresidu(
                        structure_grid, residues, mutation_residu)

    return new_conformation
