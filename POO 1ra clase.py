#class Persona():   #Todos los nombres de clase deben llevar mayuscula al principio.
    #Bloque de codigo

    #Atributos

    #Metodos

#Eemplo
class Persona():
    #Atributos(variables)
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23

    #Metodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

#Creacion de un objeto de la clase persona
persona1 = Persona()

#Acceso a los atributos y metodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

#Llamando a los metodos de la clase
persona1.hablar()
persona1.caminar()
