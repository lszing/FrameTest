# 字符串翻转
def reversal(str):
    revStr = ''
    for i in range(len(str) - 1, -1, -1):
        revStr += str[i]
    return revStr


# 寻找字符串中最大的回文
def solution(str):
    #float('-inf') 负无穷   float('inf') 正无穷
    lenth, result = float('-inf'), ''
    for i in range(len(str)):
        for j in range(1 + i, len(str)+1):
            if str[i:j] == str[i:j][::-1]:
                if j - i > lenth:
                    lenth = j - i
                    result = str[i:j]
    return result

if __name__ == '__main__':
    # print(reversal('asdfg'))
    print(solution('abbavbnmmnbv'))
    print(float("-inf"))