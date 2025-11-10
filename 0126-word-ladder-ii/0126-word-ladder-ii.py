from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        neighbors = defaultdict(list)
        for word in wordSet:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        level = {beginWord: 0}
        parents = defaultdict(set)
        queue = deque([beginWord])

        while queue:
            word = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in neighbors[pattern]:
                    if nei not in level:
                        level[nei] = level[word] + 1
                        queue.append(nei)
                    if level[nei] == level[word] + 1:
                        parents[nei].add(word)

        if endWord not in parents:
            return []

        res = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res