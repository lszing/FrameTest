# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
class Solution:
    def removeDuplicates(self, nums: list[int]) -> list:
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                nums.pop(b)
                continue
            else:
                a += 1
                b += 1
        return nums


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2, 2, 4, 5, 5, 5]))


    def removeRepeat(nums: list[int]) -> list[int]:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
                continue
            else:
                i += 1
                j += 1
        return nums


    print(removeRepeat([1, 1, 2, 2, 4, 5, 5, 5]))
