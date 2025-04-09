class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        n=len(people)
        
        left=0
        right=n-1
        people.sort()
        boats=0

        while left<=right:
            print(left, right)
            if(people[left]+people[right]<=limit):
                boats+=1
                left+=1
                right-=1
            else:
                boats+=1
                right-=1
        return boats



        