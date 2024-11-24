# 169. 多数元素
# 简单
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。
# 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

# 示例使用
nums = [3, 2, 3]
print(majorityElement(nums))  # 输出: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # 输出: 2