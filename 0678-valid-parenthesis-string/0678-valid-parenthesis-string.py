class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # we maintain a range of min and max values to check the count
        mini,maxi=0,0

        for i in range(len(s)):
            if(s[i]=="("):
                mini+=1
                maxi+=1
            elif(s[i]==")"):
                mini-=1
                maxi-=1
                if(mini<0):
                    mini=0
            else:
                mini-=1
                maxi+=1
            # if(mini<0 and maxi>=0):
            #     mini=0
                if(mini<0):
                    mini=0
            if(maxi<0):
                return False
        return (mini==0)

        