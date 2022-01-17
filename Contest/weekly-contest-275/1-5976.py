class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        for i in range(n):
            nums = [False for _ in range(n)]
            for j in range(n):
                son = matrix[i][j]-1
                if son<n:
                    nums[son] = True
            if not all(nums):
                return False
        for i in range(n):
            nums = [False for _ in range(n)]
            for j in range(n):
                son = matrix[j][i]-1
                if son<n:
                    nums[son] = True
            if not all(nums):
                return False
        return True

    def wordCount(self, startWords, targetWords):
        startWords.sort(key=len)
        targetWords.sort(key=len)

        answer = 0
        word_leng_hash = {
        }
        for i, word in enumerate(startWords):
            n = len(word)+1
            if word_leng_hash.get(n) is None:
                word_leng_hash[n] = {
                    "start":i,
                    "finish":i
                }
            else:
                word_leng_hash[n]["finish"] = i
        for word in targetWords:
            get_hash = word_leng_hash.get(len(word))
            if get_hash is not None:

                for i in range(get_hash["start"], get_hash['finish']+1):
                    sword = startWords[i]
                    match_letter = 0
                    
                    for l in word:
                        if l in sword:
                            match_letter+=1
                    if match_letter == len(word)-1:
                        answer += 1
                        break
        return answer

class Solution:
    def removeDuplicates(self, nums) -> int:
        last = -200
        last_index = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] > last:
                nums[i], nums[last_index] = nums[last_index], nums[i]
                k+=1
                last_index+=1
            last = nums[i]
        return k

# print(Solution().wordCount( ["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"], ["r","am","jg","umhjo","fov","lujy","b","uz","y"]))
       
