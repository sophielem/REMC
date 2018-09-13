#! /usr/bin/env python3
"""REMC script

Usage:
  main.py -s <seq> -e <x> -p <nb_steps> -m <move> -t <temp>

Options:
  -h --help                  help
  --version                  version of the script
  -s --sequence = seq        write the sequence according to HP model
  -e --energy = x            write the mminimum energy to reach
  -p --steps = nb_steps      the maximum steps
  -m --movement = move       VSHD, PULLMOVES or MIXE
  -t --temperature = temp    the temperature
"""

import random
import math
import os
import matplotlib.pyplot as plt
from docopt import docopt
import conformation
import checkingArgument as cA
from Residu import *
from Movement import *

DEBUG = True

def initialization():
    """ Initialization of the lattice and residues object
    """
    residues = []
    previous = None

    for i in range(0, cA.LEN_SEQ):
        structure_grid[2 * cA.LEN_SEQ][i + round(1.5 * cA.LEN_SEQ)] = i
        now = Residu(cA.SEQUENCE[i], 2 * cA.LEN_SEQ,
                     i + round(1.5 * cA.LEN_SEQ))
        if i != 0:
            # the residu object now is the following of residu previous
            previous.next_res = now
           # the residu previous is the previous of residu now
        now.previous_res = previous
        residues.append(now)
        previous = now
    # the last residu has not next residu
    residues[i].next_res = None
    return residues


def display(residues, energy):
    lines = []
    columns = []
    hp = []
    # Create list for line and column
    for entry in residues:
        lines.append(entry.line)
        columns.append(entry.column)
        # Retrieve hp for color each point
        if entry.hp == "H":
            hp.append('r')
        else:
            hp.append('b')
    # Create the directory results if it does not exist
    if not os.path.exists("../results"):
        os.makedirs("../results")

    plt.scatter(columns, lines, color=hp, zorder=2, s=400)
    plt.plot(columns, lines, 'grey', zorder=1)
    plt.title('Optimal conformation found\n Energy : {}'.format(energy))
    plt.savefig("../results/conformation.png")
    plt.show()


if __name__ == '__main__':
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialize the lattice to -1 for empty
    structure_grid = [[-1] * (4 * cA.LEN_SEQ) for i in range(4 * cA.LEN_SEQ)]

    residues = initialization()
    energy = 0
    nb_steps = 0

    while nb_steps < cA.NB_STEPS:
        index = random.randint(0, cA.LEN_SEQ - 1)

        # Movement
        move = Movement(index)
        if cA.MOVE_SET == "VSHD":
            # the lattice and residues object with the mutation if it is possible
            new_conformation = conformation.vshd_move(
                index, structure_grid, residues)

        elif cA.MOVE_SET == "PULLMOVES":
            conformation.pullmoves_move(index, structure_grid)

        else:
            conformation.mixe_move(index, structure_grid)

        # The movement is possible, the new energy is calculated
        if new_conformation != None:
            energy_new = move.countBonds(
                new_conformation[1], new_conformation[0])

        # The movement makes the energy decrease
            if energy_new <= energy:
                # Keep the new conformation and residues object
                residues = new_conformation[0]
                structure_grid = new_conformation[1]
                energy = energy_new

        # Otherwise, calculate the probability to accept anyway the new conformation
            else:
              prob_random = random.random()
              if prob_random >= math.exp(-(energy_new - energy) / cA.TEMPERATURE):
                residues = new_conformation[0]
                structure_grid = new_conformation[1]
                energy = energy_new
        nb_steps = nb_steps + 1


    if DEBUG:
        for i in structure_grid:
            for j in i:
                if j != -1:
                    print("{0:2d}".format(j), end='')
                else:
                    print("  ", end='')
            print("")
        print(energy)
    display(residues, energy)
