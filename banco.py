import random

# Clase para objeto de banco
class Banco:
    def __init__(self, monto, baraja):
        self.baraja = baraja
        self.monto = monto
        self.granAcum = 0

    # Método que realiza cobro a un jugador
    def realizaCobro(self, cant, jug):
        if (jug.acumulado - cant) > 0:
            jug.acumulado -= cant
            self.monto += cant
        elif (jug.acumulado - cant) <= 0:
            jug.acumulado = 0
            self.monto += jug.acumulado

    # Método que realiza pago a un jugador
    def realizaPago(self, cant, jug):
        if (self.monto - cant) > 0:
            jug.acumulado += cant
            self.monto -= cant
        elif (self.monto - cant) <= 0:
            jug.acumulado += self.monto
            self.monto = 0

    # Revisa las propiedades y acumulados y determina el ganador
    def determinaGanador(self, jugadores):
        ganador = jugadores[0]
        empate = []

        for jugador in jugadores:
            if len(jugador.propiedades) > len(ganador.propiedades):
                ganador = jugador
            if len(jugador.propiedades) == len(ganador.propiedades):
                empate += [ganador,jugador] 
        
        if empate:
            for jugador in empate:
                if jugador.acumulado > ganador.acumulado:
                    ganador = jugador
        return ganador

    # Cobra a un jugador pero lo manda al gran acumulado
    def cobraGranAcumulado(self, monto, jug):
        if (jug.acumulado - monto) > 0:
            jug.acumulado -= monto
            self.granAcum += monto
        elif (jug.acumulado - monto) <= 0:
            jug.acumulado = 0
            self.granAcum += jug.acumulado

    # Paga a un jugador el gran acumulado
    def pagaGranAcumulado(self, jug):
        jug.acumulado += self.granAcum
        self.granAcum = 0

    # Saca una carta de la baraja
    def sacarCarta(self, jugador):
        carta = self.baraja[random.randint(0, len(self.baraja) - 1)]
        if carta[1] == 0:
            if carta[2] >= 0:
                self.realizaPago(carta[2], jugador)
            else:
                self.cobraGranAcumulado(abs(carta[2]), jugador)
        if carta[1] == 1:
            jugador.posicion = carta[2]
        return carta

 