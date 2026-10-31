class MyQueue:

    def __init__(self):
        self.list_push = []
        self.list_pop = []
        

    def push(self, x: int) -> None:
        self.list_push.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        
        self.move()
        return self.list_pop.pop()

    def peek(self) -> int:
        if self.empty():
            return -1

        self.move()
        return self.list_pop[-1]

    def empty(self) -> bool:
        return not self.list_push and not self.list_pop

    def move(self) -> None:
        if not self.list_pop:
            while self.list_push:
                self.list_pop.append(self.list_push.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()