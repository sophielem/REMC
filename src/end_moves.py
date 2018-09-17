#! /usr/bin/env python3
import random
import movement


class end_moves(movement.movement):
    """ The residue is pivoted relative to its connected
    neighbour to a free position adjacent to that neighbour.
    """

    def mutation(self, structure_grid):
        """ Search free neighbour for the residu adjacent.
        If several positions are free, one is chosen randomly and the residu
        is pivoted to this position.
            @param: structure_grid: A list of lists, which contains the
                                   conformation of the sequence
            Return None if the movement is not possible or the free position
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
        """ Initialize the object end_moves
            :param res: residu object
            :param   i: index of the residu object
        """
        movement.movement.__init__(self, i)
        self.residu = res
