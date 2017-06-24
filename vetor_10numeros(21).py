#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
c=[]
n=9
b=9
v=[]
while n>=0:
    c.append(input('Digite um numero inteiro: '))
    n=n-1
while b>=0:
    v.append(c[b])
    b=b-1
print(v)