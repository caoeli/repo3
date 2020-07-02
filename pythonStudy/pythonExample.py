# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2020-02-13 12:21:54
# @Last Modified by:   Marte
# @Last Modified time: 2020-02-15 08:30:45
print('hello')

total = 'item_one' +\
        'item_two' +\
        'item_three'
total =['one','two',
        'three','four']
print(total)

str1='''hello pythonExample.py
        word 123456'''
print(str1)
print('123\r\n456')
print(r'789\r\n654')
a=['this','is','string']
print(a)
print('a'*10)
str2='123456789'
print(str2[-1])
print(str2[-1:-5:-2])
str2='456789'
print(str2)
word='字符串'
sentence ='这是一个句子'
paragraph='''这是一个段落，
            可以由多行组成'''
print(word)
print(sentence)
print(paragraph)

str2='123456789'
print(str2) #123456789
print(str2[0:-1]) #12345678
print(str2[0]) #1
print(str2[2:5]) #345
print(str2[2:])#3456789
print(str2*2)#123456789123456789
print(str2+'您好')#123456789您好

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# input("\n\n 按下 enter 键后退出")
print('result12')

import sys;x1='runoob'; sys.stdout.write(x1+'\n123')
x='a'
y='b'
print('***************')
print(x,end="")
print(y,end="")

import sys
for i in sys.argv:
    print(i)
print('python  path is',sys.path)

from sys import argv,path
print('path',path)
# from sys import argv,path  #  导入特定的成员

# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

a=b=c=123
print(a,b,c)

a,b,c=1,5.5,'abcd'
print(a,b,c)
e=True
print(type(a))
print(type(b))
print(type(c))
print(type(e))

class A:
    pass
class B(A):
    pass
print(isinstance(A(), A))
print(type(A())==A)
print(isinstance(B(), A))
print(type(B())==A)
var1=123
var2=10
del var1
print(5+4)

print(2//4)
print(2**5)
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
print(len(word))

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表l

letters=['a','h','e','c','k','i','o']
print(letters[1:4:2])

def reverseWords(input):
    inputWords=input.split(" ")
    inputWords=inputWords[-1::-1]
    output =" ".join(inputWords)
    return output
if __name__ == '__main__':
    input ="I like runoob"
    rw=reverseWords(input)
    print(rw)
#元组
tuple = ('abc','789',2.23,'runoob',70.2)
tinytuple =(123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)


tuple1=()
tup0=(20)

student={'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student)
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')


dic ={'1':'one','2':'two'}
print(dic)
print(dic.keys())

print(dic.values())
print({x:x**2 for x in (2,3)})
'''
this  is pythonExample.py
this is pytyon

'''

a = 25
b = 20

if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 25
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")

if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")
print('****************************')
import random
print(random.choice(range(10)))
# import randrange
print(random.randrange(0,100,2))

random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())

list=[1,2,34,5]
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
real1=random.uniform(1,10)
print(real1)
import math
print(math.acos(1/2))
print(math.sin(math.pi/2))
print(math.hypot(5,6))
print(math.pi/math.radians(90))
print(math.degrees( math.pi/2))
print(math.sqrt(61))

print("{} {}".format("hello","world"))
print("{0} {1}".format("hello","world"))
print("{1} {0} {1}".format("hello","world"))

# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))

# # 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print("网站名：{name},地址 {url}".format(name="菜鸟教程",url="www.runoob.com"))
site={'name':'菜鸟教程','url':'www.runoob.com'}
print('网站名称:{name},地址 {url}'.format(**site))
my_list=['菜鸟教程','www.runoob.com']
print("网站名称:{0[0]},地址 {0[1]}".format(my_list))

class AssignValue(object):
    """docstring for AssignValue"""
    def __init__(self, arg):
        super(AssignValue, self).__init__()
        self.arg = arg
