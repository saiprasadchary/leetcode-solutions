class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7
        
        # Arrays to store previous and next less
        ple = [-1] * n
        nle = [n] * n
        
        # Monotonic stack
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                nle[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                ple[stack.pop()] = i
            stack.append(i)
        
        # Calculate the sum using contributions
        result = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            result = (result + arr[i] * left * right) % mod
        
        return result