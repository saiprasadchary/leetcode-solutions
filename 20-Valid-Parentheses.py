class Solution(object):
    def isValid(self, s):
        stack=[];

        for i in s:
            if i==\(\ or i ==\[\ or i==\{\:
                stack.append(i);
            else:
                if len(stack) ==0:
                    return False;
                char=stack.pop()
                if (i==')' and char==\(\ )or (i==']' and char==\[\) or (i==\}\ and char==\{\):
                    continue;
                else:
                    return False;
                        
        return len(stack)==0
        