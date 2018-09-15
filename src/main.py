#! /usr/bin/env python3
"""REMC script

Usage:
  main.py -s <seq> -e <x> -m <move>
  main.py -s <seq> -e <x> -m <move> [-p <nb_steps>] [-t <temp>] [-r <nb_rep>]

Options:
  -h --help                  help
  --version                  version of the script
  -s --sequence = seq        write the sequence according to HP model
  -e --energy = x            write the mminimum energy to reach
  -m --movement = move       VSHD, PULLMOVES or MIXE
  -p --steps = nb_steps      the maximum steps [default: 500]
  -t --temperature = temp    the minimal temperature [default: 160]
  -r --replica = nb_rep      number of replica [default: 5]
"""

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from docopt import docopt
import checkingArgument as cA
import monteCarlo as MC


def display(residues, energy, idx):
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
    # Add a z axe to product a 3D plot
    z_axe = [0] * len(lines)
    # Create the directory results if it does not exist
    if not os.path.exists("../results"):
        os.makedirs("../results")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(columns, lines, z_axe, color=hp, zorder=2, s=400)
    plt.plot(columns, lines, z_axe, zorder=1)
    plt.title("Optimal conformation found for replica {}\n Energy : {}".format(idx, energy))
    plt.savefig("../results/conformation{}.png".format(idx))
    plt.show()


if __name__ == '__main__':
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialization of the list which contains all replicates
    replicates = [None] * cA.REPLICA
    # The step between temperature of each replica
    shift = (cA.TEMPERATURE - 220) / cA.REPLICA
    for r in range(cA.REPLICA):
        residues, structure_grid = MC.initialization()
        replicates[r] = {"sequence": residues, "lattice": structure_grid, "temperature": cA.TEMPERATURE + shift*(r+1), "energy": 0}

    replicates = MC.REMCSimulation(0, 0, 0, replicates)

    for idx, replica in enumerate(replicates):
        display(replica["sequence"], replica["energy"], idx)
