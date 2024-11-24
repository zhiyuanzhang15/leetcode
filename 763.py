# 763. 划分字母区间
# 中等
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，
# 同一字母最多出现在一个片段中。
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
# 返回一个表示每个字符串片段的长度的列表。

def partitionLabels(s):
    last_occurrence = {c: i for i, c in enumerate(s)}
    result = []
    start, end = 0, 0
    for i, c in enumerate(s):
        end = max(end, last_occurrence[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result

# 示例使用
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))  # 输出: [9, 7, 8]

s = "eccbbbbdec"
print(partitionLabels(s))  # 输出: [10]