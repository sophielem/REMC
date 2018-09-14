#! /usr/bin/env python3
import Movement


class Pull_moves(Movement.Movement):
    """ A square is formed by residues i, i + 1, L and C.
        A pull move can only proceed if C is either empty
        or occupied by residue i - 1.
    """

    def __findNeighbourOccupied(self, structure_grid, j, idx, elmt, i):
        """ Find if a neighbour of the first or last residues of sequence
            of 3 residues is occupied or not in the next or previous column
            or next or previous line
        """
        second_residu = None
        for offset in [1, -1]:
            if i == 0:
                if (structure_grid[j][idx + offset] == elmt[j] + offset or
                   structure_grid[j][idx - offset] == elmt[j] + offset):
                    a = elmt[j] + offset
                    second_residu = elmt[j]
                    return [a, second_residu]
                elif (structure_grid[j+2][idx + offset] == elmt[j+2] + offset or
                      structure_grid[j+2][idx - offset] == elmt[j+2] + offset):
                    a = elmt[j+2] + offset
                    second_residu = elmt[j+2]
                    return [a, second_residu]
                else:
                    a = None

            else:
                if (structure_grid[idx + offset][j] == elmt[j] + offset or
                   structure_grid[idx - offset][j] == elmt[j] + offset):
                    # si le voisin se trouve sur la ligne au dessus de j,
                    # alors le second residu à bouger est j
                    a = elmt[j] + offset
                    second_residu = elmt[j]
                    return [a, second_residu]
                elif (structure_grid[idx + offset][j+2] == elmt[j+2] + offset or
                      structure_grid[idx - offset][j+2] == elmt[j+2] + offset):
                    # si le voisin se trouve sur la ligne au dessus de j+2,
                    # alors le second residu à bouger est j+2
                    a = elmt[+2j] + offset
                    second_residu = elmt[j+2]
                    return [a, second_residu]
                else:
                    a = None

        return [a, second_residu]

    def __checkNeighboursFree(self, structure_grid, a, j, second_residu, i):
        """ Check if the 2 neighbours in the same line or column of residu a are free.
            If so, the conformation is correct to do the pull move.
        """
        if i == 0:
            if a.line == j:
                if (structure_grid[a.line + 1][a.column] == -1 and
                   structure_grid[a.line + 2][a.column] == -1):
                    # Les 2 emplacements vides, et le deuxieme residu à bouger
                    return [{'line': a.line + 2, 'column': a.column},
                            {'line': a.line + 1, 'column': a.column},
                            second_residu - self.index]
            else:
                if (structure_grid[a.line - 1][a.column] == -1 and
                   structure_grid[a.line - 2][a.column] == -1):
                    return [{'line': a.line - 2, 'column': a.column},
                            {'line': a.line - 1, 'column': a.column},
                            second_residu - self.index]
        else:
            if a.column == j:
                if (structure_grid[a.line][a.column + 1] == -1 and
                   structure_grid[a.line][a.column + 2] == -1):
                    # Les 2 emplacements vides, et le deuxieme residu à bouger
                    return [{'line': a.line, 'column': a.column + 2},
                            {'line': a.line, 'column': a.column + 1},
                            second_residu - self.index]
            else:
                if (structure_grid[a.line][a.column - 1] == -1 and
                   structure_grid[a.line][a.column - 2] == -1):
                    # Les 2 emplacements vides, et le deuxieme residu à bouger
                    return [{'line': a.line, 'column': a.column - 2},
                            {'line': a.line, 'column': a.column - 1},
                            second_residu - self.index]
        return None

    def mutation(self, structure_grid, residues):
        """ Check if the conformation is correct to do the pull move.
            If so, return the 2 new positions in a list.
        """
        attribut = ["column", "line"]
        i = 0
        flag = False
        while i < 2 and flag is False:
            idx = getattr(self.residu, attribut[i])
            # It's a list which contains list, so it's not possible
            # to reach a column directly
            if i == 0:
                elmt = []
                for k in range(len(structure_grid)):
                    elmt.append(structure_grid[k][idx])
            else:
                elmt = structure_grid[idx]
            # Browse the entire element to find an occupied position
            # Then, check if it has 2 neighbours occupied in the same
            # line or column
            # Moreover, the next neighbour must be the chosen residu
            for j in range(len(elmt)):
                if elmt[j] != -1 and elmt[j] != 0:
                    if elmt[j+1] == self.index and elmt[j+2] != -1:
                        print("coord", j, idx)
                        print(elmt[j+1], elmt[j+2])
                        flag = True
                        break
            i += 1

        if flag:
            # Check if the residu j has an occupied neighbour
            a, second_residu = self.__findNeighbourOccupied(structure_grid,
                                                            j, idx, elmt, i)

            if a is not None:
                # Check if residu a has 2 free neighbours
                return self.__checkNeighboursFree(structure_grid,
                                                  residues[a], j, second_residu, i)

        return None

    def __init__(self, res, i):
        """ Initialize the object End_moves
            :param res: Residu object
            :param   i: index of the Residu object
        """
        Movement.Movement.__init__(self, i)
        self.residu = res
