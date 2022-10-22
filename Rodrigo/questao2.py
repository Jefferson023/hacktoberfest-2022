horaSalario = int(input("Digite qual o valor da hora de trabalho: "))
horasTrabalhadas = int(input("Digite quantas horas o funcionario trabalhou: "))

cargaHorariaPadrao = 40*4
salarioPadrao = horaSalario*cargaHorariaPadrao
horaExtra = horasTrabalhadas - cargaHorariaPadrao

if(horaExtra>0):
  salario = salarioPadrao + horaExtra*(horaSalario*1.50);
  print(salario)
else:
  print(salarioPadrao)