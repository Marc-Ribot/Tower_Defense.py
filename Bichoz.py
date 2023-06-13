from Mapa_qtdesigner2 import map_matrix
class Bicho:
    def __init__(self, velocitat, hp, damage, shield, pos, recompensa):
        self.vel = velocitat # Assignam a l'atribut vel, el valor de velocitat que ens han passat.
        self.hp = hp
        self.damage = damage
        self.shield = shield
        self.pos = pos
        self.recompensa = recompensa
        self.map_matrix = map_matrix

    ######## GETTERS #########
    def get_velocity(self):
        return self.vel

    def get_hp(self):
        return self.hp

    def get_shield(self):
        return self.shield
    def get_pos(self):
        return self.pos

    def get_damage(self):
        return self.damage

    def get_recompensa(self):
        return self.recompensa
    # completar per la resta d'atributs

    ######## SETTERS #########
    def set_velocity(self, new_vel):
        if new_vel >= 0:
            self.vel = new_vel

    def set_hp(self, new_hp):
        # Cada vegada que volem modificar hp, ens hem d'assegurar que la nova hp no sigui negativa
        # Si la nova hp és negativa, el valor de hp serà 0.
        if new_hp > 0:
            self.hp = new_hp
        else:
            self.hp = 0

    def set_shield(self, new_shield):
        if new_shield > 0:
            self.shield = new_shield
        else:
            self.shield = 0

    # completar per la resta d'atributs




    ##### MÈTODES ADICIONALS #####
    def attacked(self, attack_val):
        # Si un bicho té escut i amb el valor de l'atac es queda fora escut, no li lleva vida. (príncipe oscuro)
        # Alsehores, si un bicho té escut, el valor de l'atack s'aplicarà a l'escut.
        if self.get_shield() > 0: # Si el bicho té escut, hem de modificar la vida de l'escut
            self.set_shield(self.get_shield() - attack_val)
        else:
            self.set_hp(self.get_hp() - attack_val)

    def atacar(self, base):
        if self.get_pos() == base.get_pos():
            base.attacked(self.get_damage())

    def morir(self, bicho,money_manager):
        if self.get_hp() <= 0:
            bicho.remove_bicho(self)
            money_manager.increase_money(self.get_recompensa())

    def move(self, elapsed_time):
        # Obtener las coordenadas x e y actuales del bicho
        x, y = self.pos

        # Calcular el desplazamiento en función de la velocidad y el tiempo transcurrido
        desplazamiento = self.get_velocity()* elapsed_time()

        # Verificar si el desplazamiento excede el tamaño de una casilla
        if desplazamiento >= 1:
            # Obtener la casilla siguiente en el camino
            siguiente_casilla = self.trobarcasella()

        # Verificar si se encontró una casilla siguiente disponible
        if siguiente_casilla is not None:
            # Actualizar la posición del bicho a la siguiente casilla
            self.pos = siguiente_casilla

        # Restar la parte entera del desplazamiento para determinar la fracción de movimiento
        fraccion_movimiento = desplazamiento % 1

        # Actualizar las coordenadas x e y según la fracción de movimiento
        if fraccion_movimiento > 0:
            # Mover el bicho hacia la derecha
            x += fraccion_movimiento

        # Actualizar la posición del bicho
        self.pos = (x, y)
#Aquí el bicho es mourà segons la seva velocitat.


    def trobarcasella(self):
        fila_actual, columna_actual = self.pos
        filas = len(self.map_matrix)
        columnas = len(self.map_matrix[0])

        # Buscar la siguiente casilla disponible avanzando hacia la derecha
        for columna in range(columna_actual + 1, columnas):
            if self.map_matrix[fila_actual][columna] == 1:
                return fila_actual, columna

        # Si no se encuentra ninguna casilla disponible hacia la derecha, intentar moverse hacia arriba o abajo
        for fila in range(fila_actual - 1, -1, -1):
            for columna in range(columnas):
                if self.map_matrix[fila][columna] == 1:
                    return fila, columna

        for fila in range(fila_actual + 1, filas):
            for columna in range(columnas):
                if self.map_matrix[fila][columna] == 1:
                    return fila, columna

    #detectar quina es la següent casella o caselles disponibles






class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    pos_peter = Point(1, 2)
    peter = Bicho(34, 100, 30, 10, pos_peter)
    print("Vida peter: {}\nEscut peter: {}".format(peter.get_hp(), peter.get_shield()))
    peter.attacked(15)
    print("Vida peter: {}\nEscut peter: {}".format(peter.get_hp(), peter.get_shield()))
    peter.attacked(10)
    print("Vida peter: {}\nEscut peter: {}".format(peter.get_hp(), peter.get_shield()))

if __name__ == '__main__':
    main()