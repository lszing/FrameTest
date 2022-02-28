'''统计字符串中某个字符出现的个数
解题思路1：按照指定字符切分字符串
解题思路2：笨方法遍历
'''


class solution():
    def statisticalTimes(self, s, keyword):
        key_list = s.split(keyword)
        return len(key_list) - 1

    def statisticalTimes1(self, s, keyword):
        keyLen = len(keyword)
        a = 0
        result = 0
        while a < len(s):
            if s[a:a + keyLen] == keyword:
                result += 1
                a += keyLen
            else:
                a += 1
        return result

    def statisticalTimes2(self, s, keyword):
        return (s.count(keyword))


if __name__ == '__main__':
    print(solution().statisticalTimes('AABBABBACAABCAA', 'AA'))
    print(solution().statisticalTimes1('AABBABBACAABCAA', 'AA'))
    print(solution().statisticalTimes2('AABBABBACAABCAA', 'AA'))
