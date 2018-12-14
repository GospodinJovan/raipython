



class MyCounter(object):
    def __init__(self, l):
        self._d = {}
        for item in l:
            if item in self._d:
                self._d[item] += 1
            else:
                self._d[item] = 1


    def most_common(self):
        m = None
        for k, v in self._d.items():
            if m is None:
                m = (k, v)
            else:
                if v > m[1]:
                    m = (k, v)
        return m

    def __contains__(self, item):
        return item in self._d

    def __getitem__(self, item):
        return self._d[item]

    def __repr__(self):
        return str(self._d)



def main():
    a = [1,2,3,1,2,1,1,1,4]
    c = MyCounter(a)
    print(c)
    print(c.most_common())
    print(1 in c)
    print(c[1])

if __name__== "__main__":
    main()




class MyCounter(dict):
    def __init__(self, l):
        super().__init__()
        for item in l:
            if item in self:
                self[item] += 1
            else:
                self[item] = 1


    def most_common(self):
        m = None
        for k, v in self.items():
            if m is None:
                m = (k, v)
            else:
                if v > m[1]:
                    m = (k, v)
        return m

    @classmethod
    def foo(cls):
        print("Hello")




def main():
    a = [1,2,3,1,2,1,1,1,4]
    c = MyCounter(a)
    print(c)
    print(c.most_common())
    print(1 in c)
    print(c[1])
    MyCounter.foo()

if __name__== "__main__":
    main()

