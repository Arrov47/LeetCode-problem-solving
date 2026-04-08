class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(5554455))