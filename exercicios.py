## imprimir a divisão inteira

## numero_1 = int(input('inserir um número inteiro: '))
## numero_2 = int(input('inserir o segundo número inteiro:  '))
## resultado = numero_1 // numero_2
## print(resultado)
## já entende ordem matemática
## import math as ma
## raio = float(input("Digite o Raio: "))
## area_circulo = ma.pi * (raio) ** 2
## print(f"{area_circulo:.2f}")

##if 
nome = (input('qual é o seu nome? '))

if nome.isdigit():
   print('você digitou ao menos um número')
elif len(nome) >= 5:
   print('nome muito grande') 
else:
   print(nome)   
