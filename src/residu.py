#! /usr/bin/env python3


class residu:
    """ A class containing the coordinates of one amino acid and its
    hydrophobicty. It contains its previous and next residu in the sequence.
    """

    def search_free_neighbour(self, structure_grid):
        """ Search for freedom neighbour and return a dictionnaire
        of their coordinates
        """
        # A list of dictionnaries with coordinates of free neighbours
        freedom_neighbour_list = []

        if structure_grid[self.line][self.column + 1] == -1:
            freedom_neighbour_list.append({'line': self.line,
                                           'column': self.column + 1})
        if structure_grid[self.line][self.column - 1] == -1:
            freedom_neighbour_list.append({'line': self.line,
                                           'column': self.column - 1})
        if structure_grid[self.line + 1][self.column] == -1:
            freedom_neighbour_list.append({'line': self.line + 1,
                                           'column': self.column})
        if structure_grid[self.line - 1][self.column] == -1:
            freedom_neighbour_list.append({'line': self.line - 1,
                                           'column': self.column})

        return freedom_neighbour_list

    def __init__(self, hydrophobicity, x, y):
        """ Initialize the object residu
            @param hydrophobicty: h or p
            @param   x: the line of the residu
            @param   y: the column of the residu
        """
        self.hp = hydrophobicity
        self.line = x
        self.column = y
