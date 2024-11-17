# 543. 二叉树的直径
# 简单
# 给你一棵二叉树的根节点，返回该树的 直径 。
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。
# 这条路径可能经过也可能不经过根节点 root 。
# 两节点之间路径的 长度 由它们之间边数表示。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1
    diameter = 0
    depth(root)
    return diameter

# 示例使用
def create_binary_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

root = create_binary_tree([1, 2, 3, 4, 5])
print(diameterOfBinaryTree(root))  # 输出: 3