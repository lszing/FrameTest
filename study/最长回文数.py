def solution(a: str) -> str:
    lenth, result = float('-inf'), ''
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            if a[i:j] == a[i:j][::-1]:
                if j - i > lenth:
                    lenth = j - i
                    # result = a[i-1:j+1]
                    result = a[i:j]
    return result


def longestPalindrome(s: str) -> str:
    length = 0
    start = 0
    for i in range(len(s)):
        t = s[i - length - 1:i + 1]
        if i - length - 1 >= 0 and t == t[::-1]:
            start = i - length - 1
            length += 2
            continue
        t = s[i - length:i + 1]
        if i - length >= 0 and t == t[::-1]:
            start = i - length
            length += 1
    return s[start:start + length]


if __name__ == '__main__':
    print(solution('abbajbnmmnbj'))
    print(longestPalindrome('abbajjabb'))
    a='afdsafsadg'
    print(a[3:6])
