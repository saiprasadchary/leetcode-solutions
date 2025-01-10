class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        n = len(num)
        if n == k:
            return "0"

        for i in range(n):
            while st and k > 0 and st[-1] > num[i]:
                st.pop()
                k -= 1
            st.append(num[i])
        
        # If there are still k digits left to remove, remove them from the end
        while k > 0:
            st.pop()
            k -= 1
        
        # Convert stack to string and strip leading zeros
        result = ''.join(st).lstrip('0')
        return result if result else "0"


        