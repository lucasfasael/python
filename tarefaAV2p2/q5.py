temperaturas = []
meses = []
mesesDoAno = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for index,mes in enumerate(mesesDoAno):
    temperatura = float(input("Qual a temperatura do {}º  mês ? : ".format(index+1)))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print("\n A média anual é de : {} \n".format(media))
print("Estão com a temperatura da média os meses de : \n")

for index,mes in enumerate(mesesDoAno):
    if(temperaturas[index] > media):
        print(index+1,"-", mes,":", temperaturas[index])