class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n=len(nums)
        freq={}
        left=0
        wind_sum=0
        maxSum=0

        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
            wind_sum+=nums[i]

            if(i>=k):
                wind_sum-=nums[left]
                freq[nums[left]]-=1
                if(freq[nums[left]]==0):
                    del freq[nums[left]]
                left+=1

            if(len(freq)==k):
                maxSum=max(maxSum, wind_sum)
                
        return maxSum

###### the natural intuition that comes to mind is that the repetative values are first removed and if the windsize>k then size is adjusted accordingly######

    #     n=len(nums)
    #     l=r=0
    #     maxSum=0
    #     freq={}
    #     sum1=0

    #     while(r<n):

    #   increment freq for nums[r]
    #         freq[nums[r]] = freq.get(nums[r], 0) + 1
    #         sum1 += nums[r]

    #         # if we see a duplicate, move left until no duplicates
    #         while freq[nums[r]] > 1:
    #             freq[nums[l]] -= 1
    #             sum1 -= nums[l]
    #             if freq[nums[l]] == 0:
    #                 del freq[nums[l]]
    #             l += 1
            
    #         # if window is bigger than k, remove left
    #         if (r - l + 1) > k:
    #             freq[nums[l]] -= 1
    #             sum1 -= nums[l]
    #             if freq[nums[l]] == 0:
    #                 del freq[nums[l]]
    #             l += 1

    #         # check if window size = k could also check with freq len
    #         if (r - l + 1) == k:
    #             maxSum = max(maxSum, sum1)

    #         r += 1
    #     return maxSum
 




        # l=r=0
        # l1=[]
        # res=0
        # currCount=0
        # while r<n:
        #     if nums[r] not in l1 and currCount<k:
        #         l1.append(nums[r])
        #         currCount+=1
        #         l+=1
        #     elif nums[r] not in l1 and currCount==k:
                
        #         sum1=sum(l1)
        #         res=max(res,sum1)
        #         currCount+=1
        #         l+=1
        #         l1=[]
        #     elif nums[r] in l1 and currCount<=k:
        #         r=l
        #     r+=1
        # return res


#below are brute force approaches

        # res=0
        # for i in range(n):
        #     dict1={}
        #     currCount=0
        #     sum1=0
        #     for j in range(i,n):
        #         if nums[j] not in dict1:
        #             dict1[nums[j]]=1
        #             sum1+=nums[j]
        #             currCount+=1
        #         else:
        #             break
        #         if currCount==k:
        #             res=max(res,sum1)
        #             break
        # return res


        # n=len(nums)
        # maxSum=0
        # for i in range(n):

        #     visited=set()
        #     sum1=0

        #     for j in range(i, n):

        #         if(nums[j] in visited):
        #             break
        #         else:   
        #             sum1+=nums[j]
        #             if(j-i+1==k):
        #                 maxSum=max(maxSum, sum1)
        #                 break
        #             visited.add(nums[j])

        # return maxSum
        