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

        # Interleave positive and negative numbers
        i, j, k = 0, 0, 0  # 'i' for pos_arr, 'j' for neg_arr, 'k' for ans
        while k < len(pos_arr):
            ans[2*k]= pos_arr[k];
            ans[2*k +1] = neg_arr[k];
            k+=1
        return ans






























