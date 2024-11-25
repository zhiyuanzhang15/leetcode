# 75. 颜色分类
# 中等
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
# 原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。

def sortColors(nums):
    p0, curr = 0, 0
    p2 = len(nums) - 1
    while curr <= p2:
        if nums[curr] == 0:
            nums[curr],nums[p0] = nums[p0], nums[curr]
            curr += 1
            p0 += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1

# 示例使用
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # 输出: [0, 0, 1, 1, 2, 2]