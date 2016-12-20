#变量
a = 10
b = 20

print(a + b)

#判断
score = 80
if score > 60:
    print("及格")
else:
    print("不及格")

#循环
for i in range(8,10):
    print(i)

#函数
def sayHello():
    print("Hello Python!")

sayHello()

#继承
class Fruit:
    def __init__(self,color):  #初始化的时候传入一个水果的变量 fs
        self._fs = color   #在init里面赋值给当前class的变量 fs
    
    def fruitsColor(self):
        print("apple's color is "+self._fs)

    def howBig(self):
        print("1~2 m^3");

f = Fruit("red") #由于init，传入变量，实例化class 的时候需要传入 fs
f.fruitsColor()
f.howBig()

#class Apple(Fruit):                               #继承了父类
#    def __init__(self, color):                  #显示调用父类的__init__方法
#        Fruit.__init__(self, color)
#        print("apple's color: %s" % self.color)
#
#    def fruitsColor(self):
#        print("--")
#a = Apple("green")
#a.fruitsColor


#Python 引入py文件
##mark - 1
#import fileName
#a = fileName.className()    # a 实例化类对象
#
#
##mark - 2
#from fileName import className
#a = className()     # a 实例化类对象
#
#
