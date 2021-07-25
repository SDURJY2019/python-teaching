'''
d=['i love you ','b is c']
#print(d[1])
for i in d:
    for j in i:
        print(j)
'''
'''
print('123456789'[:-1])#列表切片
print('123456789'[1:])#列表切片
print('123456789'[::-1])#列表切片
print('123456789'[:8:2])#列表切片
print('123456789'[:])
'''

import sys
#print(sys.getsizeof(a))
print('123000004000050000600007 8 9'.replace('0','c'))
a=str(list('123000004000050000600007 8 9')+[1,2,3])
print(a)
#a.replace('[',' ')
#a.replace(']',' ')
#a.replace(',',' ')
print(type(a))
print(a)
#print(list(map(int,a)))
#b=a.split('0')
#b.remove('')


#print('123456789'.find('1'))
#print('123456789'.__reversed__())
#print(str(reversed('123456789')))
#c=3
#d='i love you'
#print(d.find('i'))
#import sys
#import re
#print(str(range(0,10,1)).split(','))
'''
print(list(str(range(0,10,1))))
print(list(range(0,10,1)))
print(''.join(map(str,list(range(0,10,1)))))
print('$$$$$$')
'''
#map返回指针
#print(list(range(0,10,1)))
#print(sys.getsizeof((int)(c)))
#c='adas'
#print(type(c))
#print('hello world '*3)
#print('你好'+'你好吗'*2+'我不好'*3+'谢谢')
#help(sys)
'''
temp='123456789'
print(list(map(int,temp)))
#print(int(temp.split('')))
print('123456789'[:-1])#列表切片
print('123456789'[1:])#列表切片
print('123456789'[::-1])#列表切片
print('123456789'[:8:2])#列表切片
print('123456789'[:])
print(temp+'0000'+'123456789')
d=(temp+'0000'+'123456789').replace('0','c')
'''
'''
temp='123456789'
d=(temp+'0000'+'123456789').replace('0','c')

print(d)
'''

#d[0:2]='123'
#print(d)
#print((','*3).join(d.split(' ')))
#a=tuple([1,2,3])
#b={'a':1,'c':'123'}
#a=[1,2,3]
#b=[4,5,6]
#a.append(b)
#print(a)

#a.extend(b)
#print(a)
#c=[['a'],[123],]
#print(b)
#a[0]=a[0]+1
#print(a[0])
#help(sys)
'''
def myfunction(type,a):
    if type=='none':
        a=a+3
    return a

if __name__ == '__main__':
    #print(myfunction(type='',a=))
    print(myfunction(type='none',a=3))
    #print(myfunction(type='none', 3))   wrong
    print(myfunction('none',3))
    '''