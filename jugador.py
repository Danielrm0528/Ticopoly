import pygame
#clase de jugador 
class Player:
    def __init__(self, nombre, posicion, color,cell_size):
        self.nombre = nombre
        self.posicion = posicion
        self.rect = pygame.Rect(0, 0, cell_size // 2, cell_size // 2)
        self.color = color
        self.acumulado = 0
        self.propiedades = []
        self.carcel = False
        self.turnosCarcel = 0
#mueve al jugador de casilla
    def move(self, dice_value):
        self.posicion = (self.posicion + dice_value - 1) % 24 + 1
    def realizaCompra(self,propiedad,banco):
        self.acumulado -= propiedad.valor
        banco.monto += propiedad.valor
        self.propiedades += [propiedad]
        propiedad.cambiaEstado(True)
#paga el derecho de paso a alguna propiedad 
    def pagaPaso(self,propiedad,duenno):
        if (self.acumulado - propiedad.paso) > 0:
            self.acumulado -= propiedad.paso
            duenno.acumulado += propiedad.paso
        else:
            duenno.acumulado += self.acumulado
            self.acumulado = 0
#cobra 
    def cobra(self,monto):
        self.acumulado += monto
#cobra a un jugador 
    def cobraJug(self,monto,jug):
        if (jug.acumulado - monto) > 0:
            self.acumulado += monto
            jug.acumulado -= monto
        else:
            self.acumulado += jug.acumulado
            jug.acumulado = 0



