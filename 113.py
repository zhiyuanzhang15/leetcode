# 113. 路径总和 II
# 中等
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，
# 找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, currentPath, currentSum):
        if not node:
            return
        currentPath.append(node.val)
        currentSum += node.val

        if not node.left and not node.right and currentSum == targetSum:
            result.append(list(currentPath))
        
        dfs(node.left, currentPath, currentSum)
        dfs(node.right, currentPath, currentSum)

        currentPath.pop()
    
    result = []
    dfs(root, [], 0)
    return result

# Helper function to build the tree from list
def buildTree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Example usage
nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
root = buildTree(nodes)
print(pathSum(root, targetSum))