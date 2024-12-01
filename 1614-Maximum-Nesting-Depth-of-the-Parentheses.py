class Solution(object):
    def maxDepth(self, s):

        c=0;
        k=0;
        for i in s:
            if i=="(":
                c+=1;
                k=max(k,c)
            elif i==")":
                c-=1;
        return k






        # stack=[];
        # k=0;
        # c=0;
        # for i in s:
        #     if i==")":
        #         c-=1
        #         while stack:
        #             if stack.pop()=="(": 
        #                 break;
        #             if stack:
        #                 stack.pop()
        #     elif i=="(":
        #         c+=1;
        #         k=max(k,c)
        #     else: 
        #         stack.append(i);
        # return k

        