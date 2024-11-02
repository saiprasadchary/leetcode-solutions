class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0=0;
        count_1=0;
        count_2=0;

        for i in range(len(nums)):
            if nums[i]==0:
                count_0+=1;
            elif nums[i]==1:
                count_1+=1;
            else:
                count_2+=1;
        
        # inplacing 0's;
        for i in range(count_0):
            nums[i]=0;
        
        for j in range(count_0, count_0 + count_1):
            nums[j]=1;
        
        for k in range(count_0+count_1 , count_0+count_1+count_2):
            nums[k]=2;
        
        return nums;



        # ******Brute Force ********** 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j]<nums[i]:
        #             nums[j],nums[i]=nums[i], nums[j];
        # return nums