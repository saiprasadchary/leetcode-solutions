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
        while i < len(pos_arr) and j < len(neg_arr):
            ans[k] = pos_arr[i]
            ans[k+1] = neg_arr[j]
            i += 1
            j += 1
            k += 2

        # If there are leftover positives or negatives due to unequal lengths
        while i < len(pos_arr):
            ans[k] = pos_arr[i]
            i += 1
            k += 1
        
        while j < len(neg_arr):
            ans[k] = neg_arr[j]
            j += 1
            k += 1

        return ans
