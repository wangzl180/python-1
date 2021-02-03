import pymysql
import os
import json
#from flask_cors import *

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

from flask import Flask, request

app = Flask(__name__)


@app.route('/index1', methods=['GET'])
def indextest():
    inputData = request.args.get("inputData")
    data1 = getcontent(inputData)
    return data1


def getcontent(inputData):

    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='WZl496085235',
        charset = 'utf8'
    )
    selectlanguage = "SELECT * FROM test.config_total where id=2 AND " \
                     "stationcode='" + inputData + "'and (date_format(dtime,'%H:%i')='08:00' or " \
                                                   "date_format(dtime,'%H:%i')='14:00' or date_format(dtime,'%H:%i')='20:00' or " \
                                                   "date_format(dtime,'%H:%i')='02:00' )  ;"
    cur = conn.cursor()
    cur.execute(selectlanguage)
    data = cur.fetchall()

    cur.close()