# 213. 打家劫舍 II
# 中等
# 你是一个专业的小偷，计划偷窃沿街的房屋，
# 每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
# 这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

def rob(nums):
    def rob_linear(nums):
        prev, curr = 0, 0

        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr
    
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# 示例使用
nums = [2, 3, 2]
print(rob(nums))  # 输出: 3

nums = [1, 2, 3, 1]
print(rob(nums))  # 输出: 4