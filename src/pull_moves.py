#! /usr/bin/env python3
import movement


class pull_moves(movement.movement):
    """ A square is formed by residues i, i + 1, L and C.
    A pull move can only proceed if C is either empty or occupied by
    residue i - 1.
    """

    def __find_ngh_occupied(self, structure_grid, j, idx, elmt, i):
        """ Find if a neighbour of the first or last residues of sequence
        of 3 residues is occupied or not in the next or previous column
        or next or previous line
            @param strcuture_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param j: The column or line of the first found residu
            @param idx: The line or column of the random residu
            @param elmt: The line or column find
            @param i: 0: column  1:line
        """
        second_residu = None
        for offset in [1, -1]:
            if i == 0:
                # if the neighbour is on the column to the right or left of j,
                # then the second residu to move is j
                if (elmt[j] != 0 and structure_grid[j][idx + offset] == elmt[j] + offset or
                   structure_grid[j][idx - offset] == elmt[j] + offset):
                    idx_ngh = elmt[j] + offset
                    second_residu = elmt[j]
                    return [idx_ngh, second_residu]

                # if the neighbour is on the column to the right or left of
                # j+2, then the second residu to move is j+2
                elif (elmt[j+2] != 0 and structure_grid[j+2][idx + offset] == elmt[j+2] + offset or
                      structure_grid[j+2][idx - offset] == elmt[j+2] + offset):
                    idx_ngh = elmt[j+2] + offset
                    second_residu = elmt[j+2]
                    return [idx_ngh, second_residu]
                else:
                    idx_ngh = None

            else:
                # if the neighbour is on the line above or below j,
                # then the second residu to move is j
                if (elmt[j] != 0 and structure_grid[idx + offset][j] == elmt[j] + offset or
                   structure_grid[idx - offset][j] == elmt[j] + offset):
                    idx_ngh = elmt[j] + offset
                    second_residu = elmt[j]
                    return [idx_ngh, second_residu]

                # if the neighbour is on the line above or below j+2,
                # then the second residu to move is j+2
                elif (elmt[j+2] != 0 and structure_grid[idx + offset][j+2] == elmt[j+2] + offset or
                      structure_grid[idx - offset][j+2] == elmt[j+2] + offset):
                    idx_ngh = elmt[j+2] + offset
                    second_residu = elmt[j+2]
                    return [idx_ngh, second_residu]
                else:
                    idx_ngh = None

        return [idx_ngh, second_residu]

    def __check_ngh_free(self, structure_grid, res_a, j, second_residu, i):
        """ Check if the 2 neighbours in the same line or column of residu a
        are free. If so, the conformation is correct to do the pull move.
            @param structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param res_a: The residu find by the function __find_ngh_occupied
            @param j: The column or the line of the first found residu
            @param second_residu: The index of the second residu to move
            @param i: 0: column  1: line
        """
        if i == 0:
            if res_a.line == j:
                # check if, on the same column, neighbour below res_a are free
                if (structure_grid[res_a.line + 1][res_a.column] == -1 and
                   structure_grid[res_a.line + 2][res_a.column] == -1):
                    # The 2 empty positions, and the second residu to move
                    return [{'line': res_a.line + 2, 'column': res_a.column},
                            {'line': res_a.line + 1, 'column': res_a.column},
                            second_residu - self.index]
            else:
                # check if, on the same column, neighbour above res_a are free
                if (structure_grid[res_a.line - 1][res_a.column] == -1 and
                   structure_grid[res_a.line - 2][res_a.column] == -1):
                   return [{'line': res_a.line - 2, 'column': res_a.column},
                            {'line': res_a.line - 1, 'column': res_a.column},
                            second_residu - self.index]
        else:
            if res_a.column == j:
                # check if, on the same line, neighbour to the right res_a are
                # free
                if (structure_grid[res_a.line][res_a.column + 1] == -1 and
                   structure_grid[res_a.line][res_a.column + 2] == -1):
                    return [{'line': res_a.line, 'column': res_a.column + 2},
                            {'line': res_a.line, 'column': res_a.column + 1},
                            second_residu - self.index]
            else:
                # check if, on the same line, neighbour to the left res_a
                # are free
                if (structure_grid[res_a.line][res_a.column - 1] == -1 and
                   structure_grid[res_a.line][res_a.column - 2] == -1):
                    return [{'line': res_a.line, 'column': res_a.column - 2},
                            {'line': res_a.line, 'column': res_a.column - 1},
                            second_residu - self.index]
        return None

    def mutation(self, structure_grid, residues):
        """ Check if the conformation is correct to do the pull move.
        If so, return the 2 new positions in a list.
            @param structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            @param residues: A list of residu object
            Return None if the movement is not possible or return the 2
        positions and the second residu to move
        """
        attribut = ["column", "line"]
        i = -1
        flag = False
        while i < 1 and flag is False:
            i += 1
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
                if (elmt[j] != -1 and elmt[j] != 0 and
                   (elmt[j] == self.index + 1 or elmt[j] == self.index - 1)):
                    if (elmt[j+1] == self.index and elmt[j+2] != -1 and
                       (elmt[j+2] == self.index + 1 or
                       elmt[j+2] == self.index - 1)):
                        flag = True
                        break

        if flag:
            # Check if the residu j has an occupied neighbour
            idx_ngh, second_residu = self.__find_ngh_occupied(structure_grid,
                                                              j, idx, elmt, i)

            if idx_ngh is not None:
                # Check if residu a has 2 free neighbours
                return self.__check_ngh_free(structure_grid, residues[idx_ngh],
                                             j, second_residu, i)

        return None

    def __init__(self, res, i):
        """ Initialize the object end_moves
            @param res: residu object
            @param   i: index of the residu object
        """
        movement.movement.__init__(self, i)
        self.residu = res
