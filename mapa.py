class Mapa:
    def __init__(self, mapa_id):
        self.mapa_id = mapa_id
        self.tamano = (10, 10)
        self.torres_disponibles = [(1, 1), (5, 5), (8, 8)]
        self.camino = None

        if self.mapa_id == 1:
            # Definir el camino del mapa 1
            self.camino = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5),
                           (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)]
        elif self.mapa_id == 2:
            # Definir el camino del mapa 2
            self.camino = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (4, 4),
                           (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2), (9, 3), (8, 3),
                           (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 9), (9, 9)]
        elif self.mapa_id == 3:
            # Definir el camino del mapa 3
            self.camino = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5), (5, 5),
                           (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 9), (8, 9), (9, 9)]
        else:
            raise ValueError("El mapa con el id especificado no existe.")


    def get_closest_target(self, pos)