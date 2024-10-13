class Solution(object):
    def __init__(self):
        self.mem={0:0,1:1}
    def fib(self, n):
        # if(n==1):
        #     return 1
        # if(n==0):
        #     return 0
        # return self.fib(n-1)+self.fib(n-2)
        #Next solve it using memoization
        if n not in self.mem:
            self.mem[n]=self.fib(n-1)+self.fib(n-2);
        return self.mem[n]
