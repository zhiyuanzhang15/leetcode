# 21. 合并两个有序链表
# 简单
# 将两个升序链表合并为一个新的 升序 链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next

# 示例使用
# 创建链表 l1: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# 创建链表 l2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 合并链表
merged_head = mergeTwoLists(l1, l2)

# 打印合并后的链表: 1 -> 1 -> 2 -> 3 -> 4 -> 4
while merged_head:
    print(merged_head.val, end=" -> " if merged_head.next else "\n")
    merged_head = merged_head.next