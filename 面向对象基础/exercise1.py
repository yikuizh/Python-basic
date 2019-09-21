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

# ex3 



