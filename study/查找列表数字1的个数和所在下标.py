class Solution:
    def findstr(self, l: list):
        num = 0
        result = []
        for i, j in enumerate(l):
            if j == 1:
                num += 1
                result.append(i)
        return num, result


if __name__ == '__main__':
    print(Solution().findstr([1, 3, 4, 2, 1, 4, 1]))
