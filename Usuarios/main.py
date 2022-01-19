from Usuario import Usuario
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
irving = Usuario("Irving Cardenas", "cisco120988@python.com", 500)
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(irving.name)

guido.hacer_deposito( 100 ).hacer_deposito( 200 ).hacer_deposito( 300 ).hacer_retiro( 200 ).mostrar_balance_usuario()

monty.hacer_deposito( 200 ).hacer_deposito( 100 ).hacer_retiro( 100 ).hacer_retiro( 200 ).mostrar_balance_usuario()

irving.hacer_deposito( 100 ).hacer_retiro( 100 ).hacer_retiro( 100 ).hacer_retiro( 100 ).tranfer_dinero( guido, 200).mostrar_balance_usuario()


