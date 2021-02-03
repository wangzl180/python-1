
import os
import time
import json

if __name__ == '__main__':

   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   Domain_File = os.path.join(BASE_DIR, 'cps_sa.log.20201115')

   with open(Domain_File) as f:
        order_str = f.read()

   order_list = order_str.split('\n')
 
   for item  in order_list:
       #item_data = json.loads(item)
       #print(item)
       item_dict = json.loads(item)
       print("theme:%s ,channel_id:%s ,order_id:%s ,order_amount:%s " %(item_dict['properties']['theme'],item_dict['properties']['channel_id'],item_dict['properties']['order_id'],item_dict['properties']['order_amount']))
       #item_dict = eval(item)
       #print(item_dict['event'])
       #time.sleep(1)
