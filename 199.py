# 199. 二叉树的右视图
# 中等
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，
# 按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

# 示例使用
def create_binary_tree(data_list):
    if not data_list:
        return None
 
    root_data = data_list.pop(0)
    root_node = Node(root_data)
 
    queue = [root_node]
    while data_list and queue:
        node = queue.pop(0)
        node_data = data_list.pop(0)
        if node_data is not None:
            node.left = Node(node_data)
            queue.append(node.left)
 
        if data_list and data_list[0] is not None:
            node_data = data_list.pop(0)
            node.right = Node(node_data)
            queue.append(node.right)
 
    return root_node

root = create_binary_tree([1, 2, 3, None, 5, None, 4,6,7,8,9,8,8,8])
print(root)
print(rightSideView(root))  # 输出: [1, 3, 4]