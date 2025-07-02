from database import criar_tabela
from backend import adicionar_contato

criar_tabela()

nome = input("Nome do contato: ")
telefone = input("Entre com o telefone: ")
email = input("Entre com o email: ")

adicionar_contato(nome, telefone, email)
print("Contato adicionado com sucesso !")