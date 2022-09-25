import cx_Oracle

url = 'SYS/MyPasswd123@localhost:1521/OraDoc'

conn = cx_Oracle.connect(url)
cur = conn.cursor()

# do something like fetch, insert, update, etc.

cur.close()
conn.close()

