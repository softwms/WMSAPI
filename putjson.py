import cx_Oracle
import datetime
ora_server='WMS_YL/WMS_YL@47.100.131.95:1521/orcl'
sku_insert = "INSERT INTO bas_sku_edi(customerid,sku,descr_c,descr_e,packid,grossweight,netweight,price,skulength,skuwidth,skuhigh,alternate_sku1,shelflife,defaultsupplierid,csqty,plqty,sku_group1,sku_group2,sku_group3,sku_group4,sku_group5,reservedfield01,reservedfield02,reservedfield03,reservedfield04,reservedfield06,reservedfield07,reservedfield08,reservedfield09,reservedfield10,edisendtime,addtime,addwho,notes)VALUES(:customerid,:sku,:descr_c,:descr_e,:packid,:grossweight,:netweight,:price,:skulength,:skuwidth,:skuhigh,:alternate_sku1,:shelflife,:defaultsupplierid,:csqty,:plqty,:sku_group1,:sku_group2,:sku_group3,:sku_group4,:sku_group5,:reservedfield01,:reservedfield02,:reservedfield03,:reservedfield04,:reservedfield06,:reservedfield07,:reservedfield08,:reservedfield09,:reservedfield10,:edisendtime,:addtime,:addwho,:notes)"
sku_dict = {'CUSTOMERID': '', 'SKU': '', 'DESCR_C': '', 'DESCR_E': '', 'PACKID': '', 'GROSSWEIGHT': '', 'NETWEIGHT': '','PRICE': '', 'SKULENGTH': '', 'SKUWIDTH': '', 'SKUHIGH': '', 'ALTERNATE_SKU1': '', 'SHELFLIFE': '','DEFAULTSUPPLIERID': '', 'CSQTY': '', 'PLQTY': '', 'SKU_GROUP1': '', 'SKU_GROUP2': '', 'SKU_GROUP3': '','SKU_GROUP4': '', 'SKU_GROUP5': '', 'RESERVEDFIELD01': '', 'RESERVEDFIELD02': '', 'RESERVEDFIELD03': '','RESERVEDFIELD04': '', 'RESERVEDFIELD06': '', 'RESERVEDFIELD07': '', 'RESERVEDFIELD08': '','RESERVEDFIELD09': '', 'RESERVEDFIELD10': '', 'EDISENDTIME': '', 'ADDTIME': '', 'ADDWHO': '', 'NOTES': ''}
asn_insert ="insert into doc_asn_header_edi(warehouseid,customerid,erpno,asntype,supperid,suppername,carrierid,intime,notes,addtime) VALUES (:warehouseid,:customerid,:erpno,:asntype,:supperid,:suppername,:carrierid,:intime,:notes,:addtime)"
asn_dict={'WAREHOUSEID':'','CUSTOMERID':'','ERPNO':'','ASNTYPE':'','SUPPERID':'','SUPPERNAME':'','CARRIERID':'','INTIME':'','NOTES':''}
asnd_insert ="insert into doc_asn_details_edi(erpno,sku,qty,lineno,price,lotatt01,lotatt02,notes) values(:erpno,:sku,:qty,:lineno,:price,:lotatt01,:lotatt02,:notes)"
asnd_dict= {'ERPNO':'','SKU':'','QTY':'','LINENO':'','PRICE':'','LOTATT01':'','LOTATT02':'','NOTES':''}
so_insert = "insert into doc_order_header_edi(WAREHOUSEID,CUSTOMERID,ERPNO,ORDERTYPE,CONSIGNEEID,CONSIGNEENAME,CONTACT,TEL,PROVINCE,CITY,ADDRESS1,ADDRESS2,OUTTIME,NOTES,ADDTIME) values (:WAREHOUSEID,:CUSTOMERID,:ERPNO,:ORDERTYPE,:CONSIGNEEID,:CONSIGNEENAME,:CONTACT,:TEL,:PROVINCE,:CITY,:ADDRESS1,:ADDRESS2,:OUTTIME,:NOTES,:ADDTIME)"
so_dict = {'WAREHOUSEID':'','CUSTOMERID':'','ERPNO':'','ORDERTYPE':'','CONSIGNEEID':'','CONSIGNEENAME':'','CONTACT':'','TEL':'','PROVINCE':'','CITY':'','ADDRESS1':'','ADDRESS2':'','OUTTIME':'','NOTES':''}
sod_insert = "INSERT INTO doc_order_details_edi(ERPNO,LINENO,SKU,QTY,PRICE,LOTATT01,LOTATT02) VALUES (:ERPNO,:LINENO,:SKU,:QTY,:PRICE,:LOTATT01,:LOTATT02)"
sod_dict = {'ERPNO':'','LINENO':'','SKU':'','QTY':'','PRICE':'','LOTATT01':'','LOTATT02':''}

def insert(sql,dict):     #调用数据库，插入接口数据
    conn = cx_Oracle.connect(ora_server)
    curs = conn.cursor()
    curs.execute(sql, dict)
    # 提交关闭数据库连接
    conn.commit()
    curs.close()
    conn.close()

def postdata(apid,data):

    jstr=eval(data) #字符串转dict
    datalist=jstr.get('HEADER')  #取jstr中HEADER节点
    if apid == "postsku":  # postsku产品档案接口报文
        #i循环list多条报文一起发过来
        for i in datalist:
            #j循环取重组的SKU字段，取报文中内容给字段赋值
            for j in sku_dict:
                sku_dict[j]=i.get(j)
            print(sku_dict)
            insert(sku_insert,sku_dict)  #写入数据库

    if apid=="postasn":   #postASN入库单接口报文
        for i in datalist:
            #j循环取重组的SKU字段，取报文中内容给字段赋值
            for j in asn_dict:
                asn_dict[j]=i.get(j)   #按asn_dict字段名找值，缺失字段时允许data顺序不一致
            asn_dict["addtime"]=datetime.datetime.now() #增加当前时间用于addtime
            insert(asn_insert,asn_dict)
            ERPNO = i.get("ERPNO")      # 取ERPNO做为H/D主键
            DETAILS = i.get("DETAILS")  # 取明细行列表
            for d in DETAILS:
                for j in asnd_dict:    #按asnd_dict字段名找值，缺失字段时允许data顺序不一致
                    asnd_dict[j]=d.get(j)
                asnd_dict["ERPNO"]=ERPNO  #ERPNO写入asnd_dect中作为主键
                print(asnd_dict)
                insert(asnd_insert,asnd_dict)  #写入数据库

    if apid=="postso":   #postso出库单接口报文
        for i in datalist:
            #j循环取重组的SKU字段，取报文中内容给字段赋值
            for j in so_dict:
                so_dict[j]=i.get(j)   #按asn_dict字段名找值，缺失字段时允许data顺序不一致
            so_dict["addtime"]=datetime.datetime.now() #增加当前时间用于addtime
            insert(so_insert,so_dict)
            ERPNO = i.get("ERPNO")      # 取ERPNO做为H/D主键
            DETAILS = i.get("DETAILS")  # 取明细行列表
            for d in DETAILS:
                for j in sod_dict:    #按asnd_dict字段名找值，缺失字段时允许data顺序不一致
                    sod_dict[j]=d.get(j)
                sod_dict["ERPNO"]=ERPNO  #ERPNO写入asnd_dect中作为主键
                print(sod_dict)
                insert(sod_insert,sod_dict)  #写入数据库