# 189. 轮转数组
# 中等
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
def rotate(nums, k):
    n = len(nums)
    k = k % n  # 处理 k 大于数组长度的情况
    new_nums = [0] * n  # 创建一个新的数组

    for i in range(n):
        new_nums[(i + k) % n] = nums[i]  # 将每个元素放到新位置

    for i in range(n):
        nums[i] = new_nums[i]  # 将新数组的内容复制回原数组
    return nums
    
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))