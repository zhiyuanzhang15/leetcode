# 19. 删除链表的倒数第 N 个结点
# 中等
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    def getlength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    length = getlength(head)
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    for i in range(1, length - n + 1):
        curr = curr.next
    curr.next = curr.next.next
    return dummy.next

# 示例使用
# 创建链表: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 删除倒数第 2 个结点
new_head = removeNthFromEnd(head, 2)

# 打印新的链表: 1 -> 2 -> 3 -> 5
while new_head:
    print(new_head.val, end=" -> " if new_head.next else "\n")
    new_head = new_head.next