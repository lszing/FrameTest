'''
 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式
 不能使用任何内置的 BigInteger 库或直接将输入转换为整数
'''


def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
    ans = '0'
    m, n = len(num1), len(num2)
    for i in range(n - 1, -1, -1):
        add = 0
        y = int(num2[i])
        # 补零个数
        curr = ['0'] * (n - 1 - i)
        for j in range(m - 1, -1, -1):
            # 两数相乘
            product = int(num1[j]) * y + add
            # 拿到最后一位拼到curr
            curr.append(str(product % 10))
            # 拿到进位赋值给add用于下次相乘进位
            add = product // 10
        if add > 0:
            curr.append(str(add))
        curr = ''.join(curr[::-1])
        ans = addStrings(ans, curr)
    return ans


def addStrings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    add = 0
    ans = list()
    while i >= 0 or j >= 0 or add != 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        result = x + y + add
        ans.append(str(result % 10))
        add = result // 10
        j -= 1
        i -= 1
    return ''.join(ans[::-1])


print(multiply('12', '13'))
