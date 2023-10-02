from .deck import Mazo
from .player import Jugador


class Partida:
    def __init__(self, nombre1, nombre2, seed=None):
        self.n1 = nombre1
        self.n2 = nombre2
        self.restart(seed)
        
    def restart(self, seed):
        self.mazo = Mazo().reset(seed)
        self.j1 = Jugador(self.j1, self.mazo)
        self.j2 = Jugador(self.j2, self.mazo)
        self.j1.robar(3)
        self.j2.robar(3)



        
