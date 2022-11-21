import time
from pymongo_get_database import get_database
dbname = get_database()

cancel = dbname["cancel"]
transaction = dbname["transaction"]

start_time = time.time()

file = open('/tmp/result.csv', 'w')

count = 0
cancel_details = cancel.find()

header = 'TIPO_PRODUTO;DATA_LIQUIDACAO_VENDA;DATA_TRANSACAO_VENDA;ID_VENDA;NSU_TRANSACAO;PARCELA_TRANSACAO;NUMERO_PARCELA;VALOR_BRUTO_PARCELA;CODIGO_AUTORIZACAO;ARQUIVO;NSU_CANCELAMENTO;ID_CANCELAMENTO;DATA_CANCELAMENTO;CODIGO_AUTORIZACAO_CANCELAMENTO;VALOR_BRUTO_PARCELA_CANCELAMENTO;ARQUIVO_CANCELAMENTO\n'
file.write(header)

# csv manual builder
for item in cancel_details:
    t1 = transaction.find_one({'nsu': item['nsuTrace']})
    count = count+1
    print(count)
    line = ''
    if t1 is not None:
        product_type = ''
        if t1['cdProductType'] == 'C':
            product_type = 'Credito'
        else:
            'Débito'
        line = f"{product_type};{t1['dtSettlement']};{t1['dtBatch']};{t1['_id']};{t1['nsu']};{t1['nuInstallmentSequence']};{t1['vlInstallmentGross']};{t1['vlInstallmentGross']};{t1['authorizationCode']};{t1['fileName']};{item['nsu']};{item['_id']};{item['dtBatch']};{item['authorizationCode']};{item['vlInstallmentGross']};{item['fileName']}\n"
    else:
        line = f" ; ; ; ; ; ; ; ; ; ;{item['nsu']};{item['_id']};{item['dtBatch']};{item['authorizationCode']};{item['vlInstallmentGross']};{item['fileName']}\n"

    file.write(line)

file.close()
print(f'--- Process time: {(time.time() - start_time)} seconds ---')
