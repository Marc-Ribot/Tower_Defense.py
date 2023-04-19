from Recta import*o0


class Segmento(Recta):
    def longitud(self):
      return self.P.distancia(self.Q)


if __name__ == "__main__":
    s = Segmento(Punto([0, 0]), Punto([]))