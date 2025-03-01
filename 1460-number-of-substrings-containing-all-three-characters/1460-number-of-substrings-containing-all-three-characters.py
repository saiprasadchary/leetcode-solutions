class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        cnt=0
        last_seen={'a':-1, 'b':-1, 'c':-1}
        for i in range(n):
            last_seen[s[i]]=i
            #if(last_seen.get('a',0)!=-1 and last_seen.get('b',0)!=-1 and last_seen.get('c',0)!=-1):
            cnt=cnt+1+min(last_seen.get('a',0), last_seen.get('b',0), last_seen.get('c',0))
        return cnt


        # brute force
        # n=len(s)
        # cnt=0
        # for i in range(n):
        #     freq={}
        #     for j in range(i,n):
        #         freq[ord(s[j])-ord('a')]=1 # 0-->1(a), 1-->1(b), 2-->1(c) 
        #         if(freq.get(0,0)+freq.get(1,0)+freq.get(2,0) == 3):
        #             cnt=cnt+(n-j)
        #             break
        # return cnt;       