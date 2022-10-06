n1 = int(input("Me diga um número inteiro : "))
n2 = int(input("Me diga outro número inteiro : "))


if(n1 < n2):
    cont = n1 + 1;
    while cont < n2:
        print("Os números inteiros que estão entre o intervalo selecionado são: {}".format(cont))
        cont = cont + 1;

if(n2 < n1):
    cont = n2 + 1;
    while (cont < n1):
        print("Os números inteiros que estão entre o intervalo selecionado são: {}".format(cont))
        cont = cont + 1;
