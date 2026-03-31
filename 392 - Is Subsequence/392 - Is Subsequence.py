class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        prevIndex = -1
        for i in range(len(s)):
            found = False
            for j in range(len(t)):
                if s[i] == t[j] and j > prevIndex:
                    found = True
                    prevIndex = j
                    break
            if not found:
                return False
        return True 
    
if __name__ == "__main__":
    s = "abc"
    t = "akmfbfcd"
    c = Solution()
    print("RESULT: ", c.isSubsequence(s,t))
    