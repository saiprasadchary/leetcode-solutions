class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_beauty = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1

                if len(freq) > 1:
                    max_freq = max(freq.values())
                    min_freq = min(freq.values())
                    if max_freq > min_freq:
                        total_beauty += max_freq - min_freq
        
        return total_beauty