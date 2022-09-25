class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None for x in range(k)]
        self.front = self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False 
        self.queue[self.rear % self.size] = value
        self.rear += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False 
        self.front += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.front % self.size]
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[(self.rear-1)%self.size]
 
    def isEmpty(self) -> bool:
         return self.front == self.rear
        

    def isFull(self) -> bool:
        return self.rear == self.front+self.size
            



