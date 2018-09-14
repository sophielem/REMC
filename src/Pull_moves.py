#! /usr/bin/env python3
import Movement


class Pull_moves(Movement.Movement):
    """ A square is formed by residues i, i + 1, L and C.
        A pull move can only proceed if C is either empty or occupied by residue i - 1.
    """

    def mutation(self, structure_grid):
        """ text
        """
        attribut = ["column", "line"]
        i = 0
        flag = False
        while i <2 and flag = False:
            idx = getattr(self.residu, attribut[i])
            # C'est une liste de liste, donc on ne peut pas prendre de colonne directement
            if i == 0:
                elmt = []
                 for k in range(len(structure_grid)):
                    elmt.append(structure_grid[k][idx])
            else:
                elmt = structure_grid[idx]
            # Parcourir l'élément entier jusqu'à trouver une case remplie
            # A partir de là, on regarde si il a 2 voisins
            # le 2 voisin devant être le résidu choisi aléatoirement
            for j in range(len(elmt)):
                if elmt[j] != -1:
                    if elmt[j+1] == self.index and elmt[j+2] != -1:
                        flag = True
            i += 1

        if flag:
            for offset in [1, -1]:
                if i == 0:
                    if structure_grid[j][idx + offset] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j]
                    elif structure_grid[j][idx - offset] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j]
                    elif structure_grid[j+2][idx + offset] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j+2]
                    elif structure_grid[j+2][idx - offset] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j+2]
                    else:
                        a = None

                else:
                    if structure_grid[idx + offset][j] == elmt[j] + offset:
                        # si le voisin se trouve sur la ligne au dessus de j, alors le second residu à bouger est j
                        a = elmt[j] + offset
                        second_residu = elmt[j]
                    elif structure_grid[idx - offset][j] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j]
                    elif structure_grid[idx + offset][j+2] == elmt[j] + offset:
                        # si le voisin se trouve sur la ligne au dessus de j+2, alors le second residu à bouger est j+2
                        a = elmt[j] + offset
                        second_residu = elmt[j+2]
                    elif structure_grid[idx - offset][j+2] == elmt[j] + offset:
                        a = elmt[j] + offset
                        second_residu = elmt[j+2]
                    else:
                        a = None


            if i == 0:
                if a.line == j:
                    if structure_grid[a.line + 1][a.column] == -1 and structure_grid[a.line + 2][a.column] == -1:
                        # Les 2 emplacements vides, et le deuxieme residu à bouger
                        return [{'line': a.line + 1, 'column': a.column}, {'line': a.line + 2, 'column': a.column}, second_residu]
                else:
                    if structure_grid[a.line - 1][a.column] == -1 and structure_grid[a.line - 2][a.column] == -1:
                        return [{'line': a.line - 1, 'column': a.column}, {'line': a.line - 2, 'column': a.column}, second_residu]
            else:
                if a.column == j:
                    if structure_grid[a.line][a.column + 1] == -1 and structure_grid[a.line][a.column + 2] == -1:
                        # Les 2 emplacements vides, et le deuxieme residu à bouger
                        return [{'line': a.line, 'column': a.column + 1}, {'line': a.line, 'column': a.column + 2}, second_residu]
                else:
                    if structure_grid[a.line][a.column - 1] == -1 and structure_grid[a.line][a.column - 2] == -1:
                        # Les 2 emplacements vides, et le deuxieme residu à bouger
                        return [{'line': a.line, 'column': a.column - 1}, {'line': a.line, 'column': a.column - 2}, second_residu]

        return None
        

    def __init__(self, res, i):
        """ Initialize the object End_moves
            :param res: Residu object
            :param   i: index of the Residu object
        """
        Movement.Movement.__init__(self, i)
        self.residu = res
