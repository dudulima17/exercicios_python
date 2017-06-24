nota=int(input('Digite uma nota de 0 a 10 '))
print(nota)
cont=0
while cont <= 10:
    x=int(input('Digite um número '))
    print(x)
    if nota < x or nota > x:
        print('O número é inválido! ')

    if nota == x:
        print('O número é válido! ')
        cont=cont+1
        break
