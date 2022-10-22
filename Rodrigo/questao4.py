lista = []

for i in range(3):
  lista.append(int(input("Digite um numero: ")))
  
for j in range(2):
  for i in range(2):
    if(lista[i]>lista[i+1]):
      aux = lista[i]
      lista[i] = lista[i+1]
      lista[i+1] = aux


for i in range(3):
  print(lista[i])