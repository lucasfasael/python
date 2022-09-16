n1 = float(input("Qual o primeiro número ? : "))
pn1 = float(input("Qual o peso deste número ? : "))
n2 = float(input("Qual o segundo número ? : "))
pn2 = float(input("Qual o peso deste número ? : "))
n3 = float(input("Qual o terceiro número ? : "))
pn3 = float(input("Qual o peso deste número ? : "))
m = (pn1 * n1 + pn2 * n2 + pn3 * n3) / (pn1 + pn2 + pn3)

print("A média aritmética ponderada destes números com seus respectivos pesos é: {}".format(m))