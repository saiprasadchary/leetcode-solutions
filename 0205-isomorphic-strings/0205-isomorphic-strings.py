class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t={};
        t_s={};
        
        for u, v in zip(s,t):
            if (u in s_t and s_t[u]!=v) or (v in t_s and t_s[v]!=u):
                return False;
            s_t[u]=v;
            t_s[v]=u;
        return True;
        

               