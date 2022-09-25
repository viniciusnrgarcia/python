import datetime

import cx_Oracle
import time

url = 'SYS/MyPasswd123@localhost:1521/OraDoc'

dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='OraDoc')
conn = cx_Oracle.connect(user='vinicius', password='123456', dsn=dsn)

cursor = conn.cursor()

# do something like fetch, insert, update, etc.
cursor.execute("""
    select sysdate from dual
""")

for i in cursor:
    print("Values:", i)

cursor.close()

"""
get customers
"""
t = time.perf_counter()
cursor = conn.cursor()
cursor.execute("""
         select customer_id, name, created_at from customer
     """)

for customer_id, name, created_at in cursor:
    print("Values:", customer_id, name, created_at)

cursor.close()
print('Closed connection')

conn.commit()
print('Elapsed time during the whole program in seconds: ', time.perf_counter() - t)

conn.close()
