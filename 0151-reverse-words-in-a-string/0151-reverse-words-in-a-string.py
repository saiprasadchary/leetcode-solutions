class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=s.split();
        #s1=list(s.split(" "))
        print(s1)

        return " ".join(s1[::-1])

        # s=s.strip();
        # s2=''
        # s=s.split()

        # print(s)
        # s=s[::-1]
        # n=len(s)
        # for i in range(n):
     
        #     s2+=s[i];
        #     if i!=n-1:
        #         s2+=" "
        # s2.rstrip("  ")
        # return s2;