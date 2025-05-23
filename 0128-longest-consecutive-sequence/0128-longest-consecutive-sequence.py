class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
       
        set1=set(nums)

        maxlen=0
        for num in set1:
            if(num-1 not in set1):
                k=0
                cnt=0
                while num+k in set1:
                    cnt+=1
                    maxlen=max(maxlen, cnt)
                    k+=1
            
        return maxlen

        
        # #bruteforce approach
        # if not nums:
        #     return 0
        # if len(nums)==1:
        #     return 1
        # maxlen=1
        # cnt=1
        # nums=list(set(nums))
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if(nums[i-1]+1==nums[i]):
        #         cnt+=1
        #         maxlen=max(cnt, maxlen)
        #     else:
        #         cnt=1
        # return maxlen

        