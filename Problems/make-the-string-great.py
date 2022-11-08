class Solution:
    def makeGood(self, s: str) -> str:
        def isSame(c1, c2):
            return abs(ord(c1) - ord(c2)) == 32
        s2 = ''
        while s2 != s:
            s2 = ''
            i = 0
            n = len(s) - 1
            while i <= n:
                if i < n and isSame(s[i], s[i+1]):
                    i+=1
                else:
                    s2 += s[i]
                i+=1
            if s != s2:
              s = s2
              s2 = ''
        return s
        
                    
print(Solution().makeGood("abBAcC"))