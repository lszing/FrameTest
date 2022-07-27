'''
解法1
去重后求和，2倍和-原有和
'''


def findOnlyOne(nums: list[int]) -> int:
    return sum(set(nums)) * 2 - sum(nums)


print(findOnlyOne([2, 2, 1, 1, 3]))
'''
答复
解法2 
异或与交换律
交换律 a^b^c=a^c^b
任何数与0异或结果都为这个数 即 1^0=1
两个相同的数异或结果都为0 即 1^1=0
则 [1,1,2,3,2] 1^1^2^3^2=0^2^3^2=0^3=3
'''


def singleNumber(nums: list[int]) -> int:
    a = 0
    for i in range(len(nums)):
        a = a ^ nums[i]
    return a


def singleNumber1(nums: list) -> str:
    a = 0
    for i in range(len(nums)):
        a ^= nums[i]
    return a


print(singleNumber([1, 3, 4, 2, 1, 4, 3]))
print(singleNumber1([1, 3, 4, 2, 1, 4, 3 ]))


def singleNumber2(nums:list)->str:
    return sum(set(nums))*2-sum(nums)
print(singleNumber2([1, 3, 4, 2, 1, 4, 3]))
