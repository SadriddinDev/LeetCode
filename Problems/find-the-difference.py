class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashtable = {}
        for i in s:
            if hashtable.get(i):
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        for i in t:
            if hashtable.get(i):
                if hashtable[i] > 0:
                    hashtable[i] -= 1
                else:
                    return i
            else:
                return i

        