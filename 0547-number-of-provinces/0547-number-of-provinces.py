class Solution(object):

    #dfs function to check the 
    def dfs(self, node, visited, adjList):
        visited[node] = 1
        for neighbor in adjList[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adjList)

    def findCircleNum(self, isConnected):
        V = len(isConnected)
        adjList=[]
        for _ in range(V):
            adjList.append([])

        # Build adjacency list from adjacency matrix
        for i in range(V):
            for j in range(i+1, V):
                if isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)

        visited = [0] * V
        res = 0

        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, visited, adjList)
                res += 1  # one connected component found

        return res