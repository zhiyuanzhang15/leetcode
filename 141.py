# 141. 环形链表
# 简单
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，
# 则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 
# 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# 示例使用
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head

head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
print(hasCycle(head))  # 输出: True