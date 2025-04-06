class Solution(object):
    def isPossibleDivide(self, nums, k):
        n=len(nums)
        cnt=0

        if(n%k !=0):
            return False
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for val in sorted(freq.keys()):

            while freq[val]:
                for j in range(k):
                    curr=val+j
                    if(curr not in freq) or (freq[curr] == 0):
                        return False
                    freq[curr]-=1       
        return True


        
       
                
                    


        