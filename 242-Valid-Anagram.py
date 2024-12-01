class Solution(object):
    def isAnagram(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: bool
        \\\
        if len(s)!=len(t):
            return False;
        s_t={};
        
        for i in s:
            if i not in s_t:
                s_t[i]=1;
            else:
                s_t[i]+=1;
        
        for u,v in zip(s,t):
            if v in s_t:
                s_t[v]-=1;
                if s_t[v]==0:
                    del[s_t[v]]
        print(s_t)
        if len(s_t)==0:
            return True;
        else:
            return False;



        # if len(s)!=len(t):
        #     return False
        # s1=sorted(s)
        # t1=sorted(t);
        # if s1==t1:
        #     return True;
        # else:
        #     return False;