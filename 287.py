# 287. 寻找重复数
# 中等
# 给定一个包含 n + 1 个整数的数组 nums ，
# 其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

def findDuplicate(nums):
    # 初始化快慢指针
    slow = nums[0]
    fast = nums[0]

    # 寻找相遇点
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # 找到环的入口
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# 示例使用
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # 输出: 2