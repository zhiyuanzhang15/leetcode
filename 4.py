# 4. 寻找两个正序数组的中位数
# 困难
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    if len(nums) % 2 == 0:
        return (float(nums[len(nums) // 2] + nums[(len(nums) // 2) - 1])) / 2.0
    else:
        return nums[len(nums) // 2]
    
nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1,nums2))