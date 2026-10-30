class MyStack:

    def __init__(self):
            self.queue_pop = deque()
            self.queue_push = deque()

    def push(self, x: int) -> None:
        self.queue_push.append(x)

        while self.queue_pop:
            self.queue_push.append(self.queue_pop.popleft())

        self.queue_pop, self.queue_push = self.queue_push, self.queue_pop


    def pop(self) -> int:
        if self.empty():
            return -1

        return self.queue_pop.popleft()


    def top(self) -> int:
        if self.empty():
            return -1

        return self.queue_pop[0]

        
    def empty(self) -> bool:
        return not self.queue_pop



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()