#! /usr/bin/env python3
import random
import Movement

class Crankshaft_moves(Movement.Movement):
  """ To be possible, residue i is part of a u-shaped bend in the chain which
      involves a 180° rotation of a u-shaped structure consisting of four connected neighbours.
  """

#BUG DOUBLON DE LA FONCTION
  def mutation(self, structure_grid ):
      """ Search if the residu i is part of a u-shaped then search the rotation
          Return the 2 free neighbour in a list
      """
    attribut = ['column', 'line']
    attribut2 = ['line', 'column']
    for i in range(2):
      # i and i+1 are in the same column
      if getattr(self.residu, attribut[i]) == getattr(self.residu.next_res, attribut[i]):
        # i-1 and i+2 are in the same column and
        # i and i-1 are in the same line and
        # i+1 and i+2 are in the same line
        if (getattr(self.residu.previous_res, attribut[i]) == getattr(self.residu.next_res.next_res, attribut[i]) and
           getattr(self.residu, attribut2[i]) == getattr(self.residu.previous_res, attribut2[i]) and
           getattr(self.residu.next_res, attribut2[i]) == getattr(self.residu.next_res.next_res, attribut2[i])) :
          # conformation in U, search free neighbours in the same line
          delta = getattr(self.residu.previous_res, attribut[i]) - getattr(self.residu, attribut[i])
          if (structure_grid[getattr(self.residu, attribut2[i])][getattr(self.residu.previous_res, attribut[i]) + delta] == -1 and
             structure_grid[getattr(self.residu.next_res, attribut2[i])][getattr(self.residu.next_res.next_res, attribut[i]) + delta] == -1):
             return [{attribut2[i]: getattr(self.residu, attribut2[i]),
                      attribut[i]: getattr(self.previous_res, attribut[i]) + delta},
                     {attribut2[i]: getattr(self.residu.next_res, attribut2[i]),
                      attribut[i]: getattr(self.residu.next_res.next_res, attribut[i]) + delta}, 1]


      for i in range(2):
      # i and i+1 are in the same column
        if getattr(self.residu, attribut[i]) == getattr(self.residu.previous_res, attribut[i]):
        # i-1 and i+2 are in the same column and
        # i and i-1 are in the same line and
        # i+1 and i+2 are in the same line
          if (getattr(self.residu.next_res, attribut[i]) == getattr(self.residu.previous_res.previous_res, attribut[i]) and
             getattr(self.residu, attribut2[i]) == getattr(self.residu.next_res, attribut2[i]) and
             getattr(self.residu.previous_res, attribut2[i]) == getattr(self.residu.previous_res.previous_res, attribut2[i])) :
            # conformation in U, search free neighbours in the same line
            cote = getattr(self.residu.next_res, attribut[i]) - getattr(self.residu, attribut[i])
            if (structure_grid[getattr(self.residu, attribut2[i])][getattr(self.residu.next_res, attribut[i]) + cote] == -1 and
               structure_grid[getattr(self.residu.previous_res, attribut2[i])][getattr(self.residu.previous_res.previous_res, attribut[i]) + cote] == -1):
               return [{attribut2[i]: getattr(self.residu, attribut2[i]),
                        attribut[i]: getattr(self.next_res, attribut[i]) + cote},
                       {attribut2[i]: getattr(self.residu.previous_res, attribut2[i]),
                        attribut[i]: getattr(self.residu.previous_res.previous_res, attribut[i]) + cote}, -1]

    return None


  def __init__(self, res, i):
      """ Initialize the object Crankshaft_moves
          :param res: Residu object
          :param   i: index of the Residu object
      """
      Movement.Movement.__init__(self, i)
      self.residu = res
