'''
输入一个数，找到大于该数100之内的所有质数并降序排列
要求：
1.输入数字小于0时，按照从0开始计算
2.输入数字非正整数时，按照取整进行计算
'''


def solution(s: int):
    result = []
    temp = False
    if s <= 0:
        t = 100
    else:
        t = s + 100
    for i in range(t, s, -1):
        for j in range(2, i):
            # 有一个取余等于0就代表不是质数，结束循环
            if i % j == 0:
                temp = True
                break
        if temp is False:
            result.append(i)
        temp = False
    return result


print(solution(0))


def solution1(s: int) -> list:
    result = []
    temp = True
    if s <= 0:
        t = 100
    else:
        t = s + 100
    for i in range(t, s, -1):
        for j in range(2, i):
            if i % j == 0:
                temp = True
                break
        if temp is False:
            result.append(i)
        temp = False
    return result


print(solution1(0))
