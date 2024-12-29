class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        stack=[];
        for i in range(len(s)):
            if s[i]=='(':
                if stack:
                    ans+="(";
                stack.append(s[i]);
            else:
                stack.pop()
                if stack:
                    ans+=")"
        return ans;
        