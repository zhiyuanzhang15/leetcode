# 438. 找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 
# 异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

from collections import Counter

def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter()

    p_length = len(p)
    s_length = len(s)

    for i in range(s_length):
        # 增加当前字符到窗口计数器
        s_count[s[i]] += 1

        # 确保窗口大小不超过 p 的长度
        if i >= p_length:
            if s_count[s[i - p_length]] == 1:
                del s_count[s[i - p_length]]
            else:
                s_count[s[i - p_length]] -= 1

        # 比较窗口计数器和 p 的计数器
        if s_count == p_count:
            result.append(i - p_length + 1)

    return result

s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))  # 输出 [0, 6]
    