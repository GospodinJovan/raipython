a = "Prom"
b = "romp"
c=a.lower()
d=b.lower()

def sortieren(c,d):
    if sorted(c)==sorted(d):
        print ("True")
    else:
        print ("False")

sortieren(c,d)




a = "Prom"
b = "romp"
c=a.lower()
d=b.lower()

print (sorted(c)==sorted(d))


a = "Prom"
b = "romp"

def compare (a, b):
    if len(a) != len(b):
        return False
    abc = [0] * 256
    for c in a:
        abc[ord(c)] += 1

    for b in a:
        abc[ord(c)] -= 1
        if abc[ord(c)] < 0:
            return False
        return True

print(compare(a, b))
