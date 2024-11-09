# 560. 和为 K 的子数组
# 中等
# 给你一个整数数组 nums 和一个整数 k ，
# 请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。

def subarraySum(nums, k):
    prefix_sums = {0:1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1
    return count

# 示例使用
nums = [1, 2, 1, -1, 0]
k = 2
print(subarraySum(nums, k))  # 输出: 2

nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # 输出: 2