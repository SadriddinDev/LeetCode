from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashtable = defaultdict(int)
        for c in magazine:
            hashtable[c] += 1
        for c in ransomNote:
            if hashtable[c] > 0:
                hashtable[c] -= 1
            else:
                return False
        return True
