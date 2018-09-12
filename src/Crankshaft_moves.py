#! /usr/bin/env python3
import random
import Movement

class Crankshaft_moves(Movement.Movement):
  """ text
  """
#BUG DOUBLON DE LA FONCTION. ON NE SAIT PAS SI LE SECOND RESIDU EST LE +1 OU LE -1
  def mutation(self, structure_grid ):
    attribut = ['column', 'line']
    attribut2 = ['line', 'column']
    for i in range(2):
      # i et i+1 sont sur la meme colonne
      if getattr(self.residu, attribut[i]) == getattr(self.residu.next_res, attribut[i]):
        # i-1 et i+2 sont sur la meme colonne et
        # i et i-1 sont sur la meme ligne et
        # i+1 et i+2 sont sur la meme ligne
        if (getattr(self.residu.previous_res, attribut[i]) == getattr(self.residu.next_res.next_res, attribut[i]) and 
           getattr(self.residu, attribut2[i]) == getattr(self.residu.previous_res, attribut2[i]) and 
           getattr(self.residu.next_res, attribut2[i]) == getattr(self.residu.next_res.next_res, attribut2[i])) :
          # formation en U, chercher les voisins libres sur la meme ligne
          cote = getattr(self.residu.previous_res, attribut[i]) - getattr(self.residu, attribut[i]) 
          if (structure_grid[getattr(self.residu, attribut2[i])][getattr(self.residu.previous_res, attribut[i]) + cote] == -1 and
             structure_grid[getattr(self.residu.next_res, attribut2[i])][getattr(self.residu.next_res.next_res, attribut[i]) + cote] == -1):
             return [{attribut2[i]: getattr(self.residu, attribut2[i]),
                      attribut[i]: getattr(self.previous_res, attribut[i]) + cote},
                     {attribut2[i]: getattr(self.residu.next_res, attribut2[i]),
                      attribut[i]: getattr(self.residu.next_res.next_res, attribut[i]) + cote}, 1]


      for i in range(2):
      # i et i-1 sont sur la meme colonne
        if getattr(self.residu, attribut[i]) == getattr(self.residu.previous_res, attribut[i]):
          # i+1 et i-2 sont sur la meme colonne et
          # i et i+1 sont sur la meme ligne et
          # i-1 et i-2 sont sur la meme ligne
          if (getattr(self.residu.next_res, attribut[i]) == getattr(self.residu.previous_res.previous_res, attribut[i]) and 
             getattr(self.residu, attribut2[i]) == getattr(self.residu.next_res, attribut2[i]) and 
             getattr(self.residu.previous_res, attribut2[i]) == getattr(self.residu.previous_res.previous_res, attribut2[i])) :
            # formation en U, chercher les voisins libres sur la meme ligne
            cote = getattr(self.residu.next_res, attribut[i]) - getattr(self.residu, attribut[i]) 
            if (structure_grid[getattr(self.residu, attribut2[i])][getattr(self.residu.next_res, attribut[i]) + cote] == -1 and
               structure_grid[getattr(self.residu.previous_res, attribut2[i])][getattr(self.residu.previous_res.previous_res, attribut[i]) + cote] == -1):
               return [{attribut2[i]: getattr(self.residu, attribut2[i]),
                        attribut[i]: getattr(self.next_res, attribut[i]) + cote},
                       {attribut2[i]: getattr(self.residu.previous_res, attribut2[i]),
                        attribut[i]: getattr(self.residu.previous_res.previous_res, attribut[i]) + cote}, -1]

    return None


  def __init__(self, res, i):
      Movement.Movement.__init__(self, i)
      self.residu = res
