class Solution(object):
    def isPossible(self, nums):
        freq={}
        n=len(nums)
        vacancy={}
        for k in nums:
            freq[k]=freq.get(k,0)+1

        for i in range(n):
            if(freq[nums[i]]==0):
                continue

            if(vacancy.get(nums[i],0)>0):
                vacancy[nums[i]]-=1
                vacancy[nums[i]+1]=vacancy.get(nums[i]+1, 0)+1
                freq[nums[i]]-=1
            
            elif freq.get(nums[i], 0) > 0 and freq.get(nums[i] + 1, 0) > 0 and freq.get(nums[i] + 2, 0) > 0:                
                freq[nums[i]]-=1
                freq[nums[i]+1]-=1
                freq[nums[i]+2]-=1

                vacancy[nums[i]+3]=vacancy.get(nums[i]+3, 0)+1

            else:
                return False
        return True
            