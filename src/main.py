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
import math
from docopt import docopt
import conformation
import checkingArgument as cA
from Residu import *
from Movement import *


def initialization():
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
  # Le dernier residu n a pas de residu suivant
  residues[i].next_res = None
  return residues


if __name__ == '__main__':
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialiser une matrice vide à -1
    structure_grid = [[-1] * (4*cA.LEN_SEQ) for i in range(4*cA.LEN_SEQ)]

    residues = initialization()
    energy = 0

    # for i in range(0, NB_STEPS):
    index = random.randint(0, cA.LEN_SEQ - 1)

    # Mouvement
    move = Movement(cA.LEN_SEQ - 1)
    if cA.MOVE_SET == "VSHD":
        random_neighbour = conformation.vshd_move(cA.LEN_SEQ - 1, structure_grid, residues)

    elif cA.MOVE_SET == "PULLMOVES":
        conformation.pullmoves_move(index, structure_grid)

    else:
        conformation.mixe_move(index, structure_grid)

    # Le mouvement est possible
    if random_neighbour != None:
      new_conformation = move.changeConformation(structure_grid, residues, random_neighbour)
      energy_new = move.countBonds(new_conformation[1], new_conformation[0])
      
    # Le mouvement permet de baisser l energie
      if energy_new <= energy:
        residues = new_conformation[0]
        structure_grid = new_conformation[1]

    # Sinon on regarde la probabilite suivant l algo de Monte Carlo
      else:
        prob_random = random.random()
        if prob_random >= math.exp(-(energy_new - energy) / TEMPERATURE):
          residues = new_conformation[0]
          structure_grid = new_conformation[1]
