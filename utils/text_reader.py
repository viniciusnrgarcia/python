import json

f = open('/home/ubuntu-python/python-workspace/utils/input2.json', 'r')

# data = json.loads(f.read())

# for i in data['list']:
#     print(i)

data = f.readlines()
for i in data:
    if "vlInstallmentGross" in i:
        # print(i)
        #  print(i[-12:-1] + ',')
        print(i[23:-2].replace('.', ','))

f.close()



