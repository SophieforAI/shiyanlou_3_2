def weather(f):
    def wrap(*args, **kw):
        print('Today\'s weather:')
        return f(*args, **kw)
    return wrap

def f(a):
    return a

@weather
def f1(a):
    return a

#print(weather(f)('cool'))
print(f1)
print(f1('cool'))
