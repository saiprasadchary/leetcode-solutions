
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
        

        #actual code starts here
        time=0
        que=deque()

        while heap or que:
            time+=1

            if heap:
                # poping the heap value to make it count decrease
                cnt=1+heapq.heappop(heap)
                # if count>0, thenext instance of same task should be designed in the queue mentioning the place taking
                if cnt:
                    que.append([cnt, time+n]) # remaining taskscount and the idle time for that particular task

            # the que values i.e the place holders, up on return should be appended into the heap
            if que and que[0][1]==time:
                heapq.heappush(heap, que.popleft()[0])

        return time

        
        

        
        
        