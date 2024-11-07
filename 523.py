# 523. 连续的子数组和
# 中等
# 给你一个整数数组 nums 和一个整数 k ，如果 nums 有一个 好的子数组 返回 true ，否则返回 false：
# 一个 好的子数组 是：
# 长度 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 注意：
# 子数组 是数组中 连续 的部分。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终 视为 k 的一个倍数。

def checkSubarraySum(nums, k):
    prefix_sums = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        mod = current_sum % k if k != 0 else current_sum
        if mod in prefix_sums:
            if i - prefix_sums[mod] > 1:
                return True
        else:
            prefix_sums[mod] = i

    return False

# 示例使用
nums = [23, 2, 4, 6, 7]
k = 6
print(checkSubarraySum(nums, k))  # 输出: True

nums = [5, 0, 0, 0]
k = 3
print(checkSubarraySum(nums, k))  # 输出: True

nums = [23, 2, 6, 4, 7]
k = 13
print(checkSubarraySum(nums, k))  # 输出: False