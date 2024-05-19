class Nodo:
  '''
  Constructor del Nodo
  @param: municipio: municipio que representa el nodo
  @param: codINE: codigo INE del municipio
  @param: coste: cuanto tiempo hay que estar la primera vez de la ruta en un municipo
  @param: visitado: si el municipio ya ha sido visitado en la ruta
  @param: poblacion: poblacion del municipio
  @param: x: posición del nodo en x al grafico
  @param: y: posición del nodo en y al grafico
  '''
  def __init__(self, municipio, codINE, coste, visitado, poblacion, vecinos, x=0, y=0) -> None:
      self.municipio = municipio
      self.edges = list()
      self.set_pose(x, y)
      self.codINE = codINE
      self.coste = coste
      self.visitado = visitado
      self.poblacion = poblacion
      self.vecinos = vecinos
