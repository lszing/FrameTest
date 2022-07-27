# python中字符串是可以比较的 按照ascll码排序 ascll码比较是字符串每个字符ascll值
# 因此只需比较最小字符串和最大字符串相同前缀就可以
# 重点在于列表 max min方法按照ascll比较
# 最大字符串与最小字符串按位比较若相同则代表中间都相同
class Solution():
    def longestCommonPrefix(self, nums: list) -> str:
        max_str = max(nums)
        min_str = min(nums)
        # seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        # list(enumerate(seasons))
        # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        # list(enumerate(seasons,1))
        # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
        for i, x in enumerate(min_str):
            if x != max_str[i]:
                return max_str[:i]
        return min_str


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))

    def longestCommonPrefix1(nums: list) -> str:
        maxStr = max(nums)
        minStr = min(nums)
        for i, j in enumerate(minStr):
            if j != maxStr[i]:
                return minStr[:i]
        return minStr

    print(longestCommonPrefix1(strs))
