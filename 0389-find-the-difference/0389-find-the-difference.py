class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dict_s = {}

        # # couting the chars in the base dictionary i.e dict_s:
        # for i in s:
        #     if i not in dict_s:
        #         dict_s[i]=1;
        #     else:
        #         dict_s[i]+=1;
        
        # # check if the count of the ele in the t is present or not;

        # for j in t:
        #     if j not in dict_s or dict_s[j]==0:
        #         return j;
        #     else:
        #         # negate the cout in the existing dictionary
        #         dict_s[j]-=1;
        x=0;
        for i in s+t:
            x=x^ord(i)
        return chr(x)
            

