class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t={};
        t_s={};

        for i, j in zip(s,t):
            if ((i in s_t and s_t[i]!=j) or (j in t_s and t_s[j]!=i)):
                return False

            s_t[i]=j;
            t_s[j]=i;


        return True
                