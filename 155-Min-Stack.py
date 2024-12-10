class Pair:
    def __init__(self, first, second):
        self.first=first;
        self.second=second;


class MinStack(object):

    def __init__(self):
        self.st=[];
        
    def push(self, val):
        if len(self.st)==0:
            self.st.append(Pair(val, val))
        else:
            self.st.append(Pair(val, min(val,self.st[-1].second)));     

    def pop(self):
        \\\
        :rtype: None
        \\\
        if self.st:
            self.st.pop()
        
    def top(self):
        \\\
        :rtype: int
        \\\
        if self.st:
            return self.st[-1].first
        
    def getMin(self):
        \\\
        :rtype: int
        \\\
        if self.st:
            return self.st[-1].second
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()