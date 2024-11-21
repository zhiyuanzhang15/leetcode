# 22. 括号生成
# 中等
# 数字 n 代表生成括号的对数，请你设计一个函数，
# 用于能够生成所有可能的并且 有效的 括号组合。

def generateParenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack("", 0, 0)
    return result

# 示例使用
n = 3
print(generateParenthesis(n))  # 输出: ["((()))", "(()())", "(())()", "()(())", "()()()"]