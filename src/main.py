#! /usr/bin/env python3
"""REMC script

Usage:
  main.py -s <seq> -e <x> -t <nb_steps> -m <move>

Options:
  -h --help                  help
  --version                  version of the script
  -s --sequence = seq        hgjgjhgjh
  -e --energy = x            hgjgjhgjh
  -t --steps = nb_steps      hgjgjhgjh
  -m --movement = move       VSHD, PULLMOVES or MIXE
"""

import random
from docopt import docopt
import conformation
import checkingArgument as cA

if __name__ == '__main__':
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialiser une matrice vide à -1
    structure_grid = [[-1] * (4*cA.LEN_SEQ) for i in range(4*cA.LEN_SEQ)]

    dico_residu = []
    # Ecrire la séquence au milieu de la matrice
    for i in range(0, cA.LEN_SEQ):
        structure_grid[2*cA.LEN_SEQ][i + round(1.5*cA.LEN_SEQ)] = i
        dico_residu.append({'HP': cA.SEQUENCE[i], 'line': 2*cA.LEN_SEQ, 'column': i + round(1.5*cA.LEN_SEQ)})

    # for i in range(0, NB_STEPS):
    residu = random.randint(0, cA.LEN_SEQ - 1)

    if cA.MOVE_SET == "VSHD":
        conformation.vshd_move(residu, structure_grid, dico_residu)
    elif cA.MOVE_SET == "PULLMOVES":
        conformation.pullmoves_move(residu, structure_grid)
    else:
        conformation.mixe_move(residu, structure_grid)
