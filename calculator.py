"""
Calculadora
Autor: Lets Louise
Função: Fazer contas: soma, divisão, multiplicação e subtração
"""
print("Lets Louise Calculator")

sair = False

while sair == False:

	num1 = input("Type your firt number: ")
	num1 = int(num1)
	operador = input("Choose the operator (+-/*): ")
	num2 = input("Type your second number: ")
	num2 = int(num2)

	# + soma
	if operador == "+":
		operação = num1 + num2
	# - substração
	if operador == "-":
		operação = num1 - num2
	# / divisão
	if operador == "/":
		operação = num1 / num2
	# * multiplicação
	if operador == "*":
		operação = num1 * num2

	print("Result: ")
	print(operação)
	teste = input("Would you like to exit? (yes/no): ")
	if teste == "yes":
		sair = True
