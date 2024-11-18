# 437. 路径总和 III
# 中等
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，
# 求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，
# 但是路径方向必须是向下的（只能从父节点到子节点）。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, currentSum):
        nonlocal count
        if not node:
            return
        
        currentSum += node.val

        if currentSum - targetSum in prefixSums:
            count += prefixSums[currentSum - targetSum]
        prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1
        dfs(node.left, currentSum)
        dfs(node.right, currentSum)
        prefixSums[currentSum] -= 1
    count = 0
    prefixSums = {0:1}
    dfs(root, 0)
    return count

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

root = create_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
targetSum = 8
print(pathSum(root, targetSum))  # 输出: 3