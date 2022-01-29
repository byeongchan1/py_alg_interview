# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

# Design your implementation of the circular queue. 
# The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
# and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
# In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
# But using the circular queue, we can use the space to store new values.

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] == None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
    
    # 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] == None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True        

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]        

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] == None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] != None

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()