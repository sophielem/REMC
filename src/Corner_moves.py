#! /usr/bin/env python3
import random
import Movement

class Corner_moves(Movement.Movement):
  """ text
  """

  def mutation(self, structure_grid):
    # Chercher les voisins libres des residus i+1 et i-1
    freedom_neighbour_next = self.residu.next_res.search_freedom_neighbour(structure_grid)
    freedom_neighbour_prev = self.residu.previous_res.search_freedom_neighbour(structure_grid)
    freedom_neighbour_list = []

    # Trouver le voisin libre commun aux residus i+1 et i-1
    for page in freedom_neighbour_prev:
      for page2 in freedom_neighbour_next:
        if page['line'] == page2['line'] and page['column'] == page2['column']:
          freedom_neighbour_list.append(page)
    # Si il y a plusieurs voisins dispo, en choisir un aleatoirement
    if freedom_neighbour_list == []: 
      return None

    random_neighbour = random.randint(0, len(freedom_neighbour_list) - 1)
    return freedom_neighbour_list[random_neighbour]


  def __init__(self, res, i):
      Movement.Movement.__init__(self, i)
      self.residu = res
