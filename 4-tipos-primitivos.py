"""
Tipos de dados

str - string "Texto" 'Texto'
int - inteiro 123456 -123456
float - real/ponto flutuante 10.50 0.0 2.0
bool - boolean/lógico True/False
"""
print(type('Vinicius'), type(123456), type(0.0), type(True))

t: str = "Texto"

if type("Texto") == type(t):
    print("Foi")
