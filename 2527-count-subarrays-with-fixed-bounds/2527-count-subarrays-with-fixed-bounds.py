
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        negInd=-1
        minInd=-1
        maxInd=-1
        n=len(nums)
        count=0

        for i in range(n):
            if(nums[i] == minK):
                minInd=i
            if(nums[i]== maxK):
                maxInd=i
            if(nums[i]> maxK or nums[i]< minK):
                negInd=i
            
            count+=max(0,min(minInd,maxInd)-negInd);  
            print(count, i)
        return count


        # c=0
        # n=len(nums)
        # arr=nums
        # for i in range(n):
        #     maxflag=0
        #     minflag=0
        #     flag=1
        #     for j in range(i,n):
        #         if(arr[j]!=minK and i==j):
        #             break
        #         if(arr[j]>=minK and arr[j]<=maxK):
        #             if(minK==arr[j]):
        #                 minflag=1
        #             if(maxK==arr[j]):
        #                 maxflag=1
        #             if(minflag ==1 and maxflag==1):
        #                 c+=1
        #         else:
        #             break
        # return c
        