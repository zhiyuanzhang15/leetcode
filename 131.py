# 131. 分割回文串
# 中等
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 
# 回文串。
# 返回 s 所有可能的分割方案。

def partition(s):
    def isPalindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if isPalindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()
    result = []
    backtrack(0, [])
    return result
s = "aab"
print(partition(s))