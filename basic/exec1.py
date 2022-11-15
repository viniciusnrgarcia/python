import re


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


text = input('Digite um número inteiro: ')

if text.isnumeric() and int(text) % 2 == 0:
    print(f'Este é um número par: {text}')

elif is_int(text) and int(text) % 2 == 1:
    print(f'Este é um número impar: {text}')

elif is_float(text):
    print(f'Não é um número inteiro: {text}')

else:
    print('Valor não válido: {text} ')

count = 0

while count <= 5:
    horario = input('Digite um horário (0-23): ')
    if horario.isdigit():
        horario = int(horario)

        if horario < 0 or horario > 23:
            print('Horário deve estar entre 0 e 23h')
        else:
            if horario <= 11:
                print('Bom dia')
            elif horario <= 17:
                print('Boa tarde')
            else:
                print('Boa noite')
    else:
        print('Por favor, digite um horário entre 0 e 23.')
    count = count + 1
