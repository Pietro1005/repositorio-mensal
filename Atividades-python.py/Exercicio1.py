def soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)  
    return soma

numero = input("Digite um número inteiro: ")

if numero.isdigit(): 
    print(f"A soma dos dígitos do número {numero} é: {soma_digitos(numero)}")
else:
    print("Valor inválido! Por favor, insira um número inteiro.")
