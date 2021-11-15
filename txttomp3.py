import requests
import time
from playsound import playsound
def mp3(txt):
    #lan = zh：语言是中文，如果改为lan = en，则语言是英文。ie = UTF - 8：文字格式。spd = 2：语速，可以是1 - 9的数字，数字越大，语速越快。text = ** ：这个就是你要转换的文字。
    url="http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=2&text="+txt
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data=requests.get(url,headers=headers)
    print(data.text.encode('utf-8'))
    #millis = int(round(time.time() * 1000))  #时间文件名，取重
    filePath = "test.mp3" #生成文件的路径和名称
    fo = open(filePath, 'wb')                #打开文件
    fo.write(data.content)                   #写入声音码
    fo.close()                               #关闭文件
    playsound(filePath)                      #播放声音文件


while True:
    mp3(input())