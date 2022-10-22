contaCliente = int(input("Digite o numero da conta do cliente: "))
saldo = float(input("Digite o saldo do cliente: "))
debito= float(input("Digite o débito do cliente: "))
credito = float(input("Digite o crédito do cliente: "))
saldoAtual = saldo - debito + credito

if(saldoAtual < 0):
  print("Saldo negativo\n",saldoAtual)
elif(saldoAtual == 0):
  print("Saldo igual a 0")
else:
  print("Saldo positivo\n",saldoAtual)