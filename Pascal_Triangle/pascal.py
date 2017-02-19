# -*- coding: utf-8 -*-
#根据上一行(x-1)的元素求出当前行的元素，然后把整行添加到ll列表
def generate_line(x):
    new=[]
    for i in range(len(ll[x-1])+1):
        if i == 0 or i == len(ll[x-1]):
            new.append(1)
        else:
            new.append(ll[x-1][i]+ll[x-1][i-1])
    ll.append(new)
#将各行转换为字符，并用‘ ’连接所有元素，返回最长一行的长度
def generate_triangle():
    wtf=0
    for i in range(len(ll)):
        for j in range(len(ll[i])):
            ll[i][j]=str(ll[i][j])
        output.append(' '.join(ll[i]))
        wtf = max(wtf,len(output[i]))
    return wtf
#按最大长度居中输出各行
def print_triangle():
    for i in output :
        print i.center(maxlen)



ll=[[1]]   #生成一个嵌套列表的列表，其中每一个列表元素代表一行
output=[]

n=input("To generate pascal triangle,\nhow many lines do you want?:")

for i in range(1,n):
    generate_line(i)
maxlen=generate_triangle()
print_triangle()
