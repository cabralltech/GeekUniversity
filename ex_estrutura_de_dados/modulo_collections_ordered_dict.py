from collections import OrderedDict
dic = dict(c=3, g=9, a=2, f=3, b=2)
print(dic)
ordem_dic = OrderedDict(dic)
print(ordem_dic)
print(type(ordem_dic))

dic1 = dict(a=1, b=2)
dic2 = dict(b=2, a=1)
print(dic1 == dic2)

dic1 = OrderedDict(dic1)
dic2 = OrderedDict(dic2)
print(dic1 == dic2)
