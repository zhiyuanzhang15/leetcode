# 56. 合并区间
# 中等
# 以数组 intervals 表示若干个区间的集合，
# 其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，
# 该数组需恰好覆盖输入中的所有区间 。
def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x:x[0])
    res = []
    for interval in intervals:
        if not res or interval[0] > res[-1][1]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))