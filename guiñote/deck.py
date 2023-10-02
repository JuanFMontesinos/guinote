import random


class Carta:
    PALOS = ['oros', 'copas', 'espadas', 'bastos']
    VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

    def __init__(self, palo: str, valor: int):
        if palo not in self.PALOS or valor not in self.VALORES:
            raise ValueError(f'Palo o valor no válido: {palo}, {valor}')
        self.palo = palo
        self.valor = valor
        self.es_triunfo = False

    def __repr__(self):
        return f'{self.valor} de {self.palo}'

    def __eq__(self, other):
        if not isinstance(other, Carta):
            return False
        return self.palo == other.palo and self.valor == other.valor

    def __gt__(self, other):
        if not isinstance(other, Carta):
            return False
        if self.es_triunfo and not other.es_triunfo:
            return True
        if not self.es_triunfo and other.es_triunfo:
            return False
        return self.VALORES.index(self.valor) > self.VALORES.index(other.valor)

    def __lt__(self, other):
        return not self.__gt__(other) and self != other

    def set_triunfo(self):
        self.es_triunfo = True
        return self


class Mazo:
    def __init__(self):
        self.reset()

    def __repr__(self):
        return f'Mazo({self.cartas})'

    def reset(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.cartas = [Carta(palo, valor)
                       for palo in Carta.PALOS for valor in Carta.VALORES]
        self.barajar()
        return self

    def barajar(self):
        random.shuffle(self.cartas)

    def cartas_restantes(self):
        return len(self.cartas)

    def robar(self):
        if not self.cartas:
            raise ValueError('No hay más cartas en el mazo para robar')
        return self.cartas.pop()
    
    def is_empty(self):
        return len(self.cartas) == 0
