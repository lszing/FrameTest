class test:
    a = '1'
    b = 2
    c = 3
    d = 4


class test1:
    a = '1'
    b = 2
    c = 3
    d = 4


def c(func):
    def ww(b):
        result = func(b)
        result += 1
        print(f'result is {result}')

    return ww


@c
def a(b):
    b += 1
    return b

if __name__ == '__main__':
    # test = test
    # test1 = test1
    # list = [test, test1]
    #
    # list1 = [i.b for i in list]
    #
    # print(list1)
    a(3)


    def checkRecord(s: str) -> bool:
        len_A = 0
        slow = 0
        fast = 1
        while fast <= len(s):
            if len_A >= 2:
                return False
            if s[slow:fast] == 'A':
                len_A += 1
            if s[slow:fast] == 'L' and s[slow+1 :fast + 1] == 'L' and s[slow+2:fast + 2] == 'L':
                return False
            slow += 1
            fast += 1
        return True
    print(checkRecord('ALL'))

    str='ALL'
    print(str[2:4])
