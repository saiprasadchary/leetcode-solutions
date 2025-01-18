class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        max_size = 0

        for right, char in enumerate(s):
            if char not in seen:
                max_size = max(max_size, right - left + 1)
            
            else: 
                # not in the window so we can keep going
                if seen[char] < left:
                    max_size = max(max_size, right - left + 1)
                else: 
                # we need to reset left to the seen pointer
                    left = seen[char] + 1

            # Storing at which index we found the character
            seen[char] = right

        return max_size