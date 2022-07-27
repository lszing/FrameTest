def mergeArray(nums1: list[int], m1, nums2: list[int], m2) -> None:
    tail = m1 + m2 - 1
    p1, p2 = m1 - 1, m2 - 1
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
