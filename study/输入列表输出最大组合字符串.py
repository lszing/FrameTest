'''思路为转为字符串 字符串排序为按位ascll码排序'''
class solution:
    def cambination(self,nums: list):
        nums1 = [str(i) for i in nums]
        nums1.sort(reverse=True)
        result = ''
        for i in nums1:
            result += i
        return result


if __name__ == '__main__':
    print(solution().cambination([12, 98, 435, 78, 24]))
