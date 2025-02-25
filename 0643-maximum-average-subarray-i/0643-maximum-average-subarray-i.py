class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        l=0
        avg=0.0
        x=1/float(k)

        ksum=sum(nums[:k])
        maxavg=ksum*x

        for i in range(k,n):
            ksum= ksum-nums[l]+nums[i]
            avg=ksum*x
            maxavg=max(avg, maxavg)
            l+=1
        return maxavg

        # an optimal solution that doesn't consider the first k elements calculations but (optimal)
        # l=r=0
        # temp=nums[0]
        # max_avg=float("-inf")
        # avg=0.0
        # x=1.0/k

        # while r<n:  
        #     if r-l+1==k: 
        #         avg=temp*x
        #         max_avg=max(avg, max_avg)   
        #         temp-=nums[l]
        #         l+=1
        #     r+=1
        #     if r<n:  
        #         temp+=nums[r]
        # return max_avg


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
        