# 1043. 分隔数组以得到最大和
# 中等
# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。
# 分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 返回将数组分隔变换后能够得到的元素最大和。
# 本题所用到的测试用例会确保答案是一个 32 位整数。

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * ( n + 1)

    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
    return dp[n]

# 示例使用
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(maxSumAfterPartitioning(arr, k))  # 输出: 84

arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k = 4
print(maxSumAfterPartitioning(arr, k))  # 输出: 83
