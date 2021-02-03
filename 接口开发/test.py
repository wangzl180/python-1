# import flask,json
#
# server = flask.Flask(__name__)
#
# @server.route('/index',methods=['get'])
#
# def index():
#     res = {'msg': '这是一个接口','msg_code':0}
#     return json.dumps(res,ensure_ascii=False)
# server.run(port=8999,debug=True)





import requests
from pprint import pprint

res = requests.get("http://www.baidu.com")

if res.status_code == 200:
    print("测试通过")
else:
    print("状态码错误")

print(res.status_code)