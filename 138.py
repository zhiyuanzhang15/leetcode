# 138. 随机链表的复制
# 中等
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，
# 该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，
# 其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针
# 也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。
# 复制链表中的指针都不应指向原链表中的节点 。
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。
# 那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
# 返回复制链表的头节点。
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。
# 每个节点用一个 [val, random_index] 表示：
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，
# 则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next
    
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    current = head
    new_head = head.next
    while current:
        new_node = current.next
        current.next = new_node.next
        if new_node.next:
            new_node.next = new_node.next.next
        current = current.next
    return new_head

# 示例使用
def print_linked_list(head):
    current = head
    while current:
        random_val = current.random.val if current.random else "None"
        print(f"Node(val: {current.val}, random: {random_val})")
        current = current.next

# 创建示例链表
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

# 复制链表
new_head = copyRandomList(node1)
print_linked_list(new_head)