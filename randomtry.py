

import random

def compare (w,b):
    i=0
    while i < 1000:
        w=[]
        v=(random.randrange (0,10000))
        w.append(v)
        i = i + 1
    a=0
    while a < 1000:
        b=[]
        c=(random.randrange (0,10000))
        b.append(c)
        a = a + 1
        return (sorted(w) == sorted(b))

