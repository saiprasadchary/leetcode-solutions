class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def mod_exp(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        even_count = (n + 1) // 2  # Every other index starting from 0 (inclusive) for n elements
        odd_count = n // 2         # Every other index starting from 1 for n elements
        
        even_choices = mod_exp(5, even_count, MOD)  # Even indexed positions can be filled with any of 5 even numbers
        odd_choices = mod_exp(4, odd_count, MOD)    # Odd indexed positions (if any) can be filled with any of 4 primes

        return (even_choices * odd_choices) % MOD