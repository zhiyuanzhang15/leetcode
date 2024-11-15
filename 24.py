# 24. 两两交换链表中的节点
# 中等
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        first.next = second.next
        second.next = first
        current.next = second

        current = first
    return dummy.next

# 示例使用
# 创建链表: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# 两两交换节点
new_head = swapPairs(head)

# 打印新的链表: 2 -> 1 -> 4 -> 3
while new_head:
    print(new_head.val, end=" -> " if new_head.next else "\n")
    new_head = new_head.next