class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False;
        goal1=''
        for i in range(len(s)):
            goal1=goal[i+1:]+goal[:i+1]
            print(goal1)
            if goal1 == s:
                return True;
        return False;

        