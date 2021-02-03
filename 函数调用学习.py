# name = "wangzl"
# def ChangeName():
#     name = "Ennn......"
#     print("name01:%s"%name)
#
#     def ChangeName2():
#         name = "Miiii..."
#         print("name02:%s"%name)
#
#     ChangeName2()
#
# ChangeName()

import flask
import tools #自己写的py，里面写了一些下面需要调用的函数
import json
server = flask.Flask(__name__)
#新建一个服务，把当前这个python文件当做一个服务

#开发一个登录接口
@server.route('/login',methods=['get'])
def login():
    uname = flask.request.values.get('username')
    pd = flask.request.values.get('passwd')
    sql = 'select * from app_myuser where username="%s"'%uname
    res = tools.my_db(sql) #tools里的函数：连接数据库，执行sql并返回结果
    if res:
        if tools.my_md5(pd) == res.get('passwd'): #tools里的函数，加密密码
            res = {"code":0,"msg":"登录成功！"}
        else:
            res = {"code":1,"msg":"密码错误！"}
    else:
        res = {'code':2,"msg":"用户不存在"}
    return json.dumps(res,ensure_ascii=False,indent=4) #输出json格式

server.run(host='127.0.0.1',port=8998,debug=True)#若别人访问这个接口，则host需要输入自己的ip地址，而不是127.0.0.1