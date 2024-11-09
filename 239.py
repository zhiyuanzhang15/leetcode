# 239. 滑动窗口最大值
# 困难
# 给你一个整数数组 nums，有一个大小为 k 的
# 滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。
# 滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
import collections 
def maxSlidingWindow(nums, k):
    if not nums:
        return []
    deque = collections.deque()
    res = []
    for i in range(len(nums)):
        if deque and deque[0] < i - k + 1:
            deque.popleft()
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            res.append(nums[deque[0]])
    return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))