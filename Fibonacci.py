
def fib(n):
    a1 = 0
    a2 = 1
    for i in range (n):
        a1,a2 = a2, a1+a2
    return a1

m=1
print (fib(m))


#recursion
d = {}
def fib (n):
    a1 = 0
    a2 = 1
    if n==0:
        return a1
    if n==1:
        return a2
    if n in d: return d[n]
    res = fib(n-2)+fib(n-1)
    d[n]=res
    return res


m=56
print (fib(m))
