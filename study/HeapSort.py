# 堆排序
# 生成一个大顶堆
def MAX_HEAP(a):
    n = len(a)
    # (n-2)//2-1为完全二叉树最后一个非叶子节点  ps:非叶子节点即度不为0的节点/有子树的节点
    # n n-1 n-2 .... 0
    # 循环从下到上拿到非叶子节点
    for i in range((n - 2) // 2, -1, -1):
        BUILD_MAX_HEAP(a, n, i)
    print(a)


# i 非叶子节点
# a 列表
# length 列表长度
def BUILD_MAX_HEAP(a, length, i):
    last = i  # 非叶子节点索引值
    left = 2 * i + 1  # 非叶子节点左子树索引值
    right = 2 * i + 2  # 非叶子节点右子树索引值
    # 若非叶子节点值比左子树节点值小，则将拿到左子树索引值，这时last为最大值索引
    if left < length and a[i] < a[left]:
        last = left
    # 若右子树节点值比last大，则将last赋值为右子树索引
    if right < length and a[last] < a[right]:
        last = right
    # 判断若现在last最大值索引与方法传进来的非叶子节点索引不同则互换节点值
    if last != i:
        a[last], a[i] = a[i], a[last]
        # 递归，在MAX_HEAP方法中调用的BUILD_MAX_HEAP 因为先传入的是最后一个非叶子节点，MAX_HEAP方法将待排序列表/数组生成一个大顶堆
        BUILD_MAX_HEAP(a, length, last)


def HEAPSORT(a):
    # 生成一个大顶堆
    MAX_HEAP(a)
    # 遍历列表（每次列表长度-1，直到0），每次现将最后一位与根节点调换位置(将列表最大值放到列表最后一位)
    for i in range(len(a) - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        # 每次调用BUILD_MAX_HEAP，i传入0，即从上至下将最大值放到当前列表最后一位
        BUILD_MAX_HEAP(a, i, 0)


if __name__ == '__main__':
    a = [1, 5, 7, 22, 2, 0, 9]
    HEAPSORT(a)
    # MAX_HEAP(a)
    print(a)
