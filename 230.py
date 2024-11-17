# 230. 二叉搜索树中第 K 小的元素
# 中等
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，
# 请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

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

root = create_binary_tree([3, 1, 4, None, 2])
print(kthSmallest(root, 1))  # 输出: 1