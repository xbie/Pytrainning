# 正则表达式，匹配，切分，分组，预编译
import re

a = re.match(r'^\d{3}-\d{3,10}', '010-12345')
print(a)
str1 = 'a,b;;c  d'
str2 = re.split(r'[\,\;\s]+', str1)
print(str2)

re_tele = re.compile(r'^(\d{3})-(\d{3,8})$')
b = re_tele.match('010-2784738')
print(b.groups(), b.group(0), b.group(1), b.group(2))

# 验证Email地址的正确性, someone@gmail.com.  bill.gates@microsoft.com
def is_valid_email(addr):
    reemail = re.compile(r'^([0-9a-zA-Z\_\.]+)@(\w+\.com)$')
    sre = reemail.match(addr)
    return sre
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('apple#gmail.comdd')
assert not is_valid_email('mr-bob@example.com')

# 提取带名字的Email地址
def name_of_email(addr):
    # sre2 = re.match(r'^<([\w\s]+)>', addr)
    # if sre2:
    #     return sre2.group(1)
    reemail = re.compile(r'^([0-9a-zA-Z\_.]+)@\w+\.(org|com)$')
    sre = reemail.match(addr)
    if sre:
        return sre.group(1)
    else:
        return None

assert not name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')