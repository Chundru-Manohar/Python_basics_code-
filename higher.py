def Divisor(x):
    def Dividend(y):
        return y/x
    return Dividend

a = Divisor(2)
print(a(10))

def Add(x):
    def subs(y):
        return x + y
    return subs

d = Add(5)
print(d(5))