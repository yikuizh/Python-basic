# ex1
# print object directly and compare two objects
class Person:
    pass

xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong
print xiaohong == xiaoming # compare 2 objects

# ex2 给实例属性
# L1中是三个实例不是名字所以先要提取出属性
# lambda表达式在自定义排序的作用
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3] # 存放的是三个实例
L2 = sorted(L1,lambda p1,p2: cmp(p1.name,p2.name))  #提取出三个实例的属性，常用lambda来自定义排序

print L2[0].name
print L2[1].name
print L2[2].name

# ex3 初始化实例
# def __init__ 第一个参数必须是self
class Person(object):
    def __init__(self,name,gender,birth,job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# ex4 访问限制 属性如果由'__'开头则无法被外部引用
self.__score = score # 此时score无法被外部实例访问

# ex5 创建类属性
# 区分初始化属性和类属性；初始化属性只有属性名称没有内容，需要通过后续实例输入，而类属性是在类中已经定义好，所有实例都会有的值
# 类属性也可以后续动态添加和修改
## 请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
class Person(object):
    count = 0 # 类属性
    def __init__(self, name): # 初始化实例，每输入一个name，相当于初始化一次，初始化是给实例一个属性而类方法是给了一个函数运算
        Person.count = Person.count + 1 # 重复类的属性，写在初始化里面
        self.name = name
p1 = Person('Bob')
print Person.count
# => 1
p2 = Person('Alice')
print Person.count
# => 2
p3 = Person('Tim')
print Person.count
# => 3

# ex6
# 实例属性和类属性可能重复名字，Person.address为类属性，p1.address为实例属性，两者不冲突可以同时存在

# ex7 定义实例方法(def)，区分初始化__init__
# self.__name 外部不能调用但可以类内部运算调用，直接在类方法中输入此表达式
# 定义类方法 def fangfa(self,输入参数)

# ex8
# 如果将类属性 count 改为私有属性__count，则外部无法读取__score，但可以通过一个类方法获取，请编写类方法获得__count值:
class Person(object):
    __count = 0 # 此时不能直接读取 要利用类方法来转述
    @classmethod # 加上这一句定义成为类方法
    def how_many(cls): 
        return cls.__count # 此时在类方法中返回私有属性
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
print Person.how_many()
p1 = Person('Bob')
print Person.how_many()






