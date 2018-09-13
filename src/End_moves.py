#! /usr/bin/env python3
import random
import Movement


class End_moves(Movement.Movement):
    """ The residue is pivoted relative to its connected
        neighbour to a free position adjacent to that neighbour.
    """

    def mutation(self, structure_grid):
        """ Search free neighbour for the residu adjacent.
            If several positions are free, on
            is chosen randomly and the residu is pivoted to this position.
        """
        if self.index == 0:
            freedom_neighbour_list = self.residu.next_res.search_free_neighbour(
                structure_grid)
        else:
            freedom_neighbour_list = self.residu.previous_res.search_free_neighbour(
                structure_grid)
        if freedom_neighbour_list == []:
            return None

        random_neighbour = random.randint(0, len(freedom_neighbour_list) - 1)
        return freedom_neighbour_list[random_neighbour]

    def __init__(self, res, i):
        """ Initialize the object End_moves
            :param res: Residu object
            :param   i: index of the Residu object
        """
        Movement.Movement.__init__(self, i)
        self.residu = res
