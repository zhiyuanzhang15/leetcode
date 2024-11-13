# 206. 反转链表
# 简单
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reversed_head = reverseList(head)

while reversed_head:
    print(reversed_head.val, end="->" if reversed_head.next else "\n")
    reversed_head = reversed_head.next