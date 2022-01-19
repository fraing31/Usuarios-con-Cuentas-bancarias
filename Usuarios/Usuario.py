from Bank import CuentaBancaria

class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address, monto_inicial = 0):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        #self.balance_cuenta = monto_inicial
        self.cuenta = CuentaBancaria(0, 0.02)	

    
    def hacer_deposito( self, amount ):
        self.cuenta.deposito( amount )
        return self 

    def hacer_retiro( self, amount ):
        self.cuenta.retiro( amount )
        return self

    def mostrar_balance_usuario( self ):
        self.cuenta.mostrar_info_cuenta()
        return self
    
    def tranfer_dinero( self, other_user, amount):
        self.hacer_retiro( amount )
        other_user.hacer_deposito( amount )
        return self
