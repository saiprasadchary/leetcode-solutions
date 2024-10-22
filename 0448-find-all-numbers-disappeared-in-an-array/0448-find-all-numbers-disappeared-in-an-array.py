class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Create a set of all numbers that should appear in the array
        # num_set=set();
        # for x in range(1, len(nums)+1):
        #     num_set.add(x)  
        # # Remove each number that appears in nums
        # for num in (nums):
        #     if num in num_set:
        #         num_set.remove(num)
        
        # # The remaining numbers in num_set are the missing numbers
        # return list(num_set)
        set_nums=set(nums)

        l1=[];
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                l1.append(i)
        return l1