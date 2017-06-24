cont=0
while cont >= 0:
    nome = input('Digite o nome do usuário: ')
    print(nome)
    senha = input('Digite a senha do usuário: ')
    print(senha)
    if senha == nome:
        print('erro! Tente novamente')
    if senha != nome:
        print('Dados computados')
    cont=cont+1


