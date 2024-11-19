# 124. 二叉树中的最大路径和
# 困难
# 二叉树中的 路径 被定义为一条节点序列，
# 序列中每对相邻节点之间都存在一条边。
# 同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        current_max_path = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_max_path)
        return node.val + max(left_gain, right_gain)
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

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

root = create_binary_tree([-10, 9, 20, None, None, 15, 7])
print(maxPathSum(root))  # 输出: 42