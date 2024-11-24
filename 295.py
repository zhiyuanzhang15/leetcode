# 295. 数据流的中位数
# 困难
# 中位数是有序整数列表中的中间值。
# 如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。
# 与实际答案相差 10-5 以内的答案将被接受。

import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # 最大堆
        self.right = []  # 最小堆

    def addNum(self, num: int) -> None:
        # 将新元素加入最大堆
        heapq.heappush(self.left, -num)
        # 将最大堆的堆顶元素加入最小堆
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # 如果最小堆的大小超过最大堆，将最小堆的堆顶元素加入最大堆
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2

# 示例使用
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # 输出: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # 输出: 2