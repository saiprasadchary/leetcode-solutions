class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0;
        maxi=0
        for i in range(len(nums)):
            if nums[i]!=1:
                c=0;
                if maxi<c:
                    maxi=c;
                
            else:
                c+=1
                maxi=max(maxi,c)
                if maxi<c:
                    maxi=c;


                print(maxi)
        return maxi
        