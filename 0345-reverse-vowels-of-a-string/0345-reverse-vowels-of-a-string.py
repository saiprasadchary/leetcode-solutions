class Solution(object):
    def reverseVowels(self, s):
        l1=[];
        vowels=["a","e","i", "o", "u", "A", "E","I", "O", "U"]
        i=0;
        j=len(s)-1
        for k in s:
            l1.append(k)
        while i<=j:
            if l1[i] in vowels and l1[j] in vowels:
                l1[i], l1[j]=l1[j], l1[i];
                i+=1;
                j-=1;
            elif(l1[i] in vowels and l1[j] not in vowels):
                j-=1;
            elif(l1[i] not in vowels and l1[j] in vowels):
                i+=1;
            else:
                i+=1;
                j-=1;
        return "".join(l1)
                
