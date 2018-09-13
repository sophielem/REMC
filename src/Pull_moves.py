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
        for i in range(2):
            idx = getattr(self.residu, attribut[i])
            # C'est une liste de liste, donc on ne peut pas prendre de colonne directement
            if i == 0:
                elmt = []
                 for i in range(len(structure_grid)):
                    elmt.append(structure_grid[i][idx])
            else:
                elmt = structure_grid[idx]
            # Parcourir l'élément entier jusqu'à trouver une case remplie
            # A partir de là, on regarde si il a 2 voisins
            for j in range(len(elmt)):
                if elmt[j] != -1:
                    if elmt[j+1] != -1 and elmt[j+2] != -1:
                        break

    def __init__(self, res, i):
        """ Initialize the object End_moves
            :param res: Residu object
            :param   i: index of the Residu object
        """
        Movement.Movement.__init__(self, i)
        self.residu = res
