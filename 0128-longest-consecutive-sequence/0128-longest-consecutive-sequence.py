class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        maxlen = 0
        
        for num in num_set:
            # Start only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1
                
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                maxlen = max(maxlen, streak)
        
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

        