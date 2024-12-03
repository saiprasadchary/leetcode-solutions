class Solution:
    def longestPalindrome(self, s):
        if len(s) < 1:
            return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = \\
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal
            
            # Even length palindromes (two character center)
            if i + 1 < len(s):
                even_pal = expandAroundCenter(i, i + 1)
                if len(even_pal) > len(longest):
                    longest = even_pal
        
        return longest