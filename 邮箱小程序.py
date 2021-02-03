# # 邮箱小程序
# import smtplib,email
# import tkinter
# import tkinter.messagebox
# import tkinter.simpledialog
# root = tkinter.Tk()
# def MenuAbout():
#     tkinter.messagebox.showinfo("","关于我们")
# def Menusend():
#
#     chst =email.charset.Charset(input_charset ='utf-8')
#     name = entry1.get()
#     if name == "":
#         tkinter.messagebox.showinfo("","邮件名不可为空！ ")
#         return
#     receiver = entry1.get()
#     if receiver == "":
#         tkinter.messagebox.showinfo("","接受者不可为空！ ")
#         return
#     Sendername = entry3.get()
#     if Sendername == "":
#         tkinter.messagebox.showinfo("","发送者不可为空！ ")
#         return
#     header = ("from:%s\nTo: %s\nSubject:%s\n\n"
#           %(Sendername,
#             receiver,
#             chst.header_encode(name)))
#
#     body = flist.get("0.0",tkinter.END)
#     if body == "":
#         tkinter.messagebox.showinfo("","内容不可为空！ ")
#         return
#     email_con = header.encode('utf-8') +body.encode('utf-8')
#     smtp =smtplib.SMTP("smtp.163.com")
#
#     Sendpwd = entry4.get()
#     if Sendpwd == "":
#         tkinter.messagebox.showinfo("","请输入密码！ ")
#         return
#     try:
#         smtp.login(Sendername,Sendpwd)
#     except:
#          tkinter.messagebox.showinfo("","用户名或密码不正确！ ")
#          return
#     try:
#          smtp.sendmail(Sendername,receiver,email_con)
#     except:
#         tkinter.messagebox.showinfo("","接受者邮箱不正确！ ")
#         return
#     smtp.quit()
#     tkinter.messagebox.showinfo("","发送成功 ")
#
#         #创建菜单
# menu = tkinter.Menu(root)
# submenu = tkinter.Menu(menu,tearoff =0)
#
# submenu.add_command(label ="发送邮件",command= Menusend)
# submenu.add_separator()
# submenu.add_command(label ="关于..",command = MenuAbout)
# menu.add_cascade(label ="邮件系统",menu = submenu)
# root.config(menu = menu)
# lable1 =tkinter.Label(root,text ="邮件标题：",anchor = tkinter.W)
# lable1.place(x =5,y=0)
# entry1 =tkinter.Entry(root)
# entry1.place(x =65,y =10,anchor =tkinter.W)
#
# lable2 =tkinter.Label(root,text ="接受邮箱：",anchor = tkinter.W)
# lable2.place(x =5,y=20)
# entry2 =tkinter.Entry(root)
# entry2.place(x =65,y =20)
#
# lable3 =tkinter.Label(root,text ="发送者邮箱：",anchor = tkinter.W)
# lable3.place(x =220,y=0)
# entry3 =tkinter.Entry(root)
# entry3.place(x =300,y =10,anchor =tkinter.W)
#
# lable4 =tkinter.Label(root,text ="发送者密码：",anchor = tkinter.W)
# lable4.place(x =220,y=20)
# entry4 =tkinter.Entry(root,show = "*")
# entry4.place(x =300,y =30,anchor =tkinter.W)
#
# button1 = tkinter.Button(root,anchor =tkinter.CENTER,text ="发送",width =8,height = 1,command =Menusend)
# button1.place(x =400,y = 350)
#
# flist =tkinter.Text(root)
# flist.place(x =50,y =50,width = 400,height = 300)
# root.title("邮件系统")
# root.maxsize(500,400)
# root.minsize(500,400)
#
# if __name__ =="__main__":
#     root.mainloop()




import requests
from requests.cookies import RequestsCookieJar
import hmac,json
import hashlib
import time
import random
####################设置Key值##############

def hashstring(to_enc,ekey):
    enc_res = hmac.new(ekey.encode(), to_enc.encode(), hashlib.md5).hexdigest()
    # print(enc_res)
    return enc_res

if __name__=='__main__':
    print("开始进行**测试： ")
    url='http://**********'
    #设置随机值作为入参id
    id = []
    id = ''.join(str(i) for i in random.sample(range(0, 9), 2))  # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
    CurrentTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    requestid=CurrentTime+id
    #请求参数
    payload={'requestId':'',
          'merchantCode':'',
          'transferType':'',
          'transToMerCode':'',
          'transToMerName':'',
          'unionBankNum':'',
          'openBankName':'',
          'openBankProvince':'',
          'openBankCity':'',
          'sum':'0.03',
          'accountType':'1',
          'accountName':'***',
          'bankCode':'***',
          'bankAccount':'*******',
          'reason':'1555',
          'noticeUrl':'**********',
          'refundNoticeUrl':'*************',
          'transferPayType':'*',
          'signature':''
             }
    payload['requestId']=requestid
    #初始化字符串并进行加密拼接
    to_enc=''
    ekey='CSSH_KEY'
    for i in payload:
        to_enc=to_enc+payload[i]
    # print(to_enc)
    payload['signature'] = hashstring(to_enc, ekey)

    '''将中文进行GBK转化'''
    str='***'  #这个字符串与字典里accountName对应value一致
    strGBK=str.encode('GBK')
    '''转化完的中文回传到字典中'''
    payload['accountName']=strGBK
    headers={
            'Connection':'keep-alive',
            'Content-Length':'543',
            'Cache-Control':'max-age=0',
            'Origin':'http://**********',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'**************************************************',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer':'******************',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
        }
    s=requests.post(url=url,data=payload,headers=headers)
    print(s.text)
    print("status:",s.status_code)
    print("****************************************************")
    print("开始进行返回结果验证签名: ")
    '''返回结果进行验签'''
    ResultDict=s.json()
    synchronizationStr=ResultDict['requestId'] + ResultDict['result'] + ResultDict['sum']
    signature11=hashstring(synchronizationStr, ekey)
    try:
        if(ResultDict['result']=='00000' and signature11==ResultDict['signature']):
            print("                    恭喜你，同步返回验签成功")
        else:
            print("                    result错误码:", ResultDict['result'])
    except BaseException as msg:
        print(msg)
    finally:
        print("                    **处理完毕")
    print("****************************************************")

