class Solution(object):
    def AlreadySorted(self,nums):
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                print(i)
                return i;
        return True
        
    def check(self, nums):

        partitionIndex=self.AlreadySorted(nums)
        print(partitionIndex)
        if partitionIndex==True and type(partitionIndex)==bool:
            return True;
        else:
            arr=nums[partitionIndex:]+nums[0:partitionIndex]
            partitionIndex=self.AlreadySorted(arr)
            if (self.AlreadySorted(arr)==True) and type(partitionIndex)==bool:
                print("check")
                return True;
            else:
                return False
