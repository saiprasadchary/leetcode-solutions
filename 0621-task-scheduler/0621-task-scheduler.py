
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        # Count frequencies of each task
        counts = Counter(tasks)
        # Build a max-heap by pushing negative counts
        pq = [-cnt for cnt in counts.values()]
        heapq.heapify(pq)
        
        result = 0
        # While there are still tasks to schedule
        while pq:
            time = 0
            tmp = []
            # Try to execute up to n+1 tasks in this cycle
            for i in range(n + 1):
                if pq:
                    # Pop the most frequent task (as negative, so add 1 to increment toward 0)
                    tmp.append(heapq.heappop(pq) + 1)
                    time += 1
            # Push remaining tasks (with non-zero counts) back into the heap
            for t in tmp:
                if t < 0:
                    heapq.heappush(pq, t)
            # If heap is empty, we don't need to idle for a full cycle
            result += time if not pq else n + 1
        
        return result