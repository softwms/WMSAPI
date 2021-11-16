str="http://172.20.115.150:8080/postsku?1=1"
post=str.rfind("/")
print(str)
print(str[str.rfind("/")+1:str.find("?")])