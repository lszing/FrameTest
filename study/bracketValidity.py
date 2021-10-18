def isValid(str: str) -> bool:
    if len(str) % 2 != 0:
        return False
    list = []
    for i in range(len(str)):
        if '{' == str[i] or '[' == str[i] or '<' == str[i]:
            list.append(str[i])
            continue
        if ']' == str[i] and list.pop() == '[':
            continue
        if '>' == str[i] and list.pop() == '<':
            continue
        if '}' == str[i] and list.pop() == '{':
            continue
        return False
    if len(list) == 0:
        return True
    else:
        return False

def isValidd(s: str) -> bool:
    if len(s)%2!=0:
        return False
    bracket_dict={")":"(","]":"[","}":"{",">":"<"}
    stack=[]
    for c in s:
        if c in bracket_dict:#这里判断字典键值是否有C
            if len(stack)>0 and bracket_dict[c]==stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack

if __name__ == '__main__':
    # print(isValidd('{[<>]}'))
    print(isValidd('{[<>]}'))
    print(isValidd('}{[<>]}{'))