class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = float(0)

        if len(nums) <= k:
            for num in nums:
                total+=num
            return total/len(nums)

        maxAverage = float('-inf')
        j = 0

        while j+k <= len(nums):
            avg = float(0)
            if j == 0:
                for i in range(j, j+k):
                    total += nums[i]
            else:
                total -= nums[j-1]
                total += nums[j+k-1]

            avg = float(total/k)
            
            if avg > maxAverage:
                maxAverage = avg
            j+=1

        return maxAverage

if __name__ == "__main__":
    nums  = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    print("RESULT: {}".format(s.findMaxAverage(nums,k)))
    

