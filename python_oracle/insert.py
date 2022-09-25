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
 Save customers
"""
cursor = conn.cursor()
elapsed_time = time.perf_counter()

c = 1
for item in range(100000):
    n = "Test {} ".format(c)
    t = datetime.datetime.now()
    cursor.execute("""
               INSERT INTO customer (customer_id,
               name,
               last_name,
               affiliation,
               customer_type,
               created_at,
               user_creation,
               modified_at,
               user_modified
               ) VALUES (seq_customer_id.nextval,
                :name,
                :last_name,
                :affiliation,
                :customer_type,
                sysdate,
                :user_creation,
                sysdate,
                :user_modified)
          """,
                   name=n,
                   last_name=n,
                   affiliation=t,
                   customer_type='10',
                   user_creation='user_system_test',
                   user_modified='user_system_test'
                   )
    c += 1

cursor.close()

print('Elapsed time during the whole program in seconds: ', time.perf_counter() - elapsed_time)

conn.commit()
conn.close()
