class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        res = 0
        for num in nums:
            if counter == 0:
                res = num
            counter += (1 if num == res else -1)
        return res