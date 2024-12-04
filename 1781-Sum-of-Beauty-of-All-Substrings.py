class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """

        c=0;
        for i in range(len(s)):
            temp_dict={};
            for j in range(i, len(s)):
                u=s[j]
                temp_dict[u]=temp_dict.get(u,0)+1
                #print(temp_dict, str1)
                if len(temp_dict)>=2:
                    maxi=max(temp_dict.values());
                    mini=min(temp_dict.values());
                    if maxi>mini:
                        c+=maxi-mini 
                        
        return c;

                        



        