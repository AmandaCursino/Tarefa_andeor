#3
idade = int(input("Informe sua idade: "))
autorização = input("Tem autorização dos pais?: ")

if idade >= 18 or autorização == "sim":
    print("Você pode entrar! ")
else:
    print("Você não pode entrar! ")