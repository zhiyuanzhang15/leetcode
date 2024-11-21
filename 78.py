# 78. 子集
# 中等
# 给你一个整数数组 nums ，数组中的元素 互不相同 。
# 返回该数组所有可能的子（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

def subsets(nums):
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    result = []
    backtrack(0, [])
    return result

nums = [1, 2, 3]
print(subsets(nums))