hora_maxima = 24 * 28
horas = float(input("Informe o total de horas trabalhadas nesse mês... E não tente passar migué não, a gente sabe quantas horas existem num mês: "))
print("")
por_hora = float(input("Agora informe os seus ganhos por hora trabalhada: "))
print("")

print("Calculando...")

if 0 < horas < hora_maxima:
    if horas > 40:
        total = (40*por_hora) + ((horas - 40) * (por_hora + (por_hora / 2)))
    else:
        total = (horas*por_hora)

    print("Você irá receber... " + str(total) + " reais, que bufunfa hein.")
else:
    print("Eu disse pra pôr uma hora válida meu véi, saia daqui, saia...")

