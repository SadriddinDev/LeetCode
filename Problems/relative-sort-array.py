class Solution:
    def relativeSortArray(self, arr1, arr2):
        mdict = {}
        for i in arr1:
            if mdict.get(i):
                mdict[i].append(i)
            else:
                mdict[i] = [i]
        result = []
        for i in arr2:
            result += mdict[i]
        other_elements = []
        for i in arr1:
            if i not in arr2:
                other_elements.append(i)
        other_elements.sort()
        result += other_elements
        return result
