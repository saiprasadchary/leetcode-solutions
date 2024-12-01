class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RomInt={
        "I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000};

        SpclCase={"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400,"CM": 900};
        
        res=0;
        i=len(s);

        while i!=0:
            if s[i-2:i] in SpclCase:
                res+=SpclCase[s[i-2:i]];
                i-=2;
            elif s[i-1:i] in RomInt:
                res+=RomInt[s[i-1:i]];
                i-=1;
        return res