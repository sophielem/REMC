#! /usr/bin/env python3
import random
import movement


class crankshaft_moves(movement.movement):
    """ To be possible, residue i is part of a u-shaped bend in the chain which
        involves a 180° rotation of a u-shaped structure consisting
        of four connected neighbours.
    """

    def mutation(self, structure_grid):
        """ Search if the residu i is part of a u-shaped then search the rotation
            Return the 2 free neighbour in a list
        """
        attribut = ['column', 'line', 'column', 'line']
        attribut2 = ['line', 'column', 'line', 'column']

        if (self.residu.next_res is not None and
           self.residu.previous_res is not None):
            # to simplify the notation
            next = self.residu.next_res
            previous = self.residu.previous_res
            i = 0
        else:
            i = 4

        while i < 4:
            if i < 2 and self.residu.next_res.next_res is not None:
                following = self.residu.next_res.next_res
                shift = 1
            elif i >= 2 and self.residu.previous_res.previous_res is not None:
                following = self.residu.previous_res.previous_res
                shift = -1
            else:
                break

            # i and i+1 are in the same column
            if getattr(self.residu, attribut[i]) == getattr(next, attribut[i]):
                # i-1 and i+2 are in the same column and
                # i and i-1 are in the same line and
                # i+1 and i+2 are in the same line
                if (getattr(previous, attribut[i]) ==
                   getattr(following, attribut[i]) and
                   getattr(self.residu, attribut2[i]) ==
                   getattr(previous, attribut2[i]) and
                   getattr(next, attribut2[i]) ==
                   getattr(following, attribut2[i])):
                    # conformation in U,search free neighbours in the same line
                    delta = getattr(previous, attribut[i]) -\
                            getattr(self.residu, attribut[i])
                    # Conformation horizontal:
                    #       i      i+1
                    #       i-1    i+2
                    if (i == 0 and structure_grid[getattr(previous, attribut2[i]) + delta][getattr(self.residu, attribut[i])] == -1 and structure_grid[getattr(following, attribut2[i]) + delta][getattr(next, attribut[i])] == -1):
                        return [{attribut[i]: getattr(self.residu,
                                 attribut[i]), attribut2[i]:
                                 getattr(previous, attribut2[i]) + delta},
                                {attribut[i]: getattr(next, attribut[i]),
                                attribut2[i]: getattr(following, attribut2[i]) +
                                delta}, shift]

                    # Conformation vertical:
                    #       i-1      i
                    #       i+2     i+1
                    elif (i == 1 and structure_grid[getattr(self.residu, attribut[i])][getattr(previous, attribut2[i]) + delta] == -1 and structure_grid[getattr(next, attribut[i])][getattr(following, attribut2[i]) + delta] == -1):
                        return [{attribut[i]: getattr(self.residu,
                                 attribut[i]), attribut2[i]:
                                 getattr(previous, attribut2[i]) + delta},
                                {attribut[i]: getattr(next, attribut[i]),
                                attribut2[i]: getattr(following, attribut2[i]) +
                                delta}, shift]

                    # Conformation horizontal:
                    #       i-1     i
                    #       i-2    i+1
                    elif (i == 2 and structure_grid[getattr(next, attribut2[i]) + delta][getattr(self.residu, attribut[i])] == -1 and structure_grid[getattr(following, attribut2[i]) + delta][getattr(previous, attribut[i])] == -1):
                        return [{attribut[i]: getattr(self.residu,
                                 attribut[i]), attribut2[i]:
                                 getattr(next, attribut2[i]) + delta},
                                {attribut[i]: getattr(previous, attribut[i]),
                                attribut2[i]: getattr(following, attribut2[i]) +
                                delta}, shift]

                    # Conformation vertical:
                    #       i-2     i-1
                    #       i+1      i
                    elif (i == 3 and structure_grid[getattr(self.residu, attribut[i])][getattr(next, attribut2[i]) + delta] == -1 and structure_grid[getattr(previous, attribut[i])][getattr(following, attribut2[i]) + delta] == -1):
                        return [{attribut[i]: getattr(self.residu,
                                 attribut[i]), attribut2[i]:
                                 getattr(next, attribut2[i]) + delta},
                                {attribut[i]: getattr(previous, attribut[i]),
                                attribut2[i]: getattr(following, attribut2[i]) +
                                delta}, shift]
            i += 1

        return None

    def __init__(self, res, i):
        """ Initialize the object crankshaft_moves
            :param res: residu object
            :param   i: index of the residu object
        """
        movement.movement.__init__(self, i)
        self.residu = res
