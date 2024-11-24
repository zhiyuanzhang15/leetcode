# 32. 最长有效括号
# 困难
# 给你一个只包含 '(' 和 ')' 的字符串，
# 找出最长有效（格式正确且连续）括号
# 子串的长度。

def longestValidParentheses(s):
    if not s:
        return 0

    dp = [0] * len(s)
    max_len = 0

    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
            max_len = max(max_len, dp[i])

    return max_len

# 示例使用
s = "(()"
print(longestValidParentheses(s))  # 输出: 2

s = ")()())"
print(longestValidParentheses(s))  # 输出: 4