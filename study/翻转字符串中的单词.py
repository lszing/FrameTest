# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
'''输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc" '''


def reverseWords(s: str) -> str:
    s_list = s.split(' ')
    return ' '.join(i[::-1] for i in s_list)

#列表也可以翻转
def reverseWords1(s: str) -> str:
    return (' '.join(s.split()[::-1]))[::-1]


print(reverseWords('let go'))
print(reverseWords1('let go'))


