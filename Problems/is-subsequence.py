class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            bor = False
            while j < len(t):
                if t[j] == s[i]:
                    bor = True
                    j += 1
                    break
                j += 1
            if not bor:
                return False
            i += 1
        return True
