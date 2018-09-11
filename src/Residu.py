#! /usr/bin/env python3

class Residu:
  """ text
  """
  def search_freedom_neighbour(self, structure_grid):
    ''' Search for freedom neighbour and return a dictionnaire
        of their coordinates
    '''
    # liste de dico avec les coordonnées des voisins libres
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
      self.hp = hydrophobicity
      self.line = x
      self.column = y
