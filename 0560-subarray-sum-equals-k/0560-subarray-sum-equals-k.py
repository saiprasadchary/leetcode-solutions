class Solution(object):
    def subarraySum(self, nums, k):
        # n=len(nums)
        # count=0
        # pfs=[0]*n
        # pfs[0]=nums[0]
        # for i in range(1,n):
        #     pfs[i]+=pfs[i-1]+nums[i]

        # m={}
        # for j in range(n):
        #     if pfs[j]==k:
        #         count +=1
        #     key=pfs[j]-k
        #     if key in m:
        #         count += m[key]
        #     if pfs[j] in m:
        #         m[pfs[j]] += 1
        #     else:
        #         m[pfs[j]] = 1
            
        # return count

        #####
        n=len(nums)
        freq={}
        freq[0]=1
        pref_sum=0
        cnt=0
        for i in range(n):
            pref_sum += nums[i]
            if(pref_sum-k in freq):
                cnt+=freq[pref_sum-k]
            freq[pref_sum] = freq.get(pref_sum, 0) + 1

        return cnt


       


      


        #^^^^^^^^^^^^

        # return self.SS(nums, k)-self.SS(nums, k-1)

    # def SS(self, a, k): trail esina    #subarray with sum==k (subarray with sum<=k - subarray with sum<=k-1)
    #     n = len(a)
    #     l = 0
    #     windSum = 0
    #     cnt = 0
    #     if k==0:
    #         return 0
    #     for r in range(n):
    #         windSum += a[r]
    #         # shrink the window if it exceeds k
    #         while l <= r and windSum > k:
    #             windSum -= a[l]
    #             l += 1
    #         # At this point, all subarrays ending at r and starting from l to r are valid.
    #         cnt += (r - l + 1)
    #     return cnt

  #^^^^^^^^^^^^^^^^^^^^

        # count=0
        # for i in range(n):
        #     arrSum=0;
        #     for j in range(i,n):
        #         arrSum+=nums[j] 
        #         if arrSum==k:
        #             count+=1
        # return count

        