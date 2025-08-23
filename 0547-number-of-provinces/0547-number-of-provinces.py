class Solution(object):
    def dfs(self, node, visited, adjList):
        visited[node] = True
        for neighbor in adjList[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adjList)

    def findCircleNum(self, isConnected):
        V = len(isConnected)
        adjList = [[] for _ in range(V)]

        # Build adjacency list from adjacency matrix
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adjList[i].append(j)
                    adjList[j].append(i)

        visited = [False] * V
        res = 0

        for i in range(V):
            if not visited[i]:
                self.dfs(i, visited, adjList)
                res += 1  # one connected component found

        return res