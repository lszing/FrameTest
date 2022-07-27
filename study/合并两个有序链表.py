# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
from typing import Optional


class LinkedNode():
    def __init__(self, var=0, next=None):
        self.var = var
        self.next = next


class solution():
    def mergeTwoLists(self, list1: Optional[LinkedNode], list2: Optional[LinkedNode]):
        preHead = LinkedNode(-1)
        #preHead指向头结点
        prev = preHead
        while list1.var != None and list2.var != None:
            if list1.var <= list2.var:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        prev.next = list2 if list2 is not None else list1
        return preHead.next
