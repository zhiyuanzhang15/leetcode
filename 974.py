# 974. 和可被 K 整除的子数组
# 中等
# 给定一个整数数组 nums 和一个整数 k ，
# 返回其中元素之和可被 k 整除的非空 子数组 的数目。
# 子数组 是数组中 连续 的部分。

def subarraysDivByK(nums, k):
    prefix_sums = {0:1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        mod = current_sum % k
        if mod < 0:
            mod += k
        if mod in prefix_sums:
            count += prefix_sums[mod]
        else:
            prefix_sums[mod] = 0
        prefix_sums[mod] += 1
    return count

# 示例使用
nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarraysDivByK(nums, k))  # 输出: 7