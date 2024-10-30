class Solution(object):
    def moveZeroes(self, nums):
        j=0;
        for i in range(1, len(nums)):
            if nums[i]!=0 and nums[j]==0:
                nums[i], nums[j]=nums[j],nums[i];
                j+=1;
            elif nums[i]==0 and nums[j]==0:
                continue
            else:
                j+=1;
        




            
