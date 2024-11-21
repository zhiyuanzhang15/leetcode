# 35. 搜索插入位置
# 简单
# 给定一个排序数组和一个目标值，在数组中找到目标值，
# 并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 示例使用
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # 输出: 2

target = 2
print(searchInsert(nums, target))  # 输出: 1

target = 7
print(searchInsert(nums, target))  # 输出: 4

target = 0
print(searchInsert(nums, target))  # 输出: 0