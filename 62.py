# 62. 不同路径
# 中等
# 一个机器人位于一个 m x n 网格的左上角 
# （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。
# 机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？

def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# 示例使用
m = 3
n = 7
print(uniquePaths(m, n))  # 输出: 28

m = 3
n = 2
print(uniquePaths(m, n))  # 输出: 3