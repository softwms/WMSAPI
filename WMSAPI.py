# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import json
import putjson

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
/       根目录，测试连通
/postsku    SKU产品档案接入
'''
# 创建一个服务，把当前这个python文件当做一个服务
app = Flask(__name__)
@app.route('/', methods=['get', 'post'])
def index():
    return "接口服务连通!"
@app.route('/postsku', methods=['get', 'post'])
def login():
    #客户列表，允许调用的客户
    userlist = ['XH']
    # 获取通过url请求传参的数据
    userid = request.values.get('userid')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    ##这里是业务，看你怎么写了，想写什么写什么
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if userid and pwd:
        if userid in userlist and pwd == 'test1234':
            data = request.data.decode()
            data=data.replace('\r\n','')
            # 调用putjson写入数据库
            putjson.putjson(data,"postsku")
            resu ={'code': 000, 'message': str(data)} # 将字典转换为json串, json是字符串
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code': 998, 'message': '账号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 999, 'message': '参数不完整请提供接口URL反馈IT'}
        return json.dumps(resu, ensure_ascii=False)
# host="0.0.0.0" 代表谁都可以访问，可以加nginx处理
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=58080, debug=True,threaded=True)
    ###指定端口、host设为0.0.0.0代表不管几个网卡，任何ip都可以访问,threaded=True同时执行多个路由请求,processes=线程数