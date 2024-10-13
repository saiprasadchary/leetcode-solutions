class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str2="";
        for i in s:
            if i.isalnum():
                if(i.isalpha() and i.isupper()):
                    str2+=i.lower();
                else:
                    str2+=i

        c=0;
        for i in range(len(str2)//2):
            if(str2[i]==str2[len(str2)-i-1]):
                c+=1
        print(c)
        if c==len(str2)//2:
            return True;
        else:
            return False

