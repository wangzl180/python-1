# import pymysql
#
#
# db = pymysql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = 'WZl496085235',
#         database = 'test',
#         charset = 'utf8'
# )
#
# cur = db.cursor()
# cur.execute("select * from test.config_total where id in (2);")
# #   打印查询结果
# end = cur.fetchall()
# # for i in end:
# #     print(i)
# print(end)
# #  提交至数据库执行
# db.commit()
#
# #    关闭游标
# cur.close()
