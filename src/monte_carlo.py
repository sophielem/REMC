#! /usr/bin/env python3
"""
    Monte Carlo algorithm and Replica exchange Monte Carlo
    search to find the optimal conformation for the sequence.
"""
import random
import math
import conformation
import checking_argument as cA
from residu import *
from movement import *


def initialization():
    """ Initialization of the lattice and residues object
    """
    residues = []
    previous = None
    # Initialize the lattice to -1 for empty
    structure_grid = [[-1] * (4 * cA.LEN_SEQ) for i in range(4 * cA.LEN_SEQ)]

    for i in range(0, cA.LEN_SEQ):
        structure_grid[2 * cA.LEN_SEQ][i + round(1.5 * cA.LEN_SEQ)] = i
        now = residu(cA.SEQUENCE[i], 2 * cA.LEN_SEQ,
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
    return residues, structure_grid

def MCsearch(residues, structure_grid, energy, temperature):
    """ Monte Carlo procedure. Choose randomly a residu and try to apply a movement.
        If the new energy is lower, it will be kept.
        Otherwise, according to a transition probability, it will be kept or deleted.
    """
    index = random.randint(0, cA.LEN_SEQ - 1)

    # movement
    move = movement(index)
    if cA.MOVE_SET == "VSHD":
        # the lattice and residues object with the mutation
        # if it is possible
        new_conformation = conformation.vshd_move(
            index, structure_grid, residues)

    elif cA.MOVE_SET == "PULLMOVES":
        new_conformation = conformation.pullmoves_move(index, structure_grid, residues)

    else:
        new_conformation = conformation.mixe_move(index, structure_grid, residues)

    # The movement is possible, the new energy is calculated
    if new_conformation is not None:
        energy_new = move.countBonds(
            new_conformation[1], new_conformation[0])

    # The movement makes the energy decrease
        if energy_new <= energy:
            # Keep the new conformation and residues object
            residues = new_conformation[0]
            structure_grid = new_conformation[1]
            energy = energy_new

    # Otherwise, calculate the probability to accept
    # anyway the new conformation
        else:
            prob_random = random.random()
            if prob_random >= math.exp(-(energy_new - energy) /
               temperature):
                residues = new_conformation[0]
                structure_grid = new_conformation[1]
                energy = energy_new
    return residues, structure_grid, energy

def swapLabels(replica_i, replica_j):
    """ Swap two replicates in the list to change their environment.
    """
    tmp_residues = replica_i["sequence"]
    tmp_structure_grid = replica_i["lattice"]
    tmp_energy = replica_i["energy"]

    replica_i["sequence"] = replica_j["sequence"]
    replica_i["lattice"] = replica_j["lattice"]
    replica_i["energy"] = replica_j["energy"]

    replica_j["sequence"] = tmp_residues
    replica_j["lattice"] = tmp_structure_grid
    replica_j["energy"] = tmp_energy
    return replica_i, replica_j

def REMCSimulation(energy, nb_steps, offset, replicates):
    """ Replica exchange Monte Carlo algorithm procedure.
        Use the Monte Carlo search algorithm and another dimension, temperature.
        During the steps, replica's temperature can be modified.
        Energies between replicates are compared and the lower is kept.
    """
    while nb_steps < cA.NB_STEPS and energy > cA.MIN_ENERGY:
        for replica in replicates:
            # Use the Monte Carlo algorithm
            replica["sequence"], replica["lattice"], replica["energy"] = MCsearch(replica["sequence"], replica["lattice"], replica["energy"], replica["temperature"])
            # Compare the new energy found with the global energy.
            if replica["energy"] < energy:
                energy = replica["energy"]
        nb_steps = nb_steps + 1

        # offset indicate if the replica is swap with its superior or its inferior replica
        i = offset
        while i+1 < cA.REPLICA:
            j = i + 1
            # Product of the energy difference and inverse temperature difference
            delta = (1/replicates[j]["temperature"] - 1/replicates[i]["temperature"]) * (replicates[i]["temperature"] - replicates[j]["temperature"])
            if delta <= 0:
                replicates[i], replicates[j] = swapLabels(replicates[i], replicates[j])
            else:
                q = random.random()
                # Probability of transition
                if q <= math.exp(- delta):
                    replicates[i], replicates[j] = swapLabels(replicates[i], replicates[j])
            i = i + 2
        offset = 1 - offset

    print("***************************************")
    print("   The best energy found is {}".format(energy))
    print("***************************************")
    return replicates
