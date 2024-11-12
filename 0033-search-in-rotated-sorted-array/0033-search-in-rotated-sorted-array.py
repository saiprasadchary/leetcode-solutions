class Solution(object):
    def search(self, nums, target):
   
        low=0;
        n=len(nums);
        high=n-1;
        while low<=high:
            mid=(low+high)//2;
            if(nums[mid]==target):
                return mid;
            
            if nums[low]<=nums[mid]:
                #left portion is sorted;
                if nums[low]<=target<nums[mid]:
                    high=mid-1;
                else:
                    low=mid+1;
            else:
                #right portion is sorted;
                if nums[mid]<target<=nums[high]:
                    low=mid+1; 
                else:
                    high=mid-1;
        return -1;
        
        
        
        # left, right = 0, len(nums) - 1
        
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
            
        #     # Check if the left half is sorted
        #     if nums[left] <= nums[mid]:
        #         if nums[left] <= target < nums[mid]:  # Target is in the left sorted half
        #             right = mid - 1
        #         else:  # Target is in the right half
        #             left = mid + 1
        #     else:  # Right half must be sorted
        #         if nums[mid] < target <= nums[right]:  # Target is in the right sorted half
        #             left = mid + 1
        #         else:  # Target is in the left half
        #             right = mid - 1

        # return -1  # Target not found
            