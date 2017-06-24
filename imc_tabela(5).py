#VARIÁVEIS DE ENTRADA
peso=float(input('Informe o seu peso: '))
alt=float(input('Informe a sua altura: '))
sexo=str(input('Informe o seu sexo: (Digite h ou m) '))

imc=(peso/alt**2)
print('Seu imc é de : %0.2f'%imc)

if sexo == 'h' and imc >= 31:
    print('Voce está acima do peso ideal')
else:
    if sexo == 'h' and imc >= 26.4:
        print('Voce está marginalmente acima do peso')
    else:
        if sexo == 'h' and imc >= 20.7:
            print('Voce está no peso normal')
        else:
            if sexo == 'h' and imc < 20.7:
                print('Voce está abaixo do peso2')


if sexo == 'm' and imc >= 32.3:
    print('Voce está acima do peso ideal')
else:
    if sexo == 'm' and imc >= 25.8:
        print('Voce está marginalmente acima do peso')
    else:
        if sexo == 'm' and imc >= 19.1:
            print('Voce está no peso normal')
        else:
            if sexo == 'm' and imc < 19.1:
                print('Voce está abaixo do peso')

