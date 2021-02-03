import pymysql
import 接口
#   链接数据库
db = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "WZl496085235",
    database = "test",
    charset = "utf8"
)

cur = db.cursor()

cur.execute(sql)

#   打印查询结果
end = cur.fetchall()
for i in end:
    print(i)
#  提交至数据库执行
db.commit()

#    关闭游标
cur.close()

