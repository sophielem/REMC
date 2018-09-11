#! /usr/bin/env python3
import random
import Movement

class End_moves(Movement.Movement):
  """ text
  """

  def functii(self, structure_grid):
      freedom_neighbour_list = self.residu.search_freedom_neighbour(structure_grid)
      if freedom_neighbour_list == []:
          return None
      random_neighbour = random.randint(0, len(freedom_neighbour_list) - 1)
      return freedom_neighbour_list[random_neighbour]


  def __init__(self, res):
      Movement.Movement.__init__(self)
      self.residu = res
