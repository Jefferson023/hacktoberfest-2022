lado1 = float(input("Digite a medida do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print("É um triângulo")
else:
    print("Não é um triângulo")
