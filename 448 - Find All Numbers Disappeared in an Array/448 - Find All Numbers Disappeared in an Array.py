class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = list()
        for index, val in enumerate(nums):
            searchIndex = abs(val) - 1
            if nums[searchIndex] > 0:
                nums[searchIndex] = -nums[searchIndex]
        for index, val in enumerate(nums):
            if val > 0:
                l.append(index+1)

        return l
        
        