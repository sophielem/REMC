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
from Residu import *


if __name__ == '__main__':
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialiser une matrice vide à -1
    structure_grid = [[-1] * (4*cA.LEN_SEQ) for i in range(4*cA.LEN_SEQ)]

    residues = []
    previous = None

    for i in range(0, cA.LEN_SEQ):
        structure_grid[2*cA.LEN_SEQ][i + round(1.5*cA.LEN_SEQ)] = i
        now = Residu(cA.SEQUENCE[i], 2*cA.LEN_SEQ, i + round(1.5*cA.LEN_SEQ))
        if i != 0:
            # le résidu now est le suivant du résidu previous
            previous.next_res = now
        # ajout du residu previous au residu now
        now.previous_res = previous
        residues.append(now)
        previous = now

    # for i in range(0, NB_STEPS):
    residu = random.randint(0, cA.LEN_SEQ - 1)

    if cA.MOVE_SET == "VSHD":
        dico = conformation.vshd_move(0, structure_grid, residues)
        # residues = dico[residues]
        # structure_grid = dico[structure_grid]
    elif cA.MOVE_SET == "PULLMOVES":
        conformation.pullmoves_move(residu, structure_grid)
    else:
        conformation.mixe_move(residu, structure_grid)
