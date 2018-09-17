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
import checking_argument as cA
import monte_carlo as MC
import time


def display(residues, energy, idx):
    """ Plot the conformation of each replica in 3D with matplotlib
        @param residues: A list of residu object
        @param idx: The index of the rpelica for the title
    """
    lines = []
    columns = []
    hp = []
    # Create list for line and column
    for entry in residues:
        lines.append(entry.line)
        columns.append(entry.column)
        # Retrieve hp for color each point
        if entry.hp == "H":
            hp.append('b')
        else:
            hp.append('r')
    # Add a z axe to product a 3D plot
    z_axe = [0] * len(lines)
    # Create the directory results if it does not exist
    if not os.path.exists("../results"):
        os.makedirs("../results")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(columns, lines, z_axe, color=hp, zorder=2, s=400)
    plt.plot(columns, lines, z_axe, zorder=1)
    plt.title("Optimal conformation found for replica {}\
              \nEnergy : {}".format(idx, energy))
    plt.savefig("../results/conformation{}.png".format(idx))
    plt.show()


if __name__ == '__main__':
    tic = time.time()
    cA.check_arguments(docopt(__doc__, version='0.1'))
    # Initialization of the list which contains all replicates
    replicates = [None] * cA.REPLICA
    # The step between temperature of each replica
    shift = (220 - cA.TEMPERATURE) / cA.REPLICA
    for r in range(cA.REPLICA):
        residues, structure_grid = MC.initialization()
        replicates[r] = {"sequence": residues, "lattice": structure_grid,
                         "temp": cA.TEMPERATURE + shift*(r+1),
                         "energy": 0}
    replicates = MC.REMCSimulation(0, 0, 0, replicates)
    toc = time.time()
    print("Execution time : {:.2f} sec".format(toc-tic))

    for idx, replica in enumerate(replicates):
        display(replica["sequence"], replica["energy"], idx)
