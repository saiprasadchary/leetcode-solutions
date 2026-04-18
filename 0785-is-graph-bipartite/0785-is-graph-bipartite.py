class Solution(object):

    from collections import deque

    def check_bp(self, start, graph, visited, que):
        while que:
            parent=que.popleft()
            for node in graph[parent]:
                # fresh visit
                if visited[node]==-1:
                    visited[node]=1-visited[parent]
                    que.append(node)
                elif visited[node]==visited[parent]:
                    return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        #bfs approach
        ROWS=len(graph)
        if ROWS is None or ROWS == 1:
            return True
        #the concept of visited array comes in handy for the cyclic graph
        visited=[-1]*ROWS

        for start in range(ROWS):
            if len(graph[start]) is None:
                continue
            if visited[start]!=-1:
                continue
            que=deque()
            que.append(start) # 0-based indexing
            #marking for the coloring the first parent node i.e 0
            visited[0]=0
            if self.check_bp(start, graph, visited, que)==False:
                return False
        return True


                    

