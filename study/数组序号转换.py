'''给你一个整数数组arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。'''
import enum


def arrayRankTransform(arr):
    print(set(arr))

    '''sorted 只能用在list上'''
    '''sorted 语法：
sorted(iterable, key=None, reverse=False)  
参数说明：
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。'''
    a = sorted(set(arr))
    d = {}
    for i, v in enumerate(a, 1):
        d[v] = i
    return [d[i] for i in arr]

'''
枚举类
    不可外部修改类变量，不允许重复变量
'''
class testt(enum.Enum):
    TEST = 1
    TEST2 = 1


print(arrayRankTransform(['1', '44', '2']))
testt.TEST = 3
