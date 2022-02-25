def isValid(str: str) -> bool:
    if len(str) % 2 != 0:
        return False
    list = []
    for i in range(len(str)):
        if '{' == str[i] or '[' == str[i] or '<' == str[i]:
            list.append(str[i])
            continue
        if ']' == str[i] and list and list.pop() == '[':
            continue
        if '>' == str[i] and list and list.pop() == '<':
            continue
        if '}' == str[i] and list and list.pop() == '{':
            continue
        return False
    if len(list) == 0:
        return True
    else:
        return False


def isValidd(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    bracket_dict = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    for c in s:
        if c in bracket_dict:  # 这里判断字典键值是否有C
            # stack[-1]-----list最后一位
            if len(stack) > 0 and bracket_dict[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack


def isValiddd(s: str) -> bool:
    while '{}' in s or '[]' in s or '()' in s or '<>' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
        s = s.replace('<>', '')
    return s == ''


if __name__ == '__main__':
    # print(isValidd('{[<>]}'))
    print(isValidd('{[<>]}'))
    print(isValidd('}{[<>]}{'))


    def solution(str):
        re_dict = {'}': '{', '>': '<', ']': '[', ')': '('}
        tmp_list = []
        for s in str:
            if s in re_dict:
                if len(tmp_list) > 0 and re_dict[s] == tmp_list[-1]:
                    tmp_list.pop()
                else:
                    return False
            else:
                tmp_list.append(s)
        return not tmp_list


    print(solution('{}{{{}}}()<><<>><{}>'))
    print(isValiddd('{}{{{}}}()<><<>><{}>'))
    print(isValiddd('><'))


    def so(s: str):
        if len(s) % 2 != 0:
            return False
        r_dict = {'}': '{', ']': '[', ')': '(', '>': '<'}
        c_list = []
        for i in s:
            if i in r_dict:
                if len(c_list) > 0 and r_dict[i] == c_list[-1]:
                    c_list.pop()
                else:
                    return False
            else:
                c_list.append(i)
        return not c_list


    print('so is ', so('{}{{{}}}()<><<>><{}>'))


    def ss(s: str):
        while '[]' in s or '{}' in s or '<>' in s or '()' in s:
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('<>', '')
            s = s.replace('()', '')
        return s == ''


    print('ss is ', ss('{}{{{}}}()<><<>><{}>'))
