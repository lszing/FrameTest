#链表操作
# 节点
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLinkList(object):
    def __init__(self):
        # 定义一个链表
        # 首地址指针__head
        self.__head = None
        # self.__head = Node(None)

    # 判断链表是否为空  即头节点连接域指向空值则认为是空链表
    def is_empty(self):
        return self.__head == None

    # 链表长度
    def length(self):
        count = 0
        # cur初始指向头结点
        cur = self.__head
        # 最后一个节点的链接域则指向一个空值 因此while
        while cur is not None:
            count += 1
            # 后移一位
            cur = cur.next
        return count

    # 遍历链表
    def travel(self):
        if self.__head is not None:
            cur = self.__head
            while cur != None:
                # 输出当前节点数据
                print(cur.data)

                # yield 生成器
                # yield cur.item
                # 指针后移
                cur = cur.next
            return ''

    # 清空链表
    def clear_list(self):
        self.__head = None

    # 索引列表
    def index_variables(self, index):
        p = self.__head
        # 遍历入参索引 每一次都往后移一位
        for i in range(index):
            if p is None:
                raise IndexError("list index out of range")
            p = p.next
        return p.data

    # 向链表尾部插入节点
    def append(self, data):
        if self.__head is None:
            self.__head = Node(data)
        else:
            p = self.__head
            # 这里因为self.__head不为空 因此p有next属性
            while p.next is not None:
                p = p.next
            p.next = Node(data)

    # 头部插入
    def head_insert(self, data):
        d = Node(data)
        # 新节点指针指向原头部节点
        d.next = self.__head
        # 头部指针修改为新节点
        self.__head = d

    # 索引插入
    def index_insert(self, index_, val):
        p = self.__head
        # 找到索引位置
        for item in range(index_):
            if p is None:
                break
            p = p.next
        node = Node(val)
        # 插入节点连接后半部分节点 即插入节点指向位置 等于 p节点指向位置
        node.next = p.next
        # 前半部分连接插入节点 即p节点指向位置为node节点
        p.next = node

    # 删除指定位置节点
    def index_delete(self, index_):
        pre = None
        p = self.__head
        for item in range(index_):
            if p is None:
                break
            # 前一位节点
            pre = p
            # 当前位节点
            p = p.next
        if p is None:
            pass  # 超过最大位置不删除
        else:
            # 前一位节点指针指向要删除节点的指针指向
            pre.next = p.next

    # 删除指定数据的节点
    def delete_val(self, val):
        p = self.__head
        pre = None
        # 结束循环必须其中一个为假
        while p and p.data != val:
            pre = p
            p = p.next
        if p is None:
            print(val, " not in linklist")
        else:
            pre.next = p.next

    # 有序链表（从小到大）中插入单个节点，保证链表依然有序
    def insert_val(self, data):
        p = self.__head
        previous = None
        if p is None:
            self.__head = Node(data)
        else:
            while p is not None and data > p.data:
                previous = p
                p = p.next
            previous.next = Node(data, p)

    # 魔术方法 str(对象) 或 print(对象)时调用
    def __str__(self):
        data_list = []
        d = self.__head
        while d is not None:
            data_list.append(str(d.data))
            d = d.next
        # json()返回通过指定字符连接序列中元素后生成的新字符串。 即'->'.json(list) list('1','2','3')=>>> 1->2->3
        return '->'.join(data_list)

    def look(self, head):
        list = []
        d = head
        while d is not None:
            list.append(str(d.data))
            d = d.next
        return '->'.join(list)

    # 判断单链表是否有环 使用快慢指针
    def isCycle(self):
        fast = slow = self.__head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 这里判断的是内存地址
            if fast is slow:
                return True
        return False

    # 构建有环链表 逻辑为找到要循环的节点位置 将末尾节点指针指向要循环节点位置
    def createCycleLinkList(self):
        self.append(12)
        self.append(13)
        self.append(1)
        self.append(15)
        self.append(2)
        self.append(15)
        self.append(3)
        self.append(15)
        node = Node(16)
        last = self.__head
        entry = self.__head
        # 找到链表尾节点
        while last.next is not None:
            last = last.next
        while entry.data != 1:  # 入环点为1
            entry = entry.next
        last.next = node
        node.next = entry

    # 判断有环链表入环点  hash解法
    def detectCycleHash(self):
        p = self.__head
        if not p:
            return None
        dict = {}
        while p is not None:
            if p in dict:
                return p.data
            dict[p] = p
            p = p.next
        return None

    # 判断有环链表入环点
    # 设链表头节点到入环点距离为x
    # 入环点到首次相遇的点距离为y
    # 首次相遇点到入环点距离为z
    # 到首次相遇点slow走了x+y
    # 到首次相遇点fast走了x+y+n(y+z)（fast多走了n圈）
    # 又因为y的速度比x快一倍 相同时间内 距离也是2倍
    # 即2(x+y)=x+y+n(y+z)
    # x=(n-1)y+nz==>x=n(y+z)-y
    # 即头节点到入环点距离为n圈-入环点到相遇点的距离
    # 这时将任意一个放到头节点，另一个从相遇点出发 同时移动1个节点 相遇位置即是入环点
    # 总结链表头到入环点距离等于首次相遇点到入环点距离
    def detectCycle(self):
        fast = slow = self.__head
        if fast is None:
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = self.__head
        while fast:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return fast.data

    # 两单链表在某点相交，找出相交的起点 hash解法
    def findFocusHash(self, headA, headB):
        if (headA is None) or (headB is None):
            return None
        cur = headA
        dict = {}
        while cur is None:
            # 这里键值是内存地址
            dict[cur] = 1
            cur = cur.next
        cur = headB
        while cur is None:
            # 这里判断的不是节点的值 而是内存地址 所以是唯一的 这样就排除了其他非相交节点值相同的情况
            if cur in dict:
                return cur.data
            cur = cur.next
        return None

    # 两单链表在某点相交，找出相交的起点 指针解法
    # 思路为将两个单链表A B 连在一起 AB BA  如下
    # 7->3->4->6->0->   1->4->6->0
    # 1->4->6->0->   7->3->4->6->0
    # #####################4->6->0
    # 同时移动连接后的两条长链表 找到地址相同位置即是相交点3
    def findFocus(self, headA, headB):
        if (headA is None) or (headB is None):
            return None
        a = headA
        b = headB
        while a and b:
            # 如果a节点地址等于b节点地址则代表相交
            if a == b:
                return a.data
            # 每次向后移动一个节点距离
            a = a.next
            b = b.next
            # a走到链表尾后指向b链表
            if a is None:
                a = headB
            # b走到链表尾后指向A链表
            if b is None:
                b = headA
            # 开始下一轮循环直到找到最后相交的点
        return None

    # 删除链表倒数第N个节点
    # 思路为计算链表长度，链表长度-N+1为要删除节点位置
    def ddescN(self, n):
        cur = self.__head
        len = 0
        while cur is not None:
            cur = cur.next
            len += 1
        pre = None
        cur = self.__head
        # 位置删除节点
        for i in range(len - n):
            if cur:
                pre = cur
                cur = cur.next
        pre.next = cur.next

    # 删除链表倒数第N个节点 快慢指针解法
    def ddNFS(self, n):
        fast = slow = self.__head
        count = 0
        while fast is not None:
            fast = fast.next
            count += 1
        if n == count:
            self.__head = self.__head.next
            return
        for i in range(n):
            fast = fast.next
        pre = None
        while fast is not None:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next

    # 反转链表
    # 整体思路为 设置一个新的空链表  每次把需要反转链表的头结点 插入到新链表的头节点
    # 1.先把next指向第二个节点 相当于记录
    # 2.将头节点单独拿出来 即cur.next=pre  第一次pre为None  即只有头结点指针指向None
    # 3.将头节点赋值给pre 即pre指向头节点地址  这样就保证下一次循环 第二步会把新的头结点的指针域指向上一个头结点 实现新链表头部插入
    # 4.next节点赋值给头指针 即头结点
    def reversalLinkList(self):
        preNode = None
        nextNode = None
        cur = self.__head
        if cur is None or cur.next is None:
            return
        while cur is not None:
            # 将第二个节点赋值给next 即next指向第二个节点
            nextNode = cur.next
            # 将第一个节点的指针指向空值 相当第一次循环把第一个节点单独拿出来了
            cur.next = preNode
            # 将头节点复制给pre 即pre此时指向节点1 即节点一为“上一个节点“
            preNode = cur
            # 第二个节点赋值为头结点
            cur = nextNode
        return preNode

    def test(self):
        if self.__head is None or self.__head.next is None:
            return self.__head
        pre = None
        nex = None
        cur = self.__head
        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

    # 移除单链表中元素
    def deleteVal(self, data):
        if self.__head is None:
            return
        head = self.__head
        # 找到第一个不为data的节点 如果表头是则指针后移
        if data == head.data:
            head = head.next
        slow = head
        fast = head.next
        while fast:
            if fast.data == data:
                # 注意这样是不行的  这样fast指针没有后移
                slow.next = fast.next
                # 这是正确的
                # fast先指针后移 这样才能确保下次循环fast后移一位
                # slow指针域指向fast
                fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next

    # 奇偶链表
    def oddEvenList(self):
        head = self.__head
        if not head or not head.next or not head.next.next:
            return
        odd, even, head1 = head, head.next, head.next  # head1用于记录偶数序号节点的头节点
        while even and even.next:  # 两个停止条件分别对应于节点总个数为奇数和偶数的情况
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = head1
        list = []
        while head:
            list.append(str(head.data))
            head = head.next
        print('奇偶链表', list)

    # 判断链表是否是回文链表 1-2-2-1 是
    # 整体思路 找到中间节点 ---快慢指针
    # 将后半分部分链表反转
    # 比较链表值
    # 还原链表
    def isPalindrome(self):
        head = self.__head
        if not head or not head.next:
            return True
        # 找到链表前半部分的尾节点  慢的走一步 快的走两步 当快的走完 慢的正好走到一半
        pre, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 反转后半部分链表
        prev = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # 比较
        # 这里必须记录第二段头结点
        secondhead = prev
        result = True
        while secondhead:
            if head.data != secondhead.data:
                result = False
            head = head.next
            secondhead = secondhead.next
        # 恢复原表
        pre = None
        nex = prev
        while nex:
            temp = nex.next
            nex.next = pre
            pre = nex
            nex = temp
        print('判断是回文链表后 恢复的链表', result,self.look(self.__head))


if __name__ == '__main__':
    sl = SingleLinkList()
    print('true=', sl.is_empty())  # ture
    print('0=', sl.length())  # 0
    sl.insert_val(12)
    print('1=', sl.length())  # 1
    print('12=', sl)  # 12
    sl.insert_val(15)
    sl.insert_val(13)
    print('12->13->15=', sl)  # 12->13->15
    print('false=', sl.is_empty())  # false
    print('3=', sl.length())  # 3
    sl.travel()  # 12 13 15
    print(sl.index_variables(1))  # 13
    sl.append(11)
    print('12->13->15->11=', sl)  # 12->13->15->11
    sl.head_insert(17)
    print('17->12->13->15->11=', sl)  # 17->12->13->15->11
    sl.index_insert(1, 12)
    print('17->12->12->13->15->11=', sl)  # 17->12->12->13->15->11
    sl.index_delete(2)
    print('17->12->13->15->11=', sl)  # 17->12->13->15->11
    sl.delete_val(15)
    print('17->12->13->11=', sl)  # 17->12->13->11
    sl.ddescN(3)
    print('删除倒数第3位节点', sl)
    sl.insert_val(54)
    print('新增节点', sl)
    sl.ddNFS(4)
    print('删除倒数第4位', sl)

    sl.oddEvenList()  # 奇偶链表

    sl.append(11)
    sl.append(54)
    sl.append(13)
    print('回文链表，', sl)
    #非回文 用于测试 done
    # sl.append(12)
    sl.isPalindrome()

    new = sl.reversalLinkList()
    print('反转后的链表', sl.look(new))

    sl.clear_list()
    print('链表=', sl)  # 空

    sl.createCycleLinkList()
    print(sl.isCycle())
    print(sl.detectCycleHash())
    print(sl.detectCycle())
    # list = ['1', '4', '6', '0']
    # print('->'.join(list))
