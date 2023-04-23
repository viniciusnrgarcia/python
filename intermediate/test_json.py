

import json
import os


project_dir = os.path.dirname(__file__)
input_file_name = 'test_json.json'
input_file = os.path.join(project_dir, input_file_name)


pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Garcia',
    'idade': 34,
    'telefones': [
        {'ddd': '11', 'numero': '99999-9999'},
        {'ddd': '11', 'numero': '99999-9999'}
    ]
}


with open(input_file, 'w') as f:
    json.dump(pessoa,
               f,
               ensure_ascii=False,
               indent=2)


with open(input_file, 'r', encoding='utf8') as f2:
    item = json.load(f2)
    print(item)
    print(item['nome'], item['telefones'][0]['ddd'], item['telefones'][0]['numero'])

