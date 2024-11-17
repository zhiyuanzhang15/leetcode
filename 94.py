# 94. 二叉树的中序遍历
# 简单
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    result = []
    inorder(root)
    return result

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

root = create_binary_tree([1,None,2,3])
print(inorderTraversal(root))  # 输出: [1, 3, 2]