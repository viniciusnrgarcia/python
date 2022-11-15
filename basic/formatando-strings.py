from datetime import datetime

nome = 'Vinicius'
idade = 34
altura = 1.88
peso = 100
maior_idade = idade > 18
data_atual = datetime.today()
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('Nome {0}, {0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))

t: str = 'Exemplo de log com informaçoẽs {0}'

print(t.format('Texto'))
