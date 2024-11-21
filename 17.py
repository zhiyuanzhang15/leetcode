# 17. 电话号码的字母组合
# 中等
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

def letterCombinations(digits):
    if not digits:
        return []

    # 数字到字母的映射
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    def backtrack(index, path):
        # 如果路径长度等于输入的数字长度，加入结果集
        if index == len(digits):
            combinations.append("".join(path))
            return
        # 获取当前数字对应的所有可能的字母
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

# 示例使用
digits = "23"
print(letterCombinations(digits))  # 输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]