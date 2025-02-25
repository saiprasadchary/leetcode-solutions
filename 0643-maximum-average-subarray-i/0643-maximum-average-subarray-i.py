class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        l=r=0
        temp=nums[0]
        max_avg=float("-inf")
        avg=0.0

        while r<n:  
            if r-l+1==k:
                print(temp)
                avg=temp/float(k)
                max_avg=max(avg, max_avg)   
                temp-=nums[l]
                l+=1
            r+=1
            if r<n:  
                temp+=nums[r]
        return max_avg


        # n=len(nums)
        # maxAvg=float("-inf")
        # for i in range(n-k+1):
        #     temp=0.0
        #     for j in range(i,n):
        #         if (j-i+1)==k:
        #             print(j)
        #             temp+=nums[j]
        #             avg=temp/k
        #             maxAvg=max(avg,maxAvg)
        #             break
        #         temp+=nums[j]
        # return maxAvg          
        