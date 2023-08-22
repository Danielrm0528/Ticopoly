#clase de una propiedad 
class propiedad:
    def __init__(self,descripcion,posicion,valor,derechoPaso):
        self.desc = descripcion
        self.pos = posicion
        self.valor = valor
        self.paso = derechoPaso
        self.estado = False
#cambia el estado de comprado 
    def cambiaEstado(self,estado):
        self.estado = estado
#retorna los datos de una propiedad 
    def obtieneDatos(self):
        return {'descripcion': self.desc,'posicion':self.pos,'valor':self.valor,'derechoPaso':self.paso,'estado':self.estado}