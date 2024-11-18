# 105. 从前序与中序遍历序列构造二叉树
# 中等
# 给定两个整数数组 preorder 和 inorder ，
# 其中 preorder 是二叉树的先序遍历， 
# inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

# 示例使用
def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
print_inorder(root)  # 输出: 9 3 15 20 7