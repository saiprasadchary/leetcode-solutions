class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        normal_case={"I": 1,"V":5,"X":10, "L":50,"C":100, "D":500, "M":1000}
        special_case = { "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        i = 0
        val = 0
        while i < len(s):
            s1=s[i:i+2]
            if i<len(s)-1:
                if s1 in special_case:
                    val+=special_case[s1]
                    i+=2;
                    print("s1",val)
                elif s[i] in normal_case:
                    val+=normal_case[s[i]]
                    i+=1;
                    print(val)
            else:
                val+=normal_case[s[i]]
                i+=1;
        return val;
            


            




            

        