#Um programa que o usuário informe a Km percorrida e a quantidade de litros abastecidas, o sistema informe o consumo do veículo.
km=float(input("Digite os km percorridos: "))
litros=float(input("Digite os litros abastecidos: "))
consu=km/litros
print("O consumo atual do seu veículo é de", consu," km/l")