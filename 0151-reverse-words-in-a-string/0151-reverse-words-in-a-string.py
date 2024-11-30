class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip();
        s2=''
        s=s.split()

        print(s)
        s=s[::-1]
        n=len(s)
        for i in range(n):
            
            print(i)
            s2+=s[i];
            if i!=n-1:
                s2+=" "
        s2.rstrip("  ")
        return s2;