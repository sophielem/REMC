#! /usr/bin/env python3
import copy
import checking_argument as cA


class movement():
    """ Mother class of all movements.
    """

    def countBonds(self, structure_grid, residues):
        """ Counts the number of bonds. For each bond, an energy of -1 is
        summed.
            @param: structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param residues: A list of residu object
            Return the total energy.
        """
        bonds = 0
        # List all bounds already counted to avoid duplicate
        counted_bond = []
        for res in range(cA.LEN_SEQ):
            # If residu is polar, non bound possible so next
            if cA.SEQUENCE[res] == 'P':
                continue
            # Contains all neighbours, free or not
            index = []
            index.append(
                structure_grid[residues[res].line][residues[res].column + 1])
            index.append(
                structure_grid[residues[res].line][residues[res].column - 1])
            index.append(
                structure_grid[residues[res].line + 1][residues[res].column])
            index.append(
                structure_grid[residues[res].line - 1][residues[res].column])

            for idx in index:
                # check neighbour is not adjacent in the sequence,
                # it's hydrophob and not already counted
                if ((idx != res + 1) and (idx != res - 1) and
                   (idx != -1) and (residues[idx].hp == 'H') and
                   (not sorted([idx, res]) in counted_bond)):
                    counted_bond.append(sorted([idx, res]))
                    bonds -= 1

        return bonds

    def changeOneresidu(self, structure_grid, residues, random_neighbour):
        """ Change the conformation of one residu.
            @param: structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param residues: A list of residu object
            @param random_neighbour: A dictionnary with coordinates of
                                     the free position
            Return the new conformation and residues obejct modified.
        """
        # copy residues and the lattice. Assign the new conformation
        structure_grid_new = copy.deepcopy(structure_grid)
        # the old position of residu becomes empty
        structure_grid_new[residues[self.index].line][
                           residues[self.index].column] = -1
        structure_grid_new[random_neighbour['line']
                           ][random_neighbour['column']] = self.index

        residues_new = copy.deepcopy(residues)
        # Assignement of new coordinates
        residues_new[self.index].line = random_neighbour['line']
        residues_new[self.index].column = random_neighbour['column']

        return [residues_new, structure_grid_new]

    def changeTworesidues(self, structure_grid, residues, random_neighbour):
        """ Change the conformation of two residues.
            @param: structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param residues: A list of residu object
            @param random_neighbour: A list with 2 dictionnaries containing
                                     coordinates of the 2 free positions and
                                     the difference between the 2 residues
                                     to move
            Return the new conformation and reidues objet modified.
        """
        delta = random_neighbour[2]
        # copy residues and the lattice, assign the new conformation
        structure_grid_new = copy.deepcopy(structure_grid)
        # the old positions of residues become empty
        structure_grid_new[residues[self.index].line][
                           residues[self.index].column] = -1
        structure_grid_new[random_neighbour[0]['line']
                           ][random_neighbour[0]['column']] = self.index
        # Second residu
        structure_grid_new[residues[self.index + delta].line][
                           residues[self.index + delta].column] = -1
        structure_grid_new[random_neighbour[1]['line']][
                           random_neighbour[1]['column']] = self.index + delta

        residues_new = copy.deepcopy(residues)
        # Assignementof new coordinates
        residues_new[self.index].line = random_neighbour[0]['line']
        residues_new[self.index].column = random_neighbour[0]['column']
        # Second residu
        residues_new[self.index + delta].line = random_neighbour[1]['line']
        residues_new[self.index + delta].column = random_neighbour[1]['column']

        return [residues_new, structure_grid_new]

    def __init__(self, i):
        """ Initialize the object movement
            @param   i: index of the residu object
        """
        self.index = i
