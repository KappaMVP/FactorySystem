import pymysql

conn = pymysql.connect(host='Localhost',port=3306, user="root",password="",db="test",charset="utf8")

cursor = conn.cursor()

account = "a001"
password = "klp"

find = 'select * from login where account="%s" and password="%s"'%(account,password)
cursor.execute(find)

a = cursor.fetchone()
if (cursor.rowcount==0):
    print("帳密錯誤")
else:
    print(a[1])