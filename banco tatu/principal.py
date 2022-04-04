from cliente import Cliente
from contas import contas

joao = Cliente(nome="João Luiz Pilger", cpf="086946050-76", telefone="54-993240754", data_nascimento="12/03/2000")
maria = Cliente(nome="Maria Madagascar", cpf="567093173-09", telefone="54-997654587",data_nascimento="10/10/1998")

joao.imprime_dados_cliente()
maria.imprime_dados_cliente()

conta_joao = contas(joao, 2000)
