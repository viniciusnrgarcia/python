"""
Entrada de dados do usuário
"""
import datetime

nome = input("Qual seu nome? Resposta: ")
idade = int(input("Qual sua idade? Resposta: "))
ano_atual = datetime.date.today().year

print(f'\nO usuário digitou "{nome}" e o tipo da variável é f{type(nome)}')
print('Ano de nascimento: {}'.format(ano_atual - int(idade)))
