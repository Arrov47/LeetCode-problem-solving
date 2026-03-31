class Solution(object):
    def missingNumber(self, nums):
        total = sum(range(len(nums)+1))
        givenTotal = sum(nums)
        return total - givenTotal