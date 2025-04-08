class Solution(object):
    def isPossible(self, nums):
        # Build frequency dictionary.
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        vacancy = {}  # counts of subsequences waiting for a specific number
        
        for num in nums:
            if freq.get(num, 0) == 0:
                continue

            # If there's a subsequence waiting for num, extend that subsequence:
            if vacancy.get(num, 0) > 0:
                vacancy[num] -= 1
                # When num is added to a subsequence, the subsequence now expects num+1.
                vacancy[num + 1] = vacancy.get(num + 1, 0) + 1
                freq[num] -= 1
            # Otherwise, try to create a new subsequence starting from num
            elif freq.get(num, 0) > 0 and freq.get(num + 1, 0) > 0 and freq.get(num + 2, 0) > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                # New subsequence now expects num+3.
                vacancy[num + 3] = vacancy.get(num + 3, 0) + 1
            else:
                return False
        
        return True