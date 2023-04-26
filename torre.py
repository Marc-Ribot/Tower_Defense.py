import math


class Torre:
    def __init__(self, damage, rof, pos, preu, venta, rango): # Rof es rate of fire o velocitat d'atac.
        self.rof = rof
        self.damage = damage #mal per atac
        self.preu = preu  #preu de compra
        self.venta = venta #preu de venta
        self.pos = pos
        self.rango = rango
        self.ultimo_ataque = 0  # Tiempo del último ataque (para controlar la velocidad de ataque)

        ######## GETTERS #########

    def get_damage(self):
        return self.damage

    def get_rof(self):
        return self.rof

    def get_preu(self):
        return self.preu

    def get_pos(self):
        return self.pos

    def get_venta(self):
        return self.venta

    def get_rango(self):
        return self.rango


    #mètodes

    def distance(self, bicho):
        return math.sqrt((self.pos[0] - bicho.get_pos()[0]) ** 2 + (self.pos[1] - bicho.get_pos()[1]) ** 2)
        #mòdul de distància entre posició bicho y torre
    def atacar(self, bicho):
        # Verificar si el enemigo está dentro del rango de ataque
        if self.distance(bicho) <= self.get_rango():
            # Verificar si la torre está lista para atacar de nuevo  necessitam definir tot lo referent
            #a temps
            tiempo_actual = time.time()
            if tiempo_actual - self.ultimo_ataque >= 1 / self.vel_ataque:
                # Realizar el ataque
                bicho.attacked(self.get_damage())
                self.ultimo_ataque = tiempo_actual