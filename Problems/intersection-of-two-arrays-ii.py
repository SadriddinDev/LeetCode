class Solution:
    def intersect(self, nums1, nums2):
        mydict = {}
        for i in nums2:
            if mydict.get(i):
                mydict[i]+=1
            else:
                mydict[i] = 1
        answer = []
        for i in nums1:
            if mydict.get(i):
                if mydict.get(i) >=1:
                    answer.append(i)
                    mydict[i]-=1
        return answer