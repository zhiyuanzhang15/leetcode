# 347. 前 K 个高频元素
# 中等
# 给你一个整数数组 nums 和一个整数 k ，
# 请你返回其中出现频率前 k 高的元素。
# 你可以按 任意顺序 返回答案。

import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq,num in heap]

# 示例使用
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # 输出: [1, 2]

nums = [1]
k = 1
print(topKFrequent(nums, k))  # 输出: [1]