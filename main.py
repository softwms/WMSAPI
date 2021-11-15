import putjson
import test1

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    jstr={'data':[{'CUSTOMERID': 'XH', 'SKU': '1001', 'DESCR_C': '测试商品', 'DESCR_E': '1kg*5包', 'PACKID': '包', 'GROSSWEIGHT': 0.0, 'NETWEIGHT': 0.0, 'PRICE': 0.0, 'SKULENGTH': 0.0, 'SKUWIDTH': 0.0, 'SKUHIGH': 0.0, 'ALTERNATE_SKU1': '', 'SHELFLIFE': 365, 'DEFAULTSUPPLIERID': '', 'CSQTY': 5, 'PLQTY': 50, 'SKU_GROUP1': '', 'SKU_GROUP2': '', 'SKU_GROUP3': '常温', 'SKU_GROUP4': '', 'SKU_GROUP5': '', 'RESERVEDFIELD01': '', 'RESERVEDFIELD02': '', 'RESERVEDFIELD03': '', 'RESERVEDFIELD04': '', 'RESERVEDFIELD06': '', 'RESERVEDFIELD07': '', 'RESERVEDFIELD08': '', 'RESERVEDFIELD09': '', 'RESERVEDFIELD10': '', 'EDISENDTIME': '', 'ADDTIME': '', 'ADDWHO': 'EDI', 'NOTES': '备注是新品'}]}
    re=test1.pr(jstr)
    print(re)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
