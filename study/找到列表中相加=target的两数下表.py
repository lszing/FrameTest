class Solution():
    def twoSum(self, nums: list, target: int) -> list:
        a = dict()
        for i in range(len(nums)):
            c = target - nums[i]
            if c in a:
                return [a[c], i]
            a[nums[i]] = i

    def twoSum1(self, nums: list, target: int) -> list:
        a = dict()
        for i, num in enumerate(nums):
            if a.get(target - num) is not None:
                return [i, a.get(target - num)]
            a[num] = i


if __name__ == '__main__':
    print(Solution().twoSum([1, 2, 3, 4], 7))
    print(Solution().twoSum([1, 2, 3, 4], 7))
    li = ['a', 'b', 'c', 'd']
    print(list(enumerate(li)))
