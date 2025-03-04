class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        l = r = 0
        sum1 = 0
        c = 0
        while r < n:
            sum1 += nums[r]
            # The current window length is (r - l + 1)
            while (sum1 * (r - l + 1)) >= k and l <= r:
                sum1 -= nums[l]
                l += 1
            # Now, all subarrays ending at r and starting from l to r are valid.
            c += (r - l + 1)
            r += 1
        return c

        