class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==color:
            return image

        ROWS=len(image)
        COLS=len(image[0])
        que=deque()
        startColor=image[sr][sc]
    
        image[sr][sc]=color

        dimensions=[(0,1), (1,0), (-1,0), (0,-1)]
        que.append((sr, sc))

        while que:
            r,c=que.popleft()
            for ro, co in dimensions:
                nr=ro+r
                nc=co+c
                if 0<=nr<ROWS and 0<=nc<COLS and image[nr][nc]==startColor:
                    que.append((nr, nc))
                    image[nr][nc]=color
        return image


        