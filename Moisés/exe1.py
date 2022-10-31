
nota1 = input("Bem vindo, vamos calcular a média, Digite a primeira nota:")
print("")
nota2 = input("Agora a segunda nota:")
print("")
nota3 = input("Quase lá, finalmente a nota 3:")
print("")

print("A média ponderada com pesos 2, 3 e 5 é...")
nota_final = ((float(nota1) * 2) + (float(nota2) * 3) + (float(nota3) * 5))/10

print(nota_final)
