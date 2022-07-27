from collections import Counter

# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素
'''
解法1hash表记录每个元素出现的个数找到数量大于n/2的元素
'''
# collections.Counter快速统计出数组元素的个数
a = [2, 2, 1, 1, 1, 2, 2]
print(dict(Counter(a)))


def majorityElement1(nums: list[int]) -> int:
    counts = Counter(nums)
    print(counts.get)
    print(counts.keys())
    # 按照字典值对key进行排序获取最大值
    return max(counts.keys(), key=counts.get)


print(majorityElement1(a))

'''
解法2 如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为n/2的元素（下标从 0 开始）一定是众数。

'''


def majorityElement2(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


print(majorityElement2(a))


def majorityElement3(nums: list[int]) -> int:
    counts = Counter(nums)
    return max(counts.keys(),key=counts.get)