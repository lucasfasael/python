#rodar esse app
#precisa importar o requests

from tkinter import *
from tkinter import ttk

import requests
import services


def delete(event):
    if (tabela.item(tabela.focus())["values"] == ''):
        return
    click = tabela.item(tabela.focus())["values"][0]
    services.remove(click)
    popularTabela()


def popularTabela():
    for item in tabela.get_children():
        tabela.delete(item)

    for index, url in enumerate(services.findAll()):
        if (services.validatorURL(url)):
            tabela.insert("", END, text=index+1, value=(url))
        else:
            tabela.insert("", END, text=index+1, value=(url), tags=("erro"))


def insertTabela():
    if entrada.get().strip() == "":
        return
    else:
        services.create(entrada.get())
        popularTabela()
        entrada.delete(0, END)


janela = Tk()


janela.title("Validador de URLS")


# BOTÃO AQUI


botao = Button(janela, text="ADICIONAR/VALIDAR URL", command=insertTabela)


# TABELA CÁ


tabela = ttk.Treeview(janela, selectmode="browse", column=(


    "column1"), show="headings")


tabela.column("column1", width=500, minwidth=50, stretch=NO)


tabela.heading("#1", text="URL")


tabela.bind("<<TreeviewSelect>>", delete)

# ENTRADA INPUT
entrada = Entry(janela, width=100)

botao.grid(column=0, row=3, padx=0)
texto_orientacao = Label(janela, text="Para deletar clique na URL !!!")
texto_orientacao.grid(column=0, row=0, padx=0)
entrada.grid(column=0, row=2, padx=1)
tabela.tag_configure("erro", background="red")
tabela.grid(row=1, column=0)


# funções da UI


popularTabela()


janela.mainloop()
