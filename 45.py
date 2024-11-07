# 45. 跳跃游戏 II
# 中等
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，
# 如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


# 示例使用
nums = [2, 3, 1, 1, 4]
print(jump(nums))  # 输出: 2

nums = [2, 3, 0, 1, 4]
print(jump(nums))  # 输出: 2