import time
import datetime
import cx_Oracle
import requests
import json
def putjson(js,apid):
    conn = cx_Oracle.connect('WMS_YL/WMS_YL@47.100.131.95:1521/orcl')
    curs = conn.cursor()
    insert="INSERT INTO bas_sku_edi(customerid,sku,descr_c,descr_e,packid,grossweight,netweight,price,skulength,skuwidth,skuhigh,alternate_sku1,shelflife,defaultsupplierid,csqty,plqty,sku_group1,sku_group2,sku_group3,sku_group4,sku_group5,reservedfield01,reservedfield02,reservedfield03,reservedfield04,reservedfield06,reservedfield07,reservedfield08,reservedfield09,reservedfield10,edisendtime,addtime,addwho,notes)VALUES(:customerid,:sku,:descr_c,:descr_e,:packid,:grossweight,:netweight,:price,:skulength,:skuwidth,:skuhigh,:alternate_sku1,:shelflife,:defaultsupplierid,:csqty,:plqty,:sku_group1,:sku_group2,:sku_group3,:sku_group4,:sku_group5,:reservedfield01,:reservedfield02,:reservedfield03,:reservedfield04,:reservedfield06,:reservedfield07,:reservedfield08,:reservedfield09,:reservedfield10,:edisendtime,:addtime,:addwho,:notes)"
    jstr=eval(js) #字符串转dict
        #{'data':[{'CUSTOMERID': 'XH', 'SKU': '1001', 'DESCR_C': '测试商品', 'DESCR_E': '1kg*5包', 'PACKID': '包', 'GROSSWEIGHT': 0.0, 'NETWEIGHT': 0.0, 'PRICE': 0.0, 'SKULENGTH': 0.0, 'SKUWIDTH': 0.0, 'SKUHIGH': 0.0, 'ALTERNATE_SKU1': '', 'SHELFLIFE': 365, 'DEFAULTSUPPLIERID': '', 'CSQTY': 5, 'PLQTY': 50, 'SKU_GROUP1': '', 'SKU_GROUP2': '', 'SKU_GROUP3': '常温', 'SKU_GROUP4': '', 'SKU_GROUP5': '', 'RESERVEDFIELD01': '', 'RESERVEDFIELD02': '', 'RESERVEDFIELD03': '', 'RESERVEDFIELD04': '', 'RESERVEDFIELD06': '', 'RESERVEDFIELD07': '', 'RESERVEDFIELD08': '', 'RESERVEDFIELD09': '', 'RESERVEDFIELD10': '', 'EDISENDTIME': '', 'ADDTIME': '', 'ADDWHO': 'EDI', 'NOTES': '备注是新品'}]}
    datalist=jstr.get('data')
    #按字段重组dict列表，顺序与insert格式一致
    sku_dict={'CUSTOMERID': '', 'SKU': '', 'DESCR_C': '', 'DESCR_E': '', 'PACKID': '', 'GROSSWEIGHT': '', 'NETWEIGHT': '', 'PRICE': '', 'SKULENGTH': '', 'SKUWIDTH': '', 'SKUHIGH': '', 'ALTERNATE_SKU1': '', 'SHELFLIFE': '', 'DEFAULTSUPPLIERID': '', 'CSQTY': '', 'PLQTY': '', 'SKU_GROUP1': '', 'SKU_GROUP2': '', 'SKU_GROUP3': '', 'SKU_GROUP4': '', 'SKU_GROUP5': '', 'RESERVEDFIELD01': '', 'RESERVEDFIELD02': '', 'RESERVEDFIELD03': '', 'RESERVEDFIELD04': '', 'RESERVEDFIELD06': '', 'RESERVEDFIELD07': '', 'RESERVEDFIELD08': '', 'RESERVEDFIELD09': '', 'RESERVEDFIELD10': '', 'EDISENDTIME': '', 'ADDTIME': '', 'ADDWHO': '', 'NOTES': ''}
    #i循环list多条报文一起发过来
    for i in datalist:
        #j循环取重组的SKU字段，取报文中内容给字段赋值
        for j in sku_dict:
            sku_dict[j]=i.get(j)
        print(sku_dict)
        curs.execute(insert,sku_dict)

    #提交关闭数据库连接
    conn.commit()
    curs.close()
    conn.close()