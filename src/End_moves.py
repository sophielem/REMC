#! /usr/bin/env python3
import random
import Movement

class End_moves(Movement.Movement):
  """ text
  """

  def mutation(self, structure_grid):
    if self.index == 0:
      freedom_neighbour_list = self.residu.next_res.search_freedom_neighbour(structure_grid)
    else:
      freedom_neighbour_list = self.residu.previous_res.search_freedom_neighbour(structure_grid)
    if freedom_neighbour_list == []:
        return None

    random_neighbour = random.randint(0, len(freedom_neighbour_list) - 1)
    return freedom_neighbour_list[random_neighbour]


  def __init__(self, res, i):
      Movement.Movement.__init__(self, i)
      self.residu = res
