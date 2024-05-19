from math import trunc


class Ruta:
  def __init__(self, tiempo, descanso, coste, esDirigido=True) -> None:
      self.nodos = list()
      self.tiempo = tiempo
      self.descanso = descanso
      self.coste = coste
      self.esDirigido = esDirigido

  '''
  agrega un nodp a la ruta
  @param: node: Node que se agrega
  '''
  def añadirNode(self, nodo):
      self.node.append(nodo)

  '''

  Quita un nodo del graf
  '''
  def borrarNodo(self, node):
      self.nodes.remove(node)

  '''
  Crea una aresta entre dos nodes. Depen de quin tipus de graf tenim
  @param: node1: primer node
  @param node2: segon node
  '''
  def add_edge(self, nodo1, nodo2, cost):
      nodo1_self = self.find_node(nodo1.name)
      nodo2_self = self.find_node(nodo2.name)
      nodo1_self.add_edge(cost, nodo2_self)
      if not self.is_directed:
          nodo2_self.add_edge(cost, nodo1_self)

  '''
  Treu una aresta
  '''
  def remove_edge(self, nodo1, nodo2):
      nodo1_self = self.find_node(nodo1.name)
      nodo2_self = self.find_node(nodo2.name)
      nodo1_self.remove_edge(nodo2_self)
      if not self.is_directed:
          nodo2_self.remove_edge(nodo1_self)

  '''
  Calcula l'ordre del graf
  @return: L'ordre del graf
  '''
  def order(self):
      return len(self.nodes)

  '''
  Calcula la mida d'un graf
  VE DEL SEMINARI 2   
  return: La mida del graf
  '''
  def size(self):
      size = 0
      for node in self.nodes:
          size = size + len(node.edges)
      if not self.is_directed:
          size = trunc(size/2)
      return size

  '''
  Comprova si dos nodes son veins. Si és dirigit, només calcula si es pot arribar al segon node desde el primer
  @param node1: Primer node
  @param node2: Segon node
  '''
  def is_neighbour(self, nodo1, nodo2):
      if nodo2 in nodo1.neigbours():
          return True
      else:
          return False

  '''
  Calcula la sequència gràfica del graf
  @return: La sequència gràfica (ordenada de major a menor)
  '''
  def graphic_sequence(self):
      graphic_seq = list()
      for node in self.nodes:
          graphic_seq.append(node.degree())
      graphic_seq.sort(reverse = True)
      return graphic_seq

  '''
  Donat un nom, busca i retorna el node que hi conincideix
  @param: name: el nom del node a buscar
  @return: El node si el troba, None si no.
  '''
  def find_node(self, name):
      for node in self.nodes:
          if node.name == name:
              return node
      return None
  
