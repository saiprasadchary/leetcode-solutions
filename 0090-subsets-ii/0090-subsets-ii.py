class Solution(object):

    def dfs_helper(self, nums, i, sublist, op):
        if i==len(nums):
            op.append(sublist[:])
            return
        
        #picking
        sublist.append(nums[i])
        self.dfs_helper(nums, i+1, sublist, op)

        #backtrack
        sublist.pop()

        #skipping the duplicates in middle
        idx=i+1
        while idx<len(nums) and nums[idx]==nums[idx-1]:
            idx+=1

        #not picking
        self.dfs_helper(nums, idx, sublist, op)


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        op=[]
        sublist=[]

        self.dfs_helper(nums, 0, sublist, op)
        return op
    
        