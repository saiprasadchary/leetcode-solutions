class Solution:
    def isHappy(self, n):
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit ** 2
                number = number // 10
            return total_sum
        
        slow = n  # Tortoise starts at n
        fast = get_next(n)  # Hare starts at the next sum of n
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)  # Move tortoise one step
            fast = get_next(get_next(fast))  # Move hare two steps
        
        return fast == 1