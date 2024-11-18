# 114. 二叉树展开为链表
# 中等
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
# 展开后的单链表应该同样使用 TreeNode ，
# 其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if stack:
            node.right = stack[-1]
        node.left = None
# 修正后的创建二叉树函数
def create_binary_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
    return nodes[0]

def print_linked_list(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

# 示例使用
root = create_binary_tree([1, 2, 5, 3, 4, None, 6])
flatten(root)
print_linked_list(root)  # 输出: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None