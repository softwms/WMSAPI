import putjson
import datetime
apid="POSTSO"
sku=str({"HEADER": [{ "CUSTOMERID": "XH", "SKU": "1001", "DESCR_C": "测试商品名称","DESCR_E": "测试商品规格","PACKID": "箱","GROSSWEIGHT": "0","NETWEIGHT": "0","SKULENGTH": "0","SKUWIDTH": "0","SKUHIGH": "0","PRICE": "0","SHELFLIFE": "365","ALTERNATE_SKU1": "6912345678901","DEFAULTSUPPLIERID": "","SKU_GROUP1": "","SKU_GROUP2": "","SKU_GROUP3": "","SKU_GROUP4": "","SKU_GROUP5": "","NOTES": "商品备注信息"},
{ "CUSTOMERID": "XH", "SKU": "1002", "DESCR_C": "测试商品名称2","DESCR_E": "测试商品规格2","PACKID": "箱","GROSSWEIGHT": "0","NETWEIGHT": "0","SKULENGTH": "0","SKUWIDTH": "0","SKUHIGH": "0","PRICE": "0","SHELFLIFE": "365","ALTERNATE_SKU1": "6912345678901","DEFAULTSUPPLIERID": "","SKU_GROUP1": "","SKU_GROUP2": "","SKU_GROUP3": "","SKU_GROUP4": "","SKU_GROUP5": "","NOTES": "商品备注信息"}
]})
asn=str({"HEADER": [{"WAREHOUSEID": "WH1", "CUSTOMERID": "OW", "ERPNO": "ERP001", "ASNTYPE": "01", "SUPPERID": "S01", "CARRIERID": "SF", "INTIME": "2021-01-01 09:00:00", "NOTES": "商品备注信息", "DETAILS": [{"SKU": "1001", "QTY": "2", "LINENO": "1", "PRICE": "1.02", "LOTATT01": "2020-10-01", "LOTATT02": ""}, {"SKU": "1002", "QTY": "20", "LINENO": "2", "PRICE": "1.02", "LOTATT01": "2020-10-01", "LOTATT02": ""}]}]})
so=str({"HEADER":[{"WAREHOUSEID":"WH1","CUSTOMERID":"OW","ERPNO":"ERP002","ORDERTYPE":"01","CONSIGNEEID":"C01","CONSIGNEENAME":"测试店铺1","CONTACT":"张三","TEL":"13912345678","PROVINCE":"浙江省","CITY":"杭州市","ADDRESS1":"崇仁路253号","ADDRESS2":"西湖区","OUTTIME":"2021-11-0109:00:00","NOTES":"发货备注","DETAILS":[{"SKU":"1001","QTY":"2","LINENO":"1","PRICE":"1.02","LOTATT01":"2020-10-01","LOTATT02":""},{"SKU":"1002","QTY":"2","LINENO":"2","PRICE":"1.02","LOTATT01":"2020-10-01","LOTATT02":""}]}]})
print(so)
putjson.postdata(apid,so)