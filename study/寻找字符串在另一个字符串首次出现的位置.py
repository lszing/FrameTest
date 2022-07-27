class solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        t = 0
        while t + len(needle) < len(haystack):
            if haystack[t:t + len(needle)] == needle:
                return t
            t += 1
        return -1


if __name__ == '__main__':
    # 输出2
    print(solution().strStr('hello', 'll'))
    strs = 'helloll'
    s = 'll'
    print(strs.find(s))


    def findFirst(needle: str, haystack: str) -> int:
        if len(haystack) < len(needle):
            return -1
        a = 0
        while a+len(needle) <= len(haystack):
            if haystack[a:a+len(needle)] == needle:
                return a
            else:
                a += 1
        return -1


    print(findFirst('ll', 'healloll'))
