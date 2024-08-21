"""Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
Propiedades a la clase Persona:
altura (float): Representa la altura de la persona en metros.
peso (float): Representa el peso de la persona en kilogramos.
Modificar el constructor __init__ para aceptar estos nuevos parámetros y asignarlos a las propiedades
correspondientes.
Agregar un nuevo método para calcular el IMC
El método calcular_imc() debe calcular el Índice de Masa Corporal (IMC) de la persona utilizando la
fórmula (peso/altura^2)
El método debe devolver el valor del IMC y mostrar un mensaje indicando si la persona está en un
rango de peso normal, bajo peso, sobrepeso, u obesidad basado en el valor calculado.
Agregar un método llamado promedio_asignatura() a la clase Persona().
Este método debe recibir tres notas (valores de tipo float) como parámetros.
El método debe calcular el promedio de estas tres notas.
Si el promedio es igual o superior a 4.0, el método debe imprimir un mensaje indicando que la
persona aprobó la asignatura; de lo contrario, debe indicar que la persona no aprobó."""

#Ejercicio 1

class Persona():

    def _init_(self, nombre, apellido, edad, altura, peso, nota1, nota2, nota3):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura 
        self.peso = peso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3


    
    #Atributos(variables)
    nombre = "Cristina"
    apellido = "Torres"
    edad = 23

    #Metodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def calcular_imc(self):
        print(f"Su IMC es de {self.peso/self.altura**2}")
        if (self.peso/self.altura**2) < 18.5:
            print(f"Su IMC se encuentra dentro del rango de bajo peso")
        elif (self.peso/self.altura**2) >= 18.5 and (self.peso/self.altura**2) < 25:
            print(f"Segun su IMC se encuentra normal")
        elif (self.peso/self.altura**2) >= 25 and (self.peso/self.altura**2) < 35:
            print(f"Su IMC se encuentra dentro del rango de obesidad")
        else:
            print(f"Segun su IMC se encuentra dentro del rango obesidad")

    def promedio_asignatura(self):
        print(f"El promedio es {(self.nota1+self.nota2+self.nota3/3)}")
        if ((self.nota1+self.nota2+self.nota3/3))
            print("Asignatura aprobada C:")
        else:
            print("Asignatura reprobada")


#Creacion de un objeto de la clase persona
persona1 = Persona("Cristina", "Torres", 23, 1.58, 61, 5.8, )
#Acceso a los atributos y metodos del objeto
print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad} años")
print(f"{persona1.altura}m")
print(f"{persona1.peso}kg")

#Llamando a los metodos de la clase
persona1.hablar()
persona1.imc()
