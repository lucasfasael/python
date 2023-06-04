import tkinter as tk
from tkinter import messagebox

import requests


# Função para adicionar uma URL à lista
def adicionar_url():
    url = url_entry.get()  # Obtém o valor da Entry de URL
    if url:
        url_listbox.insert(tk.END, url)  # Insere a URL na ListBox
        url_entry.delete(0, tk.END)  # Limpa o campo de entrada de URL

# Função para remover a URL selecionada da lista


def remover_url():
    selecionado = url_listbox.curselection()  # Obtém a posição da URL selecionada
    if selecionado:
        url_listbox.delete(selecionado)  # Remove a URL da ListBox

# Função para editar a URL selecionada na lista


def editar_url():
    selecionado = url_listbox.curselection()  # Obtém a posição da URL selecionada
    if selecionado:
        url_atual = url_listbox.get(selecionado)  # Obtém a URL selecionada
        # Exibe uma janela de diálogo para editar a URL
        nova_url = tk.simpledialog.askstring(
            "Editar URL", "Digite a nova URL:", initialvalue=url_atual)
        if nova_url:
            url_listbox.delete(selecionado)  # Remove a URL atual da ListBox
            # Insere a nova URL na mesma posição
            url_listbox.insert(selecionado, nova_url)

# Função para testar a URL selecionada na lista


def testar_url_selecionada():
    selecionado = url_listbox.curselection()  # Obtém a posição da URL selecionada
    if selecionado:
        url = url_listbox.get(selecionado)  # Obtém a URL selecionada
        try:
            # Faz uma solicitação GET à URL usando a biblioteca requests
            response = requests.get(url)
            if response.status_code == 200:
                # Exibe uma mensagem informando que a URL está ativa
                messagebox.showinfo("URL Testada", f"A URL {url} está ativa!")
            else:
                # Exibe uma mensagem informando o código de status retornado pela URL
                messagebox.showwarning(
                    "URL Testada", f"A URL {url} retornou um código de status {response.status_code}!")
        except requests.exceptions.RequestException:
            # Exibe uma mensagem de erro caso não seja possível acessar a URL
            messagebox.showerror(
                "URL Testada", f"A URL {url} não pôde ser acessada!")

# Função para limpar a lista de URLs


def limpar_lista():
    url_listbox.delete(0, tk.END)  # Remove todos os itens da ListBox


# Cria a janela principal
root = tk.Tk()
root.title("Lista de URLs")

# Frame para a entrada de URL
url_frame = tk.Frame(root)
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="URL:")
url_label.grid(row=0, column=0)

url_entry = tk.Entry(url_frame)
url_entry.grid(row=0, column=1)

adicionar_button = tk.Button(
    url_frame, text="Adicionar", command=adicionar_url)
adicionar_button.grid(row=0, column=2, padx=10)

remover_button = tk.Button(url_frame, text="Remover", command=remover_url)
remover_button.grid(row=0, column=3, padx=10)

editar_button = tk.Button(url_frame, text="Editar", command=editar_url)
editar_button.grid(row=0, column=4)

testar_button = tk.Button(
    url_frame, text="Testar URL Selecionada", command=testar_url_selecionada)
testar_button.grid(row=0, column=5)

# Frame para a lista de URLs
lista_frame = tk.Frame(root)
lista_frame.pack(pady=10)

url_listbox = tk.Listbox(lista_frame, width=50)
url_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(lista_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

url_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=url_listbox.yview)

limpar_button = tk.Button(root, text="Limpar Lista", command=limpar_lista)
limpar_button.pack(pady=10)

root.mainloop()
