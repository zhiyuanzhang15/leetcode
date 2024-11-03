# 209. 长度最小的子数组
# 中等
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 
# 子数组[numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。

def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length,right - left + 1)
            current_sum -= nums[left]
            left += 1
    if min_length == float('inf'):
        min_length = 0
    return min_length

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
