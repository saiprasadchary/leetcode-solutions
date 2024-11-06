class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg_arr = []
        pos_arr = []
        ans = [0] * len(nums)  # Use 'ans' instead of directly modifying 'nums'

        # Separate negative and positive numbers
        for num in nums:
            if num < 0:
                neg_arr.append(num)
            else:
                pos_arr.append(num)

        k=0;
        while k < len(pos_arr):
            nums[2*k]= pos_arr[k];
            nums[2*k +1] = neg_arr[k];
            k+=1
        return nums






























