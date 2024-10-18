class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_s = {}

        # Count frequencies in s
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1

        # Check against frequencies in t
        for i in t:
            if i not in dict_s or dict_s[i] == 0:
                return i
            else:
                dict_s[i] -= 1
