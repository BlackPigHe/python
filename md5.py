import hashlib



string = "beyongjie"


md5 = hashlib.md5()
sha1=hashlib.sha1()
sha1.update("hehe".encode('utf-8'))
print(sha1.hexdigest())
md5.update("hahha".encode('utf-8'))
md5.update("加密".encode(encoding="utf-8"))
res = md5.hexdigest()
print("md5加密结果:",res)