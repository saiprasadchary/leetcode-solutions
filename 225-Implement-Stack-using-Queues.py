from collections import deque

class MyStack(object):
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Move all elements to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # Push element into queue1
        self.queue1.append(x)
        # Move all elements back to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self):
        # Pop from queue1 which is arranged to behave like a stack
        return self.queue1.popleft()

    def top(self):
        # Peek the front element of queue1
        return self.queue1[0]

    def empty(self):
        # Check if queue1 is empty
        return not self.queue1

# Example usage
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top())    # Output: 2
# print(obj.pop())    # Output: 2
# print(obj.empty())  # Output: False