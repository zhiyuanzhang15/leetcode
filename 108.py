# 108. 将有序数组转换为二叉搜索树
# 简单
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 
# 平衡
#  二叉搜索树。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    def buildBST(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = buildBST(left, mid - 1)
        node.right = buildBST(mid + 1, right)
        return node
    return buildBST(0, len(nums) - 1)

# 示例使用
def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
print_inorder(root)  # 输出: -10 -3 0 5 9