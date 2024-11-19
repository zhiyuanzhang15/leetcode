# 236. 二叉树的最近公共祖先
# 中等
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，
# 最近公共祖先表示为一个节点 x，满足 x 是 p、q 的
# 祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

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

# 创建二叉树
root = create_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = root.left  # 节点 5
q = root.left.right.right  # 节点 4

# 查找最近公共祖先
ancestor = lowestCommonAncestor(root, p, q)
print(ancestor.val)  # 输出: 5