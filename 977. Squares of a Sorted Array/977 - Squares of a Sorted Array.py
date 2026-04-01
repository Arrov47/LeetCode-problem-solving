class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lp, rp = 0, len(nums)-1
        res = []
        while lp <= rp:
            leftNum = nums[lp]**2
            rightNum = nums[rp]**2
            if leftNum > rightNum:
                res.append(leftNum)
                lp+=1
            else:
                res.append(rightNum)
                rp-=1
        return res[::-1]