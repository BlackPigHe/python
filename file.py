import os

fw=open("test.py",'w+',encoding="utf-8")
fw.write("print('hello world')")
fw.close()

fw2=open("test.py",'r+',encoding="utf-8")
print(fw2.readline())
print(fw2.tell())
fw2.seek(2)
print(fw2.tell())
fw2.close()
