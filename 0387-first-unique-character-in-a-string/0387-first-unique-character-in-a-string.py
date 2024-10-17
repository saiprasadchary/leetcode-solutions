class Solution(object):
    def firstUniqChar(self, s):
        seen={};
        for ind , val in enumerate(s):
            if val not in seen:
                seen[val]=ind;
            else:
                seen[val]=-1;
        k=float('inf');
        for u,v in seen.items():
            if v<k and v>-1:
                k=v;
        
        if k==float('inf'):
            return -1;
        else:
            return k
