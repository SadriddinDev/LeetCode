class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_table = {}
        hash_table2 = {}
        words = s.split()
        for i in range(len(pattern)):
            if hash_table.get(pattern[i]) is None:
                if hash_table2.get(words[i]) is None:
                    hash_table[pattern[i]] = words[i]
                    hash_table2[words[i]] = pattern[i]
                else:
                    return False
            else:
                if hash_table.get(pattern[i]) == words[i] and hash_table2[words[i]] == pattern[i]:
                    pass
                else:
                    return False
        return True
                    