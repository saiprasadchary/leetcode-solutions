from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()  # Instantiate a deque object

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        s = len(self.queue)  # Get the current size of the deque
        self.queue.append(x)  # Append the element to the deque
        # Rotate the deque to make the last element the front of the queue
        for _ in range(s):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()  # Pop from the front to simulate stack behavior

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]  # Return the front item of the deque, simulating the stack's top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0  # Check if the deque is empty

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()