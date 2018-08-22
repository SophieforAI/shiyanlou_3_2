import sys

'''
def weather(f):
    def wrap(*args, **kw):
        print('今天天气不错。')
        return f(*args, **kw)
    return wrap

@weather
def f(weather):
    print('Today\'s weather is {}'.format(weather))
'''

def log(temp):
    def weather(f):
        def wrap(*args, **kw):
            if temp > 15:
                print('今天天气温暖：')
            else:
                print('今天天气寒冷：')
            return f(*args, **kw)
        return wrap
    return weather

@log(11)
def f(weather):
    print('Today\'s weather is {}.'.format(weather))

if __name__ == '__main__':
    f(sys.argv[1])
