class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        count = 0

        # Transform the array: odd numbers become 1, even numbers become 0.
        binary = [0] * n
        for i in range(n):
            if nums[i] % 2 == 0:
                binary[i] = 0
            else:
                binary[i] = 1  # Instead of nums[i], we want 1 for odd numbers.

        # Build the prefix sum array.
        pf = [0] * n
        pf[0] = binary[0]
        for i in range(1, n):
            pf[i] = pf[i - 1] + binary[i]

        # Dictionary to store frequency of prefix sums.
        dict1 = {}
        for j in range(n):
            # If the current prefix sum equals k, the subarray from index 0 to j is valid.
            if pf[j] == k:
                count += 1

            # Find the target prefix sum that would give a subarray sum of k.
            key = pf[j] - k
            if key in dict1:
                count += dict1[key]

            # Update the dictionary for the current prefix sum.
            if pf[j] in dict1:
                dict1[pf[j]] += 1
            else:
                dict1[pf[j]] = 1

        return count





        #bruteforce approach
        # c=0
        # for i in range(n):
        #     odd_c=0
        #     for j in range(i,n):
        #         if nums[j]%2!=0:
        #             odd_c+=1
        #         if odd_c==k:
        #             c+=1
        #         if odd_c>k:
        #             break
        # return c

