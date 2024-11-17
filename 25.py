# 25. K 个一组翻转链表
# 困难
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    #curr = head

    while True:
        tail = prev
        for _ in range(k):
            tail = tail.next
            if not tail:
                return dummy.next
        next_group = tail.next
        start = prev.next
        tail.next = None
        prev.next = reverse(start, tail.next)
        start.next = next_group
        prev = start
        #curr = next_group

# 示例使用
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = create_linked_list([1, 2, 3, 4, 5])
head = reverseKGroup(head, 3)
print_linked_list(head)  # 输出: 3 -> 2 -> 1 -> 4 -> 5 -> None