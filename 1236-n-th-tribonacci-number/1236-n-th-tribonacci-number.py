class Solution(object):

    def __init__(self):
        self.mem={0:0,1:1,2:1};    

    def tribonacci(self, n):
     
        if n not in self.mem:
            self.mem[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3);
        return self.mem[n]