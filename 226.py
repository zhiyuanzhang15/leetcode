# 226. 翻转二叉树
# 简单
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    from collections import deque
    if not root:
        return None
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root



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

def print_binary_tree(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print()

root = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
print("Original tree:")
print_binary_tree(root)
root = invertTree(root)
print("Inverted tree:")
print_binary_tree(root)