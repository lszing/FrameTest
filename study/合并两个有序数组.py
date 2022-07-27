def mergeArray(nums1: list[int], m1, nums2: list[int], m2) -> None:
    # 合并后数组最后一位坐标
    tail = m1 + m2 - 1
    # 合并前p1 p2 最后一位坐标
    p1, p2 = m1 - 1, m2 - 1
    while p1 >= 0 or p2 >= 0:
        # 判断p1位置在第一位后咋代表nums1没有了则把nums2剩余的依次放到合并数组里
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        # nums1最后一位大与nums2最后一位则把nums1最后一位放到合并数组里，p1指针向前移
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        # 与上面相反
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1
    print(nums1)


if __name__ == '__main__':
    mergeArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)


    def testMe(nums1: list[int], m, nums2: list[int], n):
        p1, p2 = m - 1, n - 1
        target = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[target] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[target] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[target] = nums1[p1]
                p1 -= 1
            else:
                nums1[target] = nums2[p2]
                p2 -= 1
            target -= 1
        print(nums1)


    testMe([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)


    def mergeArray1(nums1: list[int], m, nums2: list[int], n):
        tail = m + n - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        print(nums1)


    print(mergeArray1([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


    def mergeArray2(nums1: list, n1: int, nums2: list, n2: int) -> list:
        tail = n1 + n2 - 1
        l1, l2 = n1 - 1, n2 - 1
        while l1 >= 0 or l2 >= 0:
            if l1 == -1:
                nums1[tail] = nums2[l2]
                l2 -= 1
            elif l2 == -1:
                nums1[tail] = nums1[l1]
                l1 -= 1
            elif nums1[l1] > nums2[l2]:
                nums1[tail] = nums1[l1]
                l1 -= 1
            else:
                nums1[tail] = nums2[l2]
                l2 -= 1
            tail -= 1
        print(f'mergeArray2 is {nums1}')

    mergeArray2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
