class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=3
        return self.NSSK(s, k)-self.NSSK1(s, k-1)
        # n=len(s)
        # cnt=0
        # last_seen={'a':-1, 'b':-1, 'c':-1}
        # for i in range(n):
        #     last_seen[s[i]]=i
        #     #if(last_seen.get('a',0)!=-1 and last_seen.get('b',0)!=-1 and last_seen.get('c',0)!=-1):
        #     #cnt=cnt+1+min(last_seen.get('a',0), last_seen.get('b',0), last_seen.get('c',0))
        #     cnt=cnt+1+min(last_seen.values())
        # return cnt


     # brute forces
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

        # n=len(s)
        # cnt=0
    
        # for i in range(n):
        #     visited=set()
        #     for j in range(i,n):
        #         visited.add(s[j])
        #         if(len(visited)==3):
        #             print(i,j)
        #             cnt+=1
        #         if(len(visited)>3):
        #             break
                
        # return cnt
    def NSSK1(self, s, k):
        l=r=0
        n=len(s)
        freq={}
        cnt=0

        while r<n:

            freq[s[r]]=freq.get(s[r],0)+1

            while(len(freq)>k):
                freq[s[l]]-=1
                if(freq[s[l]]==0):
                    del freq[s[l]]
                l+=1
                
            cnt+=r-l+1
            r+=1
        return cnt

    def NSSK(self, s, k):
        l=r=0
        n=len(s)
        freq={}
        cnt=0

        while r<n:

            freq[s[r]]=freq.get(s[r],0)+1
                
            cnt+=r-l+1
            r+=1
        return cnt

