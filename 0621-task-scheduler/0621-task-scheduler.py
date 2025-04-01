
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        # Count frequencies of each task
        m=len(tasks)
        freq={}
        heap=[]

        for char in tasks:
            freq[char]=freq.get(char, 0)+1
            
        # freq{"A":3, "B":2, "c":2}

        # pushing the freqval into the maxheap
        for v in freq.values():
            heapq.heappush(heap, -v)
        
        time=0
        que=deque()

        while heap or que:
            time+=1

            if heap:
                cnt=1+heapq.heappop(heap)

                if cnt:
                    que.append([cnt, time+n]) # remaining taskscount and the idle time for that particular task

            if que and que[0][1]==time:
                heapq.heappush(heap, que.popleft()[0])

        return time

        
        

        
        
        