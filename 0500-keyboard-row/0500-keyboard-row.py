class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3= "zxcvbnmZXCVBNM"
        l1=[];
        for word in words:
            temp=len(word)
            c1=0;
            c2=0;
            c3=0
            wording=""
            for char in word:
                print(char)
                if (char in row1):
                    wording+=char;
                    c1+=1
                elif (char in row2):
                    wording+=char;
                    c2+=1;
                    print(wording, c2)
                elif (char in row3):
                    wording+=char;
                    c3+=1;
            
            if c1  == temp or c2== temp or c3== temp:
                l1.append(wording);
        return l1
