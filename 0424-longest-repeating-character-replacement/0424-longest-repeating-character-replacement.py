class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Dictionary to keep frequency count of characters in the current window.
        freq = {}
        left = 0             # Left pointer of the sliding window.
        max_count = 0        # Maximum frequency of any character in the current window.
        max_length = 0       # Length of the longest valid window found.

        # Iterate over the string with right pointer.
        for right in range(len(s)):
            # Increase the frequency of the current character.
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the maximum frequency found in the window.
            max_count = max(max_count, freq[s[right]])

            # Current window size is (right - left + 1).
            # If the number of characters that need to be replaced is more than k, shrink the window.
            if (right - left + 1) - max_count > k:
                # Reduce the count of the character going out of the window.
                freq[s[left]] -= 1
                left += 1  # Move the left pointer to shrink the window.

            # Update the maximum length if the current window is larger.
            max_length = max(max_length, right - left + 1)

        return max_length