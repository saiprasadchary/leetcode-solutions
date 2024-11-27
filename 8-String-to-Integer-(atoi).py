class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1  # Maximum value for a 32-bit signed integer
        INT_MIN = -2**31     # Minimum value for a 32-bit signed integer
        
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':  # Skip leading whitespaces
            i += 1
        
        if i == n:  # If only whitespace is present
            return 0
        
        # Handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow and underflow
            if res > (INT_MAX - digit) / 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            res = res * 10 + digit
            i += 1
        
        return sign * res