from Usuarios.Bank import CuentaBancaria

count = CuentaBancaria(1000, 0.05)
print(count.balance)

count1 = CuentaBancaria()
print(count.balance)

count.deposito( 200 ).deposito( 200 ).deposito( 200 ).retiro( 100 )
print(count.balance)

count.generar_interes()
print(count.balance)

count1.deposito( 100 ).deposito( 100 ).retiro( 100 ).retiro( 100 ).retiro( 100 ).retiro( 100 )
print(count.balance)


