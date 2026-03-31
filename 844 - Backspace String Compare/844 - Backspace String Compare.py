class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = 0
        l1 = list()
        i = len(s)-1
        while i >=0:
            if counter == 0 and s[i] != "#":
                l1.append(s[i])
            elif s[i] == "#":
                counter+=1
            elif s[i] != "#":
                counter-=1
            i-=1
        s = "".join(l1[::-1])

        
        counter = 0
        l1 = list()
        i = len(t)-1
        while i >=0:
            if counter == 0 and t[i] != "#":
                l1.append(t[i])
            elif t[i] == "#":
                counter+=1
            elif t[i] != "#":
                counter-=1
            i-=1
        t = "".join(l1[::-1])

        return s == t





            
            