#! /usr/bin/env python3
import checkingArgument as cA
import copy
class Movement():
  """ text
  """

def countBonds(structure_grid, residues):
    bonds = 0
    for res in range(cA.LEN_SEQ):
        # Si polaire, pas de liaison possible donc suivant
        if cA.SEQUENCE[res] == 'P':
            continue
        for i in range(1, 3):
            index = structure_grid[residues[res].line][residues[res].column + i]
            index2 = structure_grid[residues[res].line + 1][residues[res].column ]
            # res+1 et res-1 vérifier que le résidu n'est pas un voisin sur la séquence
            if index != res+1 and index != res-1 and residues[index] == 'H':
                bonds += 1
            if index2 != res+1 and index2 != res-1 and residues[index2] == 'H':
                bonds += 1
    return bonds


def changeGrid(self, structure_grid, residues, random_neighbour, index):
    energy = countBonds(structure_grid, residues)

    # copie les résidus et la grille pour comparer les energies des 2 conformations
    residu_new = copy.deepcopy(self.residu)
    structure_grid_new = copy.deepcopy(structure_grid)

    # l ancienne position du residu devient vide
    structure_grid_new[residu_new.line][residu_new.column] = -1
    # attribution des nouvelles coordonnées
    residu_new.line = random_neighbour['line']
    residu_new.column = random_neighbour['column']
    # nouvelle position sur la grille
    structure_grid_new[residu_new.line][residu_new.column] = index
    print(structure_grid_new)
    energy_new = countBonds(structure_grid_new, residues)

    return energy_new < energy
