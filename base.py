
class Base:
    def __init__(self, hp, pos):
        self.hp = hp # Assignam a l'atribut hp, el valor de velocitat que ens han passat.
        self.pos = pos

    ######## GETTERS #########
    def get_hp(self):
        return self.hp
    def get_pos(self):
        return self.pos

    ######## SETTERS #########

    def set_hp(self, new_hp):
        # Cada vegada que volem modificar hp, ens hem d'assegurar que la nova hp no sigui negativa
        # Si la nova hp és negativa, el valor de hp serà 0.
        if new_hp > 0:
            self.hp = new_hp
        else:
            self.hp = 0

    ##### MÈTODES ADICIONALS #####
    def attacked(self, attack_val):
        self.set_hp(self.get_hp() - attack_val)
