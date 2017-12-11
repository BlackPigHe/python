import getpass
name="hzj"
print("my name is",name)
name=input("name:")
password=getpass.getpass("password")
info="_____________\n" \
     "name:{name}\n" \
     "password:{password}\n".format(name=name,password=password)

print(info)
