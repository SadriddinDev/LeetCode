class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n > 0:
            if n %2 == 1:
                bit_count +=1
            n //=2
        return bit_count