from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = defaultdict(int)
        for i in s: hashtable[i]+=1
        for i, c in enumerate(s):
            if hashtable[c] == 1:
                return i
        return -1