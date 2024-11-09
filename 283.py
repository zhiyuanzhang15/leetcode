# 283. 移动零
# 简单
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，
# 同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
def moveZeroes(nums):
    left = right = 0
    n = len(nums)
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums
nums = [0,1,0,3,12]
print(moveZeroes(nums))