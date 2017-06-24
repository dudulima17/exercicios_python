n=int(input("Digite um numero entre 0 a 10 "))
print(n)
y=1
cont=0
while cont <= 10:
    x=int(input("Digite seu palpite "))
    print(x)
    if x > n:
        print("Esse numero é maior que o alocado na memoria")
        y=y+1
    if x < n:
        print("Esse numero é menor que o alocado na memoria")
        y=y+1
    if x==n:
        print("Você achou a combinação certa!")
        print("Foram", y, "tentativas até você acertar")
        cont=cont+1
        break
