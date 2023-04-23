from concurrent.futures import ThreadPoolExecutor
import os
import csv

project_dir = os.path.dirname(__file__)
input_file_name = 'input.csv'
input_file = os.path.join(project_dir, input_file_name)
output_file_name = 'output.csv'
output_file = os.path.join(project_dir, output_file_name)

list = []
"""
    r => leitura de conteúdo de arquivos
    w => apaga conteúdo e escreve o que escrever ao abrir arquivo
    a => realiza um append no conteúdo do arquivo 

"""
with open(output_file, 'w', encoding='utf8') as csv_file:
    csv_file.write('Linha 1\n')
    csv_file.write('Linha 2\n')
    csv_file.write('Linha por execução à atenção 4\n')
    csv_file.close()

# remove arquivo 
os.remove(output_file)

with open(output_file, 'w', encoding='utf8') as csv_file:
    csv_file.write('Linha 1\n')
    csv_file.write('Linha 2\n')
    csv_file.write('Linha por execução à atenção 4\n')
    csv_file.close()


# ou
os.unlink(output_file)

