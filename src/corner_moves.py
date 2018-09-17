#! /usr/bin/env python3
import random
import movement


class corner_moves(movement.movement):
    """ To be possible, the two connected neighbours of some residue i must
    be mutually adjacent to another, unoccupied position on the lattice.
    """

    def mutation(self, structure_grid):
        """ Search the unoccupied position for the movement
            @param structure_grid: A list of lists, which contains the
                                    conformation of the sequence
            Return the solution or None if the movement is not possible
        """
        # Search free neighbours of residues i+1 and i-1
        freedom_neighbour_next = self.residu.next_res.search_free_neighbour(
            structure_grid)
        freedom_neighbour_prev = self.residu.previous_res.search_free_neighbour(
            structure_grid)
        freedom_neighbour_list = []

        # Find the free neighbour common to residues i+1 and i-1
        for ngh_p in freedom_neighbour_prev:
            for ngh_n in freedom_neighbour_next:
                if (ngh_p['line'] == ngh_n['line'] and
                   ngh_p['column'] == ngh_n['column']):
                    freedom_neighbour_list.append(ngh_p)
        # If none neighbour are common, return none
        if freedom_neighbour_list == []:
            return None
        # If several free neighbour common are possible, choose one randomly
        random_neighbour = random.randint(0, len(freedom_neighbour_list) - 1)
        return freedom_neighbour_list[random_neighbour]

    def __init__(self, res, i):
        """ Initialize the object corner_moves
            @param res: residu object
            @param   i: index of the residu object
        """
        movement.movement.__init__(self, i)
        self.residu = res