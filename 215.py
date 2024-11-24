# 215. 数组中的第K个最大元素
# 中等
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

import random
def partition(nums, left, right):
    pivot_index = random.randint(left,right)
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1
    nums[store_index], nums[right] = nums[right], nums[store_index]
    return store_index

def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]
    pivot_index = partition(nums, left, right)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)
def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k)

# 示例使用
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出: 5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))  # 输出: 4