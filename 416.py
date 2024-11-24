# 416. 分割等和子集
# 中等
# 给你一个 只包含正整数 的 非空 数组 nums 。
# 请你判断是否可以将这个数组分割成两个子集，
# 使得两个子集的元素和相等。

def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j -num]
    return dp[target]

# 示例使用
nums = [1, 5, 11, 5]
print(canPartition(nums))  # 输出: True

nums = [1, 2, 3, 5]
print(canPartition(nums))  # 输出: False