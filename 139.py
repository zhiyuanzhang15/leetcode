# 139. 单词拆分
# 中等
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
# 如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

# 示例使用
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # 输出: True

s = "applepenapple"
wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))  # 输出: True

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))  # 输出: False