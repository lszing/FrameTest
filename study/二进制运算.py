
'''
二进制求和
'''
def addBinary(a, b) -> str:
    print(bin(int(a, 2) + int(b, 2)))
    return '{0:b}'.format(int(a, 2) + int(b, 2))

print(addBinary('11', '10'))
