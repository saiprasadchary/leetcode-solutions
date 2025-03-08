class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {

        int negInd=-1;
        int maxInd=-1;
        int minInd=-1;
        long count=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==minK)
                minInd=i;
            if(nums[i]==maxK)
               maxInd=i;

            if(nums[i]<minK || nums[i]>maxK) negInd=i;
                
                    count+=Math.max(0,Math.min(minInd,maxInd)-negInd);           
               
        } return count;
        
    }
}