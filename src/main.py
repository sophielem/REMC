#! /usr/bin/env python3

import sys
import random
import conformation
import checkingArgument as cA

if __name__ == '__main__':
    cA.check_arguments(sys.argv[1:])
    # Initialiser une matrice vide à -1
    structure_grid = [[-1] * (4*cA.LEN_SEQ) for i in range(4*cA.LEN_SEQ)]

    # Ecrire la séquence au milieu de la matrice
    for i in range(0, cA.LEN_SEQ):
        structure_grid[2*cA.LEN_SEQ][i + round(1.5*cA.LEN_SEQ)] = i

    # for i in range(0, NB_STEPS):
    residu = random.randint(0, cA.LEN_SEQ - 1)

    if cA.MOVE_SET == "VSHD":
        conformation.vshd_move(residu)
    elif cA.MOVE_SET == "PULLMOVES":
        conformation.pullmoves_move(residu)
    else:
        conformation.mixe_move(residu)
