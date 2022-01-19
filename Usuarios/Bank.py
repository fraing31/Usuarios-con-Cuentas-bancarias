class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    nombre_banco = "Coding Dojo National"

    def __init__(self, monto_inicial = 0, interes_inicial = 0.01 ): 
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        self.balance = monto_inicial
        self.tasa_interes = interes_inicial
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def deposito(self, amount):
        self.balance += amount
        return self 

    def retiro(self, amount):
        if amount >= self.balance:
            print( "Fondos insuficientes: cobrando una tarifa de $5")
            self.balance = self.balance - 5
        if amount < self.balance:
            self.balance -= amount
        return self 

    def mostrar_info_cuenta(self):
        print(self.balance)
        return self 

    def generar_interes(self):
        self.balance = self.balance + (self.balance * self.tasa_interes)
        return self 

