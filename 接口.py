#!/usr/bin/env Python
# coding=utf-8
import flask,json
import sql脚本

server = flask.Flask(__name__)

@server.route('/login',methods=['post'])
def login():
    username = flask.request.values.get('username',type=str,default=None)
    password = flask.request.values.get("password",type=str,default=None)
    print(username,password)
    if username or password:
        sql = 'SELECT * FROM user where username="%s";'%username
        if my_db(sql):
            reg = {"code": "10002","msg": "该用户已存在"}

        else:
            insert_sql = 'insert into user (username,password) values ("%s","%s");'%(username,password)
            my_db(insert_sql)
            reg = {"code": "0","msg": "注册成功"}

    else:
        reg = {
               "msg":"缺少必填参数",
               "code":"10001"
            }
    return json.dumps(reg,ensure_ascii=False)

server.run(port=8080,debug=True,)


