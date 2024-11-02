class Solution(object):
    def reverseWords(self, s):
        s=s.strip();
        str2=""
        l1=s.split(" ");
        
        l2=[];
        for i in l1:
            if (i.isalnum()):
                l2.append(i);

        return (' '.join(l2[::-1]))
        