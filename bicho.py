class Bicho:
    def __init__(self, velocitat, hp, damage, shield, pos, recompensa):
        self.vel = velocitat # Assignam a l'atribut vel, el valor de velocitat que ens han passat.
        self.hp = hp
        self.damage = damage
        self.shield = shield
        self.pos = pos

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