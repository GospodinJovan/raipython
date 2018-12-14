import math

list=[3]
a=len(list)
if a==0:
    raise Exception ("List is empty")
else:
    list2=list[0::2]
    list3=sum(list2)*list[-1]

print(list3)


