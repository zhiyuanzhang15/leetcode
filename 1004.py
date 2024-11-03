# 1004. 最大连续1的个数 III
# 中等
# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

def longestOnes(nums, k):
    left = 0
    max_ones = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        max_ones = max(max_ones,right - left + 1)
    return max_ones

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))