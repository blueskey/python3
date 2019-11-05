import pymysql

db=pymysql.connect(host="localhost",db="study",user="root",passwd="123456",charset ="utf8")

cursor = db.cursor()

# sql = 'insert into author(name,dynasty,introduction) values(%s,%s,%s);'
# data = [
#     ('杜牧', '唐',''),
#     ('陆游', '南宋','')
# ]
# #拼接并执行sql语句
# cursor.executemany(sql, data)
# # 涉及写操作要注意提交
# db.commit()

cursor.execute("select * from author")


data=cursor.fetchall()
for d in data:
    print(d)


# 获取最新的那一条数据的ID
last_id = cursor.lastrowid
print("最后一条数据的ID是:", last_id)
cursor.close()
db.close()
