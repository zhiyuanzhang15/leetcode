# 76. 最小覆盖子串
# 困难
# 给你一个字符串 s 、一个字符串 t 。
# 返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    window_count = Counter()

    required = len(t_count)
    formed = 0

    left, right = 0, 0
    min_length = float("inf")
    min_window = (0, 0)

    while right < len(s):
        char = s[right]
        window_count[char] += 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = (left, right)
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            left += 1
        right += 1
    left, right = min_window
    return s[left:right + 1] if min_length != float("inf") else ""

# 示例使用
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # 输出: "BANC"