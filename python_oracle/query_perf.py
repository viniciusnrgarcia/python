import datetime

import cx_Oracle
import time

from python.python_oracle.customer import Customer

url = 'SYS/MyPasswd123@localhost:1521/OraDoc'

dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='OraDoc')
conn = cx_Oracle.connect(user='vinicius', password='123456', dsn=dsn)

"""
get customers
"""
print('---- Testing read with fetch size ---- ')

t2 = time.perf_counter()
cursor = conn.cursor()

"""
The best Cursor.arraysize and Cursor.prefetchrows values can be found by experimenting with your application 
under the expected load of normal application use. 
This is because the cost of the extra memory copy from the prefetch buffers when fetching a large quantity of rows 
or very “wide” rows may outweigh the cost of a round-trip for a single cx_Oracle user on a fast network. 
However under production application load, the reduction of round-trips may help performance and overall 
system scalability. The documentation in round-trips shows how to measure round-trips.
"""
cursor.arraysize = 2000
cursor.prefetchrows = 1000

cursor.execute("""
         select customer_id, 
            name,
            last_name,
            affiliation,
            customer_type,
            created_at,
            user_creation,
            modified_at,
            user_modified 
           from customer
     """).fetchall()

result2 = []
for customer_id, name, last_name, affiliation, \
        customer_type, created_at, user_creation, modified_at, user_modified in cursor:
    c = Customer.__init__(customer_id,
                        name,
                        last_name,
                        affiliation,
                        customer_type,
                        created_at,
                        user_creation,
                        modified_at,
                        user_modified)
    result2.append(c)
    # print("Values:", )

print(f'Size collection {len(result2)}')

cursor.close()
print('Elapsed time during the whole program in seconds: ', time.perf_counter() - t2)


"""
get customers
"""
print('---- Testing read without fetch size ---- ')
t = time.perf_counter()
cursor = conn.cursor()
cursor.execute("""
         select customer_id, 
            name,
            last_name,
            affiliation,
            customer_type,
            created_at,
            user_creation,
            modified_at,
            user_modified 
           from customer
     """)

result = []
for customer_id, name, last_name, affiliation, \
        customer_type, created_at, user_creation, modified_at, user_modified in cursor:
    c = Customer.__init__(customer_id,
                        name,
                        last_name,
                        affiliation,
                        customer_type,
                        created_at,
                        user_creation,
                        modified_at,
                        user_modified)
    result.append(c)
    # print("Values:", )

print(f'Size collection {len(result)}')

result.clear()

cursor.close()
print('Elapsed time during the whole program in seconds: ', time.perf_counter() - t)

#######################################

print('--- Closed connection --- ')
conn.close()

