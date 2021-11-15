import time
import datetime
import cx_Oracle
import requests
import json
#连接数据库
conn = cx_Oracle.connect('WMS_USER/WMS_USER@47.100.131.95:1521/orcl')
#定义2个游标
curs = conn.cursor()
curs1 = conn.cursor()
#sql语句，带参数的执行要给入参
sql = "select id,url,content from httppost where status='0' and appid='WXALERT'"
update = "UPDATE httppost SET message=:1,status=:2,sendtime=to_date(:3,'yyyy-mm-dd HH24:MI:SS') WHERE id=:4 "
#执行查询sql，查询出来的数据按行循环
curs.execute(sql)
for table in curs:
    print(table)
    #取行中列顺序对应的值
    id=table[0]
    url = table[1]
    c = table[2]
    #组织post请求发送的内容
    content =c #' {"msgtype": "text","text": {"content":"' + c + '","mentioned_list":["@all"]}}'
    print(content)
    headers={"Content-Type": "application/json"}
    #调用http post请求，中文要加encode
    r = requests.post(url=url,headers=headers,data=content.encode('utf-8'))
    print(r.text)
    #带参数的update,提前组织好参数，日期格式传str，在sql中转date
    info=(r.text,'1',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),id)
    curs1.execute(update,info)
#提交，关闭连接
conn.commit()
curs.close()
conn.close()
time.sleep(5)
