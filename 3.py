# 3. 无重复字符的最长子串

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 
# 子串的长度。

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        print(char_set)
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
if __name__ == "__main__":
    s = "abcabcbb"
    result = length_of_longest_substring(s)
    print(f"字符串 '{s}' 中不含重复字符的最长子串的长度是: {result}")