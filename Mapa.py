from BD import BD
import json
class Mapa:

    MAX_TIEMPO = 28800
    DEESCANSO = 3600

    def __init__(self, cantidad_de_zonas: int) -> None:
        self.regiones = list()
        self.rutas = list()
        self.bd = BD()
        self.bd.conexion()

        for i in range(cantidad_de_zonas):
            nombreRuta = f"Ruta{i}"
            self.bd.crearRuta(nombreRuta)

    
    def rellenarBd(self, rutaTxt, rutaBd):
        with open(rutaTxt, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f):
                # Separar la línea por comas
                municipio, codINE, bloc, poblacion, estanciaMin = linea.strip().split(',')
                
                '''print(municipio)
                print(codINE)
                print(bloc)
                print(poblacion)
                print(estanciaMin)'''
                # Insertar los datos en la base de datos
                self.bd.insertarNodo(rutaBd, i, municipio, codINE, bloc, poblacion, estanciaMin)
