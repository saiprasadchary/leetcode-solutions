class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums);
        longest=0;
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                c=1;
                k=nums[i]+1

                while k in s:
                    c+=1;
                    k+=1
                longest=max(longest,c);
        return longest;

        