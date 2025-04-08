class Solution(object):
    
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        tails = {}
        
        # Build the frequency dictionary.
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Process numbers in order.
        for num in nums:
            if freq[num] == 0:
                continue
            # If there is a subsequence ending with num-1, extend it.
            if tails.get(num - 1, 0) > 0:
                tails[num - 1] -= 1
                tails[num] = tails.get(num, 0) + 1
                freq[num] -= 1
            # Otherwise, try to start a new subsequence num, num+1, num+2.
            elif freq.get(num + 1, 0) > 0 and freq.get(num + 2, 0) > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                tails[num + 2] = tails.get(num + 2, 0) + 1
            else:
                # Cannot form a valid subsequence with num.
                return False
        
        return True