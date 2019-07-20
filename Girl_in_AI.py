
# coding: utf-8

# In[ ]:

# 数据类型


# In[3]:

100+100


# In[5]:

100-100


# In[6]:

2.508+1


# In[7]:

'girl'+'in'+'AI'


# In[8]:

#转义字符\  \n ---换行  \t-----tab   \\-----表示斜杠本身
print('I\'m a girl')


# In[10]:

#请尝试用python的print打出这两句话：
#I'm a GIAer.
#I'm learning machine learning by 'python'.

print('I\'m a GIAer.\nI\'m learning machine learning by \'python\'.')


# In[ ]:

#判断逻辑---布尔值


# In[11]:

True and True


# In[12]:

True or True


# In[13]:

not True


# In[17]:

print(True and False)
print(True or False)
print(False and True)
print(False or False)
print(False and False)
print(not False)
print(False and not False)
print(False or not False)


# In[18]:

#variable变量

message="I am learning python."
print(message)


# In[19]:

num = 2019
print(num)


# In[20]:

newnum = num +11
print(newnum)


# In[21]:

#bool 布尔表达式
x = 5
y = 6

x == y
x != y
x < y
x > y
x >= y
x <= y
x is y
x is not y


# In[23]:

x > 0 and x < 10 # and 同时为真即为真


# In[24]:

x > 0 and x < 4 # and 不同时为真即为假


# In[25]:

x > 0 or x < 4 # or 只要一个为真即为真


# In[26]:

not (x > 0) #取反


# In[27]:

x < 0 or not (x < 4)#优先级 not  and  or


# In[28]:

#字符串String
phone = 'apple'
phone[1]


# In[29]:

phone[0]='b'#字符串不可改变------错误示范


# In[30]:

#求字符串的长度
len(phone)


# In[32]:

length_1 = len(phone)
phone[length_1-1]


# In[34]:

#切片
phone[2:4]


# In[35]:

phone[2:]


# In[36]:

phone[:4]


# In[37]:

phone[:5]


# In[39]:

phone[:-1]


# In[40]:

#用in 找字符
single = 'a'
single in phone


# In[41]:

test = 'b'
test in phone


# In[49]:

#——其他method
#大写
print(phone.upper())

#小写
name = 'Jay'
print(name.lower())

#找到字符所在位置
print(phone.find('a'))

#去掉首尾空格
string_1 ='  hello , world      '
print(len(string_1),string_1)
print(string_1.strip())

#判断首字符，返回布尔值
print(phone.startswith('a'))


# In[51]:

name = 'Suljung'
'My name is Han %s.'%name + 'You can call me %s.'%name


# In[56]:

#切割
words = 'geeks for geeks'
print(words.split())#如果split（）函数中参数为空，默认为以空格进行分割

w_1 = 'egg,milk,apple'
print(w_1.split(','))

w_2 = 'red:pink:white'
print(w_2.split(':'))

w_3 = 'Sue:Jay:Ken:Tom'
print(w_3.split(':',2))#只按照前两个割符来分


# In[63]:

#链接
example=("aaa","bbb","ccc")
x ="&". join(example)
y ="*".join(example)
print(x,y)
print('%s\n'%x+'%s'%y)


# In[64]:

#格式操作符----%d  格式化整数 %g 格式化浮点数  %s 格式化字符串

number = 2
print('I have %d apples'%number)


# In[11]:

#数据类型转换

print(3.5/2)        # 直接除法，有小数点
print(int(3.5/2))   #取整
print(round(3.5/2)) #四舍五入取整
print(int('4'))     #把字符串转换成整数，字符串本身为整数

print('-'*100)

print(4/2)#答案为整数，取一位小数
print(float(3.1415/3))#答案为有限位小数，直到输出完整
print(round(3.1415/3,4))#四舍五入，逗号后的参数表示保留几位小数

print('-'*100)

#转换成字符串
a = 4
b = str(a)
print('a = {},type of a is {};\nb = {},type of b is {}'.format(a,type(a),b,type(b)))

print('\n'+'-'*100)

#转换成布尔值

print(bool(10))
print(bool(0))
print(bool('hello'))
print(bool(None))
print(bool(10 < 2))






