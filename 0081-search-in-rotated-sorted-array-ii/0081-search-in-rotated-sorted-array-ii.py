class Solution(object):
    def search(self, nums, target):
   
        low=0;
        n=len(nums);
        high=n-1;
        while low<=high:
            mid=(low+high)//2;
            
            if(nums[mid]==target):
                return True;

            if(nums[mid]==nums[low] and nums[mid]==nums[high]):
                low=low+1;
                high=high-1;
                continue
            
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
        return False;
        
       