# Nome: Arthur Cei Corrêa
# RM: 97781

total = 0
for month in range(1, 13, 1):
    value = float(input(f"Informe a quantidade coletada em toneladas no {month}º mês do ano: "))
    print(f"\nPerda manual..............: {value * 0.05:.2f}")
    print(f"\nPerda com máquina.........: {value * 0.15:.2f}\n")
    total += value

print(f"\nColheita do ano: {total:.2f}")
print(f"\nProjeção de desperdício:"
      f"\nManual.........................: {total * 0.05:.2f}"
      f"\nCom Máquina....................: {total * 0.15:.2f}\n")