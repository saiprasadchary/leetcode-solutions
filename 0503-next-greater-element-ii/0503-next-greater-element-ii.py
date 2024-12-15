class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums);
        res=[-1]*n;

        for i in range(n):
            for j in range(i+1, i+n):
                ind=j%n;
                if nums[ind]>nums[i]:
                    res[i]=nums[ind];
                    break
        return res
            





        # n=len(nums)
        # res=[-1]*n
        
        # for i in range(n):
        #     found=i
        #     for j in range(i+1, n):
        #         if nums[j]>nums[i]:
        #             res[i]=nums[j];
        #             found=0
        #             break;
        #     if found!=0:
        #         for k in range(j):
        #             if nums[k]>nums[i]:
        #                 res[i]=nums[k];
        #                 break;
        # return res;  
