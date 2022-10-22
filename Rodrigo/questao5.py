A = int(input("Digite a primeira medida "))
B = int(input("Digite a segunda medida "))
C = int(input("Digite a terceira media "))

if(A>= B+C or B >= A+C or C>= A+B):
  print("Triângulo inválido")
else:
  print("Triângulo válido")
