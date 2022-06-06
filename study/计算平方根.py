'''
计算算数平方根
'''

#二分法，不断找到中间值
def match(x: int) -> int:
    left, right, result = 0, x, -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            result = mid
            left = left + 1
        else:
            right = right - 1
    return result


print(match(2147395599))
