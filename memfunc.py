# 装饰器
def mem0():
    import functools, time

    def log(text):
        def metric(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                start = time.time()
                fn(*args, **kw)
                end = time.time()
                t = end - start
                print('%s:  %s executed in %s ms' % (text, fn.__name__, t))
                return fn(*args, **kw)
            return wrapper
        return metric

    # fast = log('execute')(fast)
    @log('execute')
    def fast(x,y):
        time.sleep(0.0012)
        return x + y
    @log('execute')
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;

    '''
    执行log('execute')返回metric函数,再执行metric(fast), 返回wrapper函数
    wrapper函数执行后返回的值是fast的计算结果。
    '''
    f = fast(11, 22)
    s = slow(11, 22, 33)

    def logg(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('begin call')
            a = fn(*args, **kw)
            print('the answer is %s' % a)
            print('end call')
            return a
        return wrapper

    @logg
    def func(x, y):
        time.sleep(0.0012)
        return x*y

    ff = func(4, 5)


# 二元方程式 ax**2 + bx + c = 0
# 输入a, b, c; 输出 x 的解
def mem1():
    import cmath
    import math

    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    def twoElements(a,b,c):
        d = b**2 - 4*a*c
        if d==0:
            x = (-b)/(2*a)
            print('only one solution: ', x)
        elif d>0:
            x1 = ((-b)+math.sqrt(d))/(2*a)
            x2 = ((-b)-math.sqrt(d))/(2*a)
            print('two solutions are {0} and {1}'.format(x1,x2))
        else:
            x1 = ((-b)+cmath.sqrt(d))/(2*a)
            x2 = ((-b)-cmath.sqrt(d))/(2*a)
            print('two solutions are {0} and {1}'.format(x1,x2))

    if a==0:
        if b==0 and c == 0:
            print('endless solutions')
        elif b==0 and c!=0:
            print('c input is not correct')
        elif b!=0:
            print('only one solution: ',-c/b)
    else:
        twoElements(a,b,c)

# 函数参数
def mem2():
    def f1(a, b=0, *args, **kw):
        print(a, b, args, kw)

    def f2(a, b=0, *, apple, orange, **kw):
        print(a, b, apple, orange, kw)

    f1(1)
    f1(1, 4, 'a', 'b', x=9, c=0)
    f1(1, 4, 'a', ('apple',0,0), ['dfs','dfs'],{'dfs','dfs'}, {'g':89,'o':'df'}, x=9)
    f2(1, 2, apple=90, orange='adf', appled=90)

    args = (1,2,3,4)
    kw = {'c':5, 'd':6}
    f1(*args,**kw)

# 计数器
def mem3():
    def createCounter():
        n = 0
        def counter():
            nonlocal n
            n = n + 1
            return n
        return counter

    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5

# 高级函数map, reduce, sort
def mem4():
    #第一个字符大写
    def normalize(name):
        return name.title()

    L1 = ['adam', 'LISA', 'barT fds']
    L2 = list(map(normalize, L1))
    print(L2)

    #累加
    def sum(*args):
        summary = 0
        for i in args:
            summary = summary + i
        return summary

    print('3 + 5 + 7 + 9 =', sum(13,43,34))

    #累乘
    from functools import reduce
    def prod(f):
        def multi(x,y):
            return x*y
        a = reduce(multi,f)
        return a
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

    #字符串转换浮点数
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def str2float(s):
        dotIndex = s.find('.')
        numStr = s[:dotIndex] + s[dotIndex + 1:]
        lam1 = lambda x,y: x*10+y
        lam2 = lambda x: DIGITS[x]
        num = map(lam2, numStr)
        return (reduce(lam1, num))/pow(10, (len(s)-(dotIndex+1)))
    print('str2float(\'123.456\') = ', str2float('123.456'))


    #排序
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2 = sorted(L, key = lambda t:t[0])
    print(L2)
    L3 = sorted(L, key = lambda t:t[1], reverse = True)
    print(L3)
















mem4()




