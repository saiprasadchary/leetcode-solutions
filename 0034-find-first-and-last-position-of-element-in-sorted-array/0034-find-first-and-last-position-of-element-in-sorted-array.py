class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=-1;
        end=-1;
        flag=1
        for i in range(len(nums)):
            
            if nums[i]==target and flag==1:
                flag=0;
                start=i;
                end=i
            elif nums[i]==target and flag==0:
                end=i;
                continue;
        return [start, end]
            

            

            
        