'''给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。

子字符串 是字符串中的一个连续字符序列。'''


def solution(s: str):
    return max([s.rfind(i) - s.find(i) - 1 for i in s])


def b(func):
    def swapper():
        print('b')
        func()

    return swapper


def c(func):
    def swapper():
        print('c')
        func()

    return swapper


@c
@b
def a():
    print('a')


if __name__ == '__main__':
    a()

