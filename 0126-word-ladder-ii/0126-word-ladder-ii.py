from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        L = len(beginWord)
        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()
            wordSet -= level  # block revisits of this level in future levels

            for w in level:
                arr = list(w)
                for i in range(L):
                    old = arr[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == old: 
                            continue
                        arr[i] = c
                        nw = ''.join(arr)
                        if nw in wordSet:
                            parents[nw].add(w)
                            next_level.add(nw)
                    arr[i] = old

            if endWord in next_level:
                found = True
            level = next_level

        if not found:
            return []

        # backtrack all shortest paths from endWord to beginWord
        res, path = [], [endWord]
        def dfs(w):
            if w == beginWord:
                res.append(path[::-1])
                return
            for p in parents[w]:
                path.append(p)
                dfs(p)
                path.pop()
        dfs(endWord)
        return res