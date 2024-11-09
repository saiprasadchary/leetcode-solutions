class Solution(object):
    def searchInsert(self, nums, target):
        low=0;
        n=len(nums)
        if n<=0:
            return n+1;
        high=n-1;
        while low<=high:
            mid=low+high//n;
            if nums[mid]==target:
                return mid;
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1;
        print(mid)
        if nums[mid]>target:
            return mid;
        else:
            return mid+1
