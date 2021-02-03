# '''
# python正则表达式--------零宽断言
# '''
import re

#  1、  正预测先行断言  (?=exp)
s = "I'm singing while you're dancing"
p = re.compile(r'\b\w+(?=ing\b)')
print("正预测先行断言",re.findall(p,s))
#
#
# #  2、 正回顾后发断言 (?<=exp)
# s = "doing done do todo"
# p = re.compile(r'(?<=\bdo)\w+\b')
# print("正回顾后发断言",re.findall(p,s))
#
#
# #  3、 负预测先行断言  (?!exp)
# s = 'done run going'
# p = re.compile(r'\b\w{2}(?!ing\b)')
# print("负预测先行断言",re.findall(p,s))
#
#
# #  4、 负回顾后发断言    (?<!exp)
# s = 'done run going'
# p = re.compile(r'(?<!\bdo)\w{2}\b')
# print("负回顾后发断言",re.findall(p,s))
#
#
# #  5、 正向零断断言的结合使用
# #  举例：字符串ip是一个ip地址，现在要匹配出其中的四个整数：
# ip = '160.158.0.77'
# p = re.compile(r'(?<=\.)?\d+(?=\.)?')
# print("IP输出结果为:",re.findall(p,ip))
#
#
# #  6、 负向零宽断言的结合使用
# #  举例：匹配字符串s中的一些单词，这些单词不”x“开头且不以”y“结尾
# s = 'xaay xbbc accd'
# p = re.compile(r'(?<!\bx)\w+(?!y\b)')
# print("字符串输出结果为：",re.findall(p,s))


# import json
# from urlparse import parse_qs
# from wsgiref.simple_server import make_server
#
#
# # 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
# def application(environ, start_response):
#     # 定义文件请求的类型和当前请求成功的code
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
#     # 获取当前get请求的所有数据，返回是string类型
#     params = parse_qs(environ['QUERY_STRING'])
#     # 获取get中key为name的值
#     name = params.get('name', [''])[0]
#     no = params.get('no', [''])[0]
#
#     # 组成一个数组，数组中只有一个字典
#     dic = {'name': name, 'no': no}
#
#     return [json.dumps(dic)]
#
#
# if __name__ == "__main__":
#     port = 5088
#     httpd = make_server("0.0.0.0", port, application)
#     print("serving http on port {0}...".format(str(port)))
#     httpd.serve_forever()


