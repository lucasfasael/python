ano = int(input("Qual o ano que você nasceu ? : "))
a1 = int(input("Qual ano estamos ? : "))
idade = a1-ano

print("Você tem {} anos".format(idade))
mes = idade*12
print("Em meses são: {}".format(mes))
anos = idade*365
print("Em dias são: {}".format(anos))

