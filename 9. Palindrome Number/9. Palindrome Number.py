class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        return temp == temp[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))