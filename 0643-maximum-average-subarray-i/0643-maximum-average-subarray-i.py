class Solution(object):
    def findMaxAverage(self, nums, k):
        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window from index k to end of list
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / float(k)





        # n=len(nums)
        # maxAvg=float("-inf")
        # for i in range(n-k+1):
        #     temp=0.0
        #     for j in range(i,n):
        #         if (j-i+1)==k:
        #             print(j)
        #             temp+=nums[j]
        #             avg=temp/k
        #             maxAvg=max(avg,maxAvg)
        #             break
        #         temp+=nums[j]
        # return maxAvg          
        