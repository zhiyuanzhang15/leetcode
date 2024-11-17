# 148. 排序链表
# 中等
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next

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

head = create_linked_list([4, 2, 1, 3])
head = sortList(head)
print_linked_list(head)  # 输出: 1 -> 2 -> 3 -> 4 -> None