class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen={};
        for ind, val in enumerate(nums):
            if val in seen:
                if(abs(seen[val]-ind) <= k):
                    return True;
            seen[val]=ind;
        return False;


        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         print(abs(i-j))
        #         if nums[i]==nums[j] and abs(j-i)<=k:
        #             return True;
        # return False
        