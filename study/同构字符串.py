'''
输入：s = "egg", t = "add"
输出：true

输入：s = "paper", t = "title"
输出：true
'''


def isIsomorphic(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


print(isIsomorphic('title', 'paper'))

# zip  用法
a = [1, 2, 3]
b = [4, 5, 6]
# 输出[(1,2),(2,5),(3,6)]
print(list(zip(a, b)))


def isIsomorphic1(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


print(isIsomorphic1('title', 'paper'))
