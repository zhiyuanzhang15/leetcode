# 41. 缺失的第一个正数
# 困难
# 给你一个未排序的整数数组 nums ，
# 请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

def firstMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1

nums = [3, 4, 2, 1, 0]
print(firstMissingPositive(nums)) 