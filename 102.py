# 102. 二叉树的层序遍历
# 中等
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 
# （即逐层地，从左到右访问所有节点）。

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
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

root = create_binary_tree([3, 9, 20, None, None, 15, 7])
print(levelOrder(root))  # 输出: [[3], [9, 20], [15, 7]]