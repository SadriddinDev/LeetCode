class Solution:
    def longestCommonPrefix(self, strs) -> str:
        word = strs[0]
        text = ''
        for i in word:
            temp  = text + i
            if not all([j.startswith(temp) for j in strs]):
                break
            text = temp
        return text