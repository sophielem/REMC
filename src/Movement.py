#! /usr/bin/env python3
import checkingArgument as cA
import copy
class Movement():

    def countBonds(self, structure_grid, residues):
        bonds = 0
        counted_bond = []
        for res in range(cA.LEN_SEQ):
            # Si polaire, pas de liaison possible donc suivant
            if cA.SEQUENCE[res] == 'P':
                continue
            index = []
            index.append(structure_grid[residues[res].line][residues[res].column + 1])
            index.append(structure_grid[residues[res].line][residues[res].column - 1])
            index.append(structure_grid[residues[res].line + 1][residues[res].column ])
            index.append(structure_grid[residues[res].line - 1][residues[res].column ])

            for idx in index:
                # res+1 et res-1 vérifier que le résidu n'est pas un voisin sur la séquence
                if idx != res+1 and idx != res-1 and residues[idx] == 'H' and not sorted(idx, res) in counted_bond:
                    counted_bond.append(sorted([idx, res]))
                    bonds -= 1

        return bonds


    def changeConformation(self, structure_grid, residues, random_neighbour):
        # copie les résidus et la grille et assigne la nouvelle conformation
        structure_grid_new = copy.deepcopy(structure_grid)
        # l ancienne position du residu devient vide
        structure_grid_new[residues[self.index].line][residues[self.index].column] = -1
        structure_grid_new[random_neighbour['line']][random_neighbour['column']] = self.index

        residues_new = copy.deepcopy(residues)
        # attribution des nouvelles coordonnées
        residues_new[self.index].line = random_neighbour['line']
        residues_new[self.index].column = random_neighbour['column']

        return [residues_new, structure_grid_new]


    def __init__(self, i):
        self.index = i
