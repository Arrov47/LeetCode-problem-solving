class Solution(object):
    def containsDuplicate(self, nums):
        d = set()
        for i in nums:
            if i in d:
                return True
            d.add(i)
        return False