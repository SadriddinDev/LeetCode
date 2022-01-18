class MyCircularQueue:

    def __init__(self, k: int):
        self.nums = [None for _ in range(k)]
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.nums[self.size] = value
            self.size += 1
            return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.size -= 1
            self.nums.pop(0)
            self.nums.append(None)
            return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.nums[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.nums[self.size-1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()