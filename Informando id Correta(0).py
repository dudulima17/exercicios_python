#Faça um algoritmo que leia a data de nascimento(dia, mês e ano), e informe a idade correta
#VARIÁVEIS DE ENTRADA
dia=int(input('Informe o dia em que você nasceu: '))
mes=int(input('Informe o mes em que você nasceu: '))
ano=int(input('Informe o ano em que você nasceu: '))
mes_atual=int(input('Informe o mes atual: '))

#PROCESSAMENTO
x=(2017-ano)
if mes_atual < mes:
    print(x-1)  #SAÍDA
else:
    print(x)  #SAÍDA




