# 160. 相交链表
# 简单
# 给你两个单链表的头节点 headA 和 headB ，
# 请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA

# 示例使用
# 创建链表节点
# 链表A: 4 -> 1 -> 8 -> 4 -> 5
# 链表B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
headA = ListNode(4)
headA.next = ListNode(1)
intersection = ListNode(8)
headA.next.next = intersection
intersection.next = ListNode(4)
intersection.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersection

# 找到相交节点
result = getIntersectionNode(headA, headB)
print(result.val if result else "null")  # 输出: 8