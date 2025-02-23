class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n=len(nums)

        dict_wind={}
        wind_sum=0
        maxSum=0
        for i in range(n):
            #considering every values into the dictionary
            if nums[i] not in dict_wind:
                dict_wind[nums[i]]=1
                wind_sum+=nums[i]
            else:
                dict_wind[nums[i]]+=1
                wind_sum+=nums[i]
            #incrementing the sum of the window irrespective of its presence in dictionary

            if i>=k:
                #decrementing the values to be deleted in the dict in the wind-sum
                wind_sum-=nums[i-k]
                dict_wind[nums[i-k]]-=1
                #removing its values 0 too, to clear the dictionary of unnecessary keys
                if dict_wind[nums[i-k]]==0:
                    del dict_wind[nums[i-k]]
            if len(dict_wind)==k:
                maxSum=max(maxSum, wind_sum)
        return maxSum

            









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
        