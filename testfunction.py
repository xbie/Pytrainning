# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点
def test1():
    s1 = 72
    s2 = 85
    r = (s2 - s1)/s1*100
    print('%.1f%%'%r)
    print('{:.1f}%'.format(r))

# 请用索引取出下面list的指定元素
def test2():
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    print(L[0][0])
    print(L[1][1])
    print(L[2][2])

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
def test3():
    height = 1.75
    weight = 80.5
    bmi =  weight / (height ** 2)
    if bmi <= 18.5:
        print('slim')
    elif bmi <= 25:
        print('normal')
    elif bmi <= 28:
        print('a little fat')
    elif bmi <= 32:
        print('fat')
    else:
        print('so fat')

# 利用循环依次对list中的每个名字打印出Hello, xxx!：
def test4():
    L = ['Bart', 'Lisa', 'Adam']
    n = 0
    while n < len(L):
        print('Hello, {0}!'.format(L[n]), end = '  ')
        n = n + 1
    print()
    for x in L:
        print('Hello, %s!'%x)

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
def test5():
    n1 = 255
    n2 = 1000
    print(hex(n1), hex(n2))

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。
def test6():
    import math
    def quadratic(a, b, c):
        num = b * b - 4 * a * c
        root1 = (-b + math.sqrt(num))/(2*a)
        root2 = (-b - math.sqrt(num))/(2*a)
        print('The answer is {0} and {1}'.format(root1, root2))
    quadratic(1, 3, -4)
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def test7():
    def product(x, *args):
        answer = x
        for i in args:
            answer = answer * i
        return answer
    print(product(5, 6, 7, 9))

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def test8():
    def trim(s):
        for i in s:
            if s[:1] == ' ':
                s = s[1:]
            if s[-1:] == ' ':
                s = s[:-1]
        return s
    def trim2(s):
        if s[:1] != ' ' and s[-1:] != ' ':
            return s
        elif s[:1] == ' ':
            return trim2(s[1:])
        else:
            return trim2(s[:-1])
    s1 = trim2('     hello   ')
    print(s1, '123')


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def test9():
    def findMinAndMax(L):
        if L == []:
            maxl = minl = None
        else:
            maxl = L[0]
            minl = L[0]
        for x in L:
            if maxl < x:
                maxl = x
            if minl > x:
                minl = x
        return (minl, maxl)
    def findMinAndMax2(L):
        if L == []:
            return None, None
        else:
            L.sort()
            return (L[0], L[-1])
    print(findMinAndMax2([5, 3, 2, 90]))


# 请用列表生成式将['Hello', 'World', 18, 'Apple', None]改成['hello', 'world', 'apple']
def test10():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print(L2)

# 斐波那契数列生成器
def test11():
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1

    f = fib(9)
    print(fib, '\n', fib(9))
    # for n in f:
    #     print(n, end = ' ')
    while True:
        try:
            x = next(f)
            print(x)
        except StopIteration as e:
            print('Generator return value', e.value)
            break

'''
杨辉三角
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
试写一个generator, 不断输出下一行
'''
# 1: L[0] = L[-1] + L[0], 2: L[1] = L[0]+L[1], 1: L[2] = L[1] + L[2]
# plus 1 1 0
def test12():
    def triangles():
        L = [1]
        while True:
            yield L
            L.append(0)
            # i = 0
            # while i < len(L):
            #     L2[i] = L[i-1] + L[i]
            #     i = i + 1
            L = [L[i-1] + L[i] for i in range(len(L))]

    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break

# 高阶函数，函数式编程
def test13():
    def add (x, y, f):
        return f(x) + f(y)
    print(add(-8, 6, abs))

# map() and reduce(), 自己编写 string to int 的函数
# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def test14():
    from functools import reduce
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(ch):
        return DIGITS[ch]

    def str2int(s):
        f = map(char2num, s)
        a = reduce(lambda x, y: x * 10 + y, f)
        return a

    print(char2num('3'), str2int('3242'))

    def normalize(name):
        def mytitle(namel):
           # namel = namel[0].upper() + namel[1:].lower()
            return namel.title()

        name2 = map(mytitle, name)
        return name2
    answer = normalize(['adam', 'LIASA dG', 'barT'])
    print(list(answer))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def test15():
    def is_palindrome(n):
        s1 = str(n)
        s2 = s1[::-1]
        return s1 == s2

    palindromes = filter(is_palindrome, range(1,200))
    print(list(palindromes))

# 我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按名字排序，按成绩排序
def test16():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    def by_name(t):
        return t[0]

    def by_score(t):
        return t[-1]


    L2 = sorted(L, key=by_name)
    print(L2)
    L3 = sorted(L, key=by_score, reverse=True)
    print(L3)

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def test17():
    def createcounter():
        i = 0
        def counter():
            nonlocal i
            i = i + 1
            return i
        return counter

    counterA = createcounter()  # counterA = counter, counterA() = i
    print(counterA(), counterA(), counterA(), counterA())

# 输出1～20间的奇数
def test18():
    L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
    print(L)
    f = test17
    print(f.__name__)

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def test19():
    import time, functools
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            t1 = time.time()
            fn(*args, **kw)
            t2 = time.time()
            print('%s executed in %s ms' % (fn.__name__, t2 - t1))
            return fn(*args, **kw)
        return wrapper

    def log(text):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                t1 = time.time()
                fn(*args, **kw)
                t2 = time.time()
                print('%s %s executed in %s ms' % (text,fn.__name__, t2 - t1))
                return fn(*args, **kw)
            return wrapper
        return decorator

    @metric # fast = metric(fast) => wrapper(*args, **kw) => fn(*args, **kw)
    def fast(x, y):
        time.sleep(0.0012)
        return x + y

    @log('The') # slow = log('The')(slow)
    def slow(x, y, z):
        time.sleep(0.123)
        return x + y + z

    def common(x, y):
        time.sleep(0.0012)
        return x + y

    f1 = fast(11, 22)
    print(f1)
    f2 = slow(11, 22, 33)
    # 闭包的意义就在于函数的不断深入调用，在既有计算结果下继续引入新的参数。
    print(slow.__name__, f2)
    f3 = metric(common)(11, 33)
    print(f3)
    f4 = log('The name')(common)(11, 22)
    print(f4)

# 偏函数二进制int()
def test20():
    def int2(x, base = 2):
        return int(x, base)

    print(int('01110100'), int2('01110100'), int('01110100', 2))

#IO操作
def test21():
    #读写文件
    with open('/Users/antisi/Documents/Code/foros/new.txt', 'w') as f:
        f.write('Hello World!!')

    f = open('/Users/antisi/Documents/Code/foros/new.txt', 'r', encoding='UTF-8', errors='ignore')
    print(f.readline())
    f.close()

    from io import StringIO
    f = StringIO()
    f.write('hello world')
    f.write('!!')
    print(f.getvalue())

    #操作文件夹
    import os
    print(os.path.abspath('.'))
    os.rmdir('/Users/antisi/Documents/Code/foros/apple')
    paths = os.path.join('/Users/antisi/Documents/Code/foros', 'apple')
    os.mkdir(paths)

    # 序列化
    ADDRE = '/Users/antisi/Documents/Code/foros/new.txt'
    import pickle
    d = dict(name='Bob', age=20, score=88)
    with open('/Users/antisi/Documents/Code/foros/new.txt', 'wb') as f:
        pickle.dump(d, f)
    with open(ADDRE, 'rb') as f:
        d = pickle.load(f)
        print(d)

    import json
    obj = dict(name='小明', age=20)
    s = json.dumps(obj,  ensure_ascii=True,)
    print(obj,s)

# datetime日期时间操作，获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp

def test22():
    import re
    from datetime import datetime, timedelta, timezone
    def to_timestamp(dt_str, tz_str):
        regex = re.match(r'^UTC([\+\-]\d{1,2}):\d{2}', tz_str)
        intre = int(regex.group(1))
        utch = timezone(timedelta(hours=intre))
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        dt2 = dt.replace(tzinfo=utch)
        dts = dt2.timestamp()
        return dts

    t1 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
    print(t1)
    assert t1 == 1433121030.0










test22()









#


















