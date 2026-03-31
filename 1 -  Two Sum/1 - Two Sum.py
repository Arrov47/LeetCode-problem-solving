class Solution(object):
    def twoSum(self, nums, target):
        d =  dict()
        for index, num in enumerate(nums):
            left = target - num
            if left in d and d[left] != index:
                return [d[left], index]
            d[num] = index
        