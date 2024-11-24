# 5. 最长回文子串
# 中等
# 给你一个字符串 s，找到 s 中最长的 
# 回文子串。

def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True
    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j - i + 1 > max_len:
                start = i
                max_len = j - i + 1
    return s[start:start + max_len]

# 示例使用
s = "babad"
print(longestPalindrome(s))  # 输出: "bab" 或 "aba"

s = "cbbd"
print(longestPalindrome(s))  # 输出: "bb"