#49. 字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
def group_anagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        print(sorted_str)   
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)
    print(anagrams)
    return list(anagrams.values())

# 示例用法
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # 输出: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]