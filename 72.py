# 72. 编辑距离
# 中等
# 给你两个单词 word1 和 word2， 
# 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m][n]

# 示例使用
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # 输出: 3