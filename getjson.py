import time
import datetime
import cx_Oracle
import requests
import json

#连接数据库
conn = cx_Oracle.connect('WMS_YL/WMS_YL@47.100.131.95:1521/orcl')
#定义2个游标
curs = conn.cursor()
curs1 = conn.cursor()
#sql语句，带参数的执行要给入参
sql = "select * from bas_sku_edi where customerid='XH' and rownum<100"
update = "UPDATE httppost SET message=:1,status=:2,sendtime=to_date(:3,'yyyy-mm-dd HH24:MI:SS') WHERE id=:4 "
#执行查询sql，查询出来的数据按行循环
curs.execute(sql)
desc = curs.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
data_dict = [dict(zip([col[0] for col in desc], row)) for row in curs.fetchall()]  # 列表表达式把数据组装起来
data_dict=str(data_dict).replace('None','\'\'')
print(data_dict)
data_dict="{'data':"+str(data_dict)+'}'
print(data_dict)

curs.close()
conn.close()