class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        n=len(players)
        m=len(trainers)
        players.sort()
        trainers.sort()
        i=j=0

        while j<m and i<n:

            if players[i]<=trainers[j]:
                i+=1
            j+=1

        return i
        


        