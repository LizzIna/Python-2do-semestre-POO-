class SistemaVenta:

    descuento_grupo = 0.20
    
    def __init__(self):
        self.__tickets = {}
        self.__ventas = []
    
    #agrega un tipo de ticket al sistema
    def agregar_ticket(self, tipo, precio):
        assert precio > 0, "El precio del ticket debe ser positivo."
        self.__tickets[tipo] = precio
    
    #registra la venta de tickets
    def registrar_venta(self, tipo, cantidad):
        assert tipo in self.__tickets, "El tipo de ticket no existe."
        assert cantidad > 0, "La cantidad de tickets debe ser positiva."
        self.__ventas.append((tipo, cantidad))
    
    #calcula el total de una venta considerando el descuento de grupo
    @staticmethod
    def calcular_total(precio, cantidad, aplicar_descuento=False):
        total = precio * cantidad
        if aplicar_descuento:
            total *= (1 - SistemaVenta.descuento_grupo)
        return total
    
    #calcular los ingresos totales
    def calcular_ingresos_totales(self):
        total_ingresos = 0
        for tipo, cantidad in self.__ventas:
            precio = self.__tickets[tipo]
            total_ingresos += SistemaVenta.calcular_total(precio, cantidad, cantidad > 5)  #Descuento por más de 5 tickets
        return total_ingresos

class Gimnasio:
    #Descuento para suscripciones anuales (variable de clase)
    descuento_anual = 0.10
    
    def __init__(self, nombre, tipo_suscripcion, costo):
        self.nombre = nombre  #público
        self.__tipo_suscripcion = tipo_suscripcion  #privado
        self.__costo = costo  #privado
        assert costo > 0, "El costo de la suscripción debe ser positivo."
    
    #Getters y Setters
    @property
    def tipo_suscripcion(self):
        return self.__tipo_suscripcion
    
    @tipo_suscripcion.setter
    def tipo_suscripcion(self, tipo):
        assert tipo in ["mensual", "trimestral", "anual"], "Tipo de suscripción inválido."
        self.__tipo_suscripcion = tipo
    
    @property
    def costo(self):
        return self.__costo
    
    @costo.setter
    def costo(self, nuevo_costo):
        assert nuevo_costo > 0, "El costo de la suscripción no puede ser negativo."
        self.__costo = nuevo_costo
    
    #calcula el costo final con descuento de bienvenida
    @staticmethod
    def aplicar_descuento_bienvenida(costo, descuento_bienvenida):
        assert descuento_bienvenida >= 0, "El descuento no puede ser negativo."
        return costo * (1 - descuento_bienvenida)
    
    #aplicar descuento en suscripción anual
    def aplicar_descuento_anual(self):
        if self.__tipo_suscripcion == "anual":
            self.__costo *= (1 - Gimnasio.descuento_anual)

#sistema de venta de tickets
sistema = SistemaVenta()

#agrega los tipos de tickets
sistema.agregar_ticket("General", 5000)
sistema.agregar_ticket("VIP", 10000)

#registra las ventas
sistema.registrar_venta("General", 3)
sistema.registrar_venta("VIP", 6)

#ingresos totales con descuento por más de 5 tickets en la venta VIP
ingresos_totales = sistema.calcular_ingresos_totales()
print(f"Ingresos totales: ${ingresos_totales:.2f}")

#gimnasio con suscripción mensual
gimnasio = Gimnasio("FitLife", "mensual", 30000)

#cambiar el tipo de suscripción
gimnasio.tipo_suscripcion = "anual"
print(f"Tipo de suscripción: {gimnasio.tipo_suscripcion}")

#aplicar descuento anual
gimnasio.aplicar_descuento_anual()
print(f"Costo después de descuento anual: ${gimnasio.costo:.2f}")

#aplicar descuento de bienvenida
costo_con_descuento_bienvenida = Gimnasio.aplicar_descuento_bienvenida(gimnasio.costo, 0.05)
print(f"Costo después de descuento de bienvenida: ${costo_con_descuento_bienvenida:.2f}")
