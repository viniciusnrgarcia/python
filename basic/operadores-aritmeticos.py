"""
https://docs.python.org/3/reference/expressions.html#operator-precedence

/   divisão -> ponto flutuante
//  divisão -> inteiro
**  exponenciação
%   modulo -> resto divisão
"""
print(2 / 3)
print(2 // 3)
print(10 * 10)
print(2 * 3)
print(2 ** 3)
print(10 % 3)
print(2 % 2)
print(100 % 33)
print(10 * 'V.')
print(2 + 2 * 10)
print((2 + 2) * 10)

# Precedência dos operadores aritméticos
print(2 + 5 * 3 ** 2 - (23.5 + 23.5))  # Resultado 0.0
print(3 ** 2)
print(5 * 9)
print(2 + 45)
print(2 + 45)
print(-(23.5 + 23.5))
print(~2, ~3, ~5)
print('A' is 'B')
