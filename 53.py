# 53. 最大子数组和
# 中等
# 给你一个整数数组 nums ，
# 请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组
# 是数组中的一个连续部分。

def maxSubArray(nums):
    current_sum = -float("inf")
    max_sum = -float("inf")
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums)) 