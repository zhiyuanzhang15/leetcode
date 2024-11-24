# 55. 跳跃游戏
# 中等
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

def canJump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True
    return False

# 示例使用
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # 输出: True

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  # 输出: False