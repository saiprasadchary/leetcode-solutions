class Solution:
    def isPossibleDivide(self, nums, k):
        n = len(nums)
        # Check if n is divisible by k
        if n % k != 0:
            return False
        
        # Sort the array to consider consecutive sequences
        nums.sort()
        
        # Use a frequency dictionary to track counts
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # For every number, try to form groups of k consecutive numbers
        for num in nums:
            if freq[num] > 0:
                count = freq[num]
                for j in range(num, num + k):
                    if freq.get(j, 0) < count:
                        return False
                    freq[j] -= count
        
        return True