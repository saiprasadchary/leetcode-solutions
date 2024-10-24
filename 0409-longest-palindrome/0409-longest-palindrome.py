class Solution(object):
    def longestPalindrome(self, s):
        
        if len(s)==1:
            return 1
        count=0
        count_dict={};
        odd_found=False;
        for i in s:
            if i not in count_dict:
                count_dict[i]=1;
            else:
                count_dict[i]+=1;
        for u in count_dict.values():
            if u%2==0:
                count+=u;
            else:
                odd_found=True;
                count+=u-1;
        if odd_found:
            return count+1;
        else:
            return count