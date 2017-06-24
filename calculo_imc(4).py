#Faça um algoritmo para efetuar o cálculo do IMC. Sabendo que é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado
#VARIÁVEIS DE ENTRADA
peso=float(input('Informe o seu peso: '))
alt=float(input('Informe a sua altura: '))

imc=(peso/alt**2)
print('Seu imc é de : %0.2f'%imc)

