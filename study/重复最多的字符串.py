def solution(str):
    max_result = ''
    max_count = 0
    i = 0
    j = 1
    while j < len(str):
        # 相等则j++ 直到找到不相等的
        if str[i] == str[j]:
            j += 1
        # 兼容索引越界
        if j > len(str) - 1:
            return max_result
        # 找到不相同的 计算相同的长度 记录下来  or兼容最后一位
        if str[i] != str[j] or j == len(str) - 1:
            # 兼容最后一位 长度+1
            if j == len(str) - 1:
                j += 1
            # 长度大于记录的最大长度 赋值
            if j - i > max_count:
                max_count = j - i
                max_result = str[i:j]
            i = j
            j = i + 1

    return max_result


if __name__ == '__main__':
    print(solution("aabbbccfsdaggsdaaffdcccc"))
