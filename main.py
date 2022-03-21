COLORES_ACEPTABLES = ["rojo", "verde", "amarillo", "negro", "blanco"]    

class Asiento:
    
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        if color in COLORES_ACEPTABLES:
            self.color = color

class Motor:
    
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo=tipo
    
    

class Auto:
    
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        ContadorAsientos = 0
        for i in self.asientos:
            if isinstance(i, Asiento)==True:
                ContadorAsientos += 1
        return ContadorAsientos
    
    def verificarIntegridad(self):
        Autenticidad=1
        for i in self.asientos:
            if isinstance(i, Asiento)==True:
                if i.registro == self.motor.registro == self.registro:
                    continue
                else:
                    Autenticidad=0
                    
        if Autenticidad==0:
            return("Las piezas no son originales")
        else:
            return("Auto original")