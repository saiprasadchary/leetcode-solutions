class Solution(object):

    def dfs_helper(self, nums, i, sublist, op):
        # hitting the base case with the branch length exceeded or equals to the length(language wise)
        if i==len(nums):
            # here we are appending the list copy of that particular instance not the reference of list 
            op.append(sublist[:])
            return
        
        #pick case
        sublist.append(nums[i])
        self.dfs_helper(nums, i+1, sublist, op)

        # backtrack by removing the last added element to get the parent and travel to the desired side
        sublist.pop()

        #no pick
        self.dfs_helper(nums, i+1, sublist, op)
        

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        op=[]
        sublist=[]
        self.dfs_helper(nums, 0, sublist, op)
        return op

        