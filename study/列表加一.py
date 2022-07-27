'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
[1,2,3,9]-->[1,2,4,0]
'''


def plusOne(l: list[int]) -> list[int]:
    return (list(map(int, list(str(int(''.join(map(str, l))) + 1)))))


print(plusOne([1, 2, 3, 9]))

print(list('1234'))
print(list(map(int, '1234')))


def plusOne1(l: list[int]) -> list[int]:
    return list(map(int, list(str(int(''.join(list(map(str, l)))) + 1))))


print(plusOne1([1, 2, 3, 9]))
