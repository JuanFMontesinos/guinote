from .exceptions import *
import re

OROS = ['oros', 'o', 'oro']
BASTOS = ['bastos', 'b', 'basto']
COPAS = ['copas', 'c', 'copa']
ESPADAS = ['espadas', 'e', 'espada']
PALOS = OROS + BASTOS + COPAS + ESPADAS

class Jugador:
    def __init__(self, nombre: str, mazo):
        self._mazo = mazo
        self.nombre = nombre
        self.cartas = {}
        self.puntos = 0

    def robar(self, n=1):
        for _ in range(n):
            carta = self._mazo.robar()
            self.cartas[(carta.palo, carta.value)] = carta
        return self

    def print_mano(self):
        # Preparar las líneas de cada carta
        # Suponiendo que cada carta tiene 5 líneas
        lineas_cartas = [[] for _ in range(5)]
        for carta in self.cartas:
            # Tomar la primera letra del palo
            palo_char = carta.palo[0].upper()
            lineas_cartas[0].append(" _____  ")
            lineas_cartas[1].append(f"|     | ")
            lineas_cartas[2].append(f"|  {palo_char}  | ")
            lineas_cartas[3].append(
                f"|  {carta.valor}  | " if carta.valor > 9 else f"|  {carta.valor}  | ")
            lineas_cartas[4].append("|_____| ")

        # Imprimir cada línea de todas las cartas
        for lineas_carta in lineas_cartas:
            print(''.join(lineas_carta))

    def poner_carta(self, carta: str):
        def card_value(carta: str):
            matches = re.findall(r'\d+', carta)
            if len(matches) > 1:
                raise InvalidCard(
                    'Varios valores detectados:' + ' '.join(matches))
            elif len(matches) == 0:
                raise InvalidCard('No se detectó ningún valor en la carta')

            # Si la entrada es válida, extrae y retorna el número
            numero = int(matches[0])

            return numero
        def card_palo(carta: str):
            carta_lower = carta.lower()
            for palo in PALOS:
                if palo in carta_lower:
                    return palo
            raise InvalidCard(f'Palo no detectado en la carta {carta}')
        
        val = card_value(carta)
        palo = card_palo(carta)
        key = (palo, val)
        if key not in self.cartas:
            raise InvalidCard(f'La carta {carta} no está en la mano')
        return self.cartas.pop(key)
    
