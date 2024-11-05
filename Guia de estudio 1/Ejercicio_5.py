class Planta:
    estado_semilla = "semilla"
    estado_brote = "brote"
    estado_adulto = "adulta"

    def __init__(self, nombre, estado=estado_semilla):
        self.nombre = nombre
        self.estado = estado

    def __str__(self):
        return f"Planta: {self.nombre}, Estado: {self.estado}"

    def crecer(self):
        if self.estado == self.estado_semilla:
            self.estado = self.estado_brote
        elif self.estado == self.estado_brote:
            self.estado = self.estado_adulto

planta = Planta("rosa")
print(planta)

#Hacerla crecer
planta.crecer()
print(planta)

#Hacerla crecer de nuevo
planta.crecer()
print(planta)
