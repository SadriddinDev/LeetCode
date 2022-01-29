class Solution:
    def sequentialDigits(self, low: int, high: int):
        def generate_n_seq(n):
            son = 0
            for i in range(1, n + 1):
                son = son * 10 + i
            return son
        def generate_1_seq(n):
            son = 0
            for i in range(1, n + 1):
                son = son * 10 + 1
            return son
        answer = []
        for i in range(2, 10):
            son = generate_n_seq(i)
            bir = generate_1_seq(i)
            for j in range(10 - i):
                if (son + bir * j) >= low and (son + bir * j) <= high:
                    answer.append(son+bir*j)
        return answer

        