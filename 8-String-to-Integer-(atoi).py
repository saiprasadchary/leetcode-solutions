class Solution(object):
    def myAtoi(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        i=0;
        n=len(s);

        while i<n and s[i]==\ \:
            i+=1;
        if i==n:
            return 0;

        sign=1;
        if i<n and s[i]==\-\:
            sign=-1
            i+=1
        elif i<n and s[i]==\+\:
            sign=1
            i+=1;

        res=0
        while i<n and s[i].isdigit():
            res=res*10+int(s[i]);
            i+=1;

        if sign==1 and res>(2**31-1):
            res = 2**31-1
        if sign==-1 and res>(2**31):
            res = 2**31
        
        res=res*sign;
        return res