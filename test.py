#注解增强函数，就是java中的spring
import time


def auto(type):
    print(type)
    def strong(func):
        def te(*arg):
            start_time = time.time();
            func(*arg)
            stop_time = time.time()
            print(abs(start_time - stop_time))

        return te
    return strong
@auto(type="local")
def test(x,y,z,r):
    print("------test1运行了-----",x,y,z,r)


test(2,3,4,5)

#列表生成式
a={1,2,2,2,2}
print(a)

a={i*2 for i in range(10)}
b=(i*3 for i in range(20))
print(b.__next__())
print(b.__next__())

print(a)
print(range(10))


#递归解决斐波那契数列
x, y, z = 1, 1, 2
b=[x,y,z]
def fib(m):


    print(b)
    n=b.__getitem__(b.__len__()-1)+b.__getitem__(b.__len__()-2)
    print(n)
    b.append(n)



    if b.__len__()>m:
        return b
    fib(m)

res=fib(4)
print(res.__sizeof__())
print(res)
