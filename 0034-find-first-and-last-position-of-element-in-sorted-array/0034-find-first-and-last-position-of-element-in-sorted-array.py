class Solution(object):
    def initialfn(self, nums, target):
        start=-1;
        low=0;
        n=len(nums);
        high=n-1
    
        while low<=high:
            mid=(high+low)//2;
            if(nums[mid]==target):
                start=mid;
                high=mid-1;
            elif(nums[mid]> target):
                high=mid-1; 
            else:
                low=mid+1;
        return start;
    def endfn(self, nums, target):
        end=-1;
        low=0;
        n=len(nums);
        high=n-1;

        while low<=high:
            mid=(high+low)//2;
            if(nums[mid]==target):
                end=mid;
                low=mid+1
        
            elif(nums[mid]> target):
                high=mid-1; 
            else:
                low=mid+1
        return end;

    def searchRange(self, nums, target):
        start=self.initialfn( nums, target);
        if(start==-1):
            return [-1,-1];
        end=self.endfn(nums, target);
        return [start, end]
    
            


        # start=-1;
        # end=-1;
        # flag=1
        # for i in range(len(nums)):
            
        #     if nums[i]==target and flag==1:
        #         flag=0;
        #         start=i;
        #         end=i
        #     elif nums[i]==target and flag==0:
        #         end=i;
        #         continue;
        # return [start, end]
            

            

            
        