class Solution(object):
    
    def fill(self, dist, xy, d, m, n):
        #print(dist, m, n, xy)
        x, y = xy[0], xy[1]
        if ((x<0) or (x>m-1) or (y<0) or (y>n-1)):
            return dist
        if (x>0 and dist[x-1][y]==-1):
            dist[x-1][y]=d
            dist = self.fill(dist, [x-1, y], d+1, m, n)
        if (y>0 and dist[x][y-1]==-1):
            dist[x][y-1]=d
            dist = self.fill(dist, [x, y-1], d+1, m, n)
        if (x<m-1 and dist[x+1][y]==-1):
            dist[x+1][y]=d
            dist = self.fill(dist, [x+1, y], d+1, m, n)
        if (y<n-1 and dist[x][y+1]==-1):
            dist[x][y+1]=d
            dist = self.fill(dist, [x, y+1], d+1, m, n)
        return dist
    
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if (m==1 and n==1):
            return mat
        dist = [[-1 for j in range(n)] for i in range(m)]
        firstZero = []
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    firstZero = [i, j]
                    dist[i][j] = 0
                    break
            if (len(firstZero)>0):
                break
        dist = self.fill(dist, firstZero, 1, m, n)
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    dist[i][j] = 0
                else:
                    if (m==1):
                        if (j==0):
                            dist[i][j] = 1 + dist[i][j+1]
                        elif (j==n-1):
                            dist[i][j] = 1 + dist[i][j-1]
                        else:
                            dist[i][j] = 1 + min(dist[i][j+1], dist[i][j-1])
                    elif (n==1):
                        if (i==0):
                            dist[i][j] = 1 + dist[i+1][j]
                        elif (i==m-1):
                            dist[i][j] = 1 + dist[i-1][j]
                        else:
                            dist[i][j] = 1 + min(dist[i+1][j], dist[i-1][j])
                    else:
                        if (i==0 and j==0):
                            dist[i][j] = 1 + min(dist[i][j+1], dist[i+1][j])
                        elif (i==0 and j==n-1):
                            dist[i][j] = 1 + min(dist[i][j-1], dist[i+1][j])
                        elif (i==m-1 and j==0):
                            dist[i][j] = 1 + min(dist[i][j+1], dist[i-1][j])
                        elif (i==m-1 and j==n-1):
                            dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1])
                        elif (i==0):
                            dist[i][j] = 1 + min(dist[i][j+1], dist[i+1][j], dist[i][j-1])
                        elif (j==n-1):
                            dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1], dist[i+1][j])
                        elif (j==0):
                            dist[i][j] = 1 + min(dist[i+1][j], dist[i][j+1], dist[i-1][j])
                        elif (i==m-1):
                            dist[i][j] = 1 + min(dist[i][j-1], dist[i-1][j], dist[i][j+1])
                        else:
                            dist[i][j] = 1 + min(dist[i-1][j], dist[i+1][j], dist[i][j-1], dist[i][j+1])
        for i in range(m):
            for j in range(n):
                if (m==1):
                        if (j==0):
                            dist[i][j] = min(dist[i][j], 1 + dist[i][j+1])
                        elif (j==n-1):
                            dist[i][j] = min(dist[i][j], 1 + dist[i][j-1])
                        else:
                            dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i][j-1]))
                elif (n==1):
                    if (i==0):
                        dist[i][j] = min(dist[i][j], 1 + dist[i+1][j])
                    elif (i==m-1):
                        dist[i][j] = min(dist[i][j], 1 + dist[i-1][j])
                    else:
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i+1][j], dist[i-1][j]))
                else:
                    if (i==0 and j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i+1][j]))
                    elif (i==0 and j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j-1], dist[i+1][j]))
                    elif (i==m-1 and j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i-1][j]))
                    elif (i==m-1 and j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i][j-1]))
                    elif (i==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i+1][j], dist[i][j-1]))
                    elif (j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i][j-1], dist[i+1][j]))
                    elif (j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i+1][j], dist[i][j+1], dist[i-1][j]))
                    elif (i==m-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j-1], dist[i-1][j], dist[i][j+1]))
                    else:
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i+1][j], dist[i][j-1], dist[i][j+1]))
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (m==1):
                        if (j==0):
                            dist[i][j] = min(dist[i][j], 1 + dist[i][j+1])
                        elif (j==n-1):
                            dist[i][j] = min(dist[i][j], 1 + dist[i][j-1])
                        else:
                            dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i][j-1]))
                elif (n==1):
                    if (i==0):
                        dist[i][j] = min(dist[i][j], 1 + dist[i+1][j])
                    elif (i==m-1):
                        dist[i][j] = min(dist[i][j], 1 + dist[i-1][j])
                    else:
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i+1][j], dist[i-1][j]))
                else:
                    if (i==0 and j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i+1][j]))
                    elif (i==0 and j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j-1], dist[i+1][j]))
                    elif (i==m-1 and j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i-1][j]))
                    elif (i==m-1 and j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i][j-1]))
                    elif (i==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j+1], dist[i+1][j], dist[i][j-1]))
                    elif (j==n-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i][j-1], dist[i+1][j]))
                    elif (j==0):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i+1][j], dist[i][j+1], dist[i-1][j]))
                    elif (i==m-1):
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i][j-1], dist[i-1][j], dist[i][j+1]))
                    else:
                        dist[i][j] = min(dist[i][j], 1 + min(dist[i-1][j], dist[i+1][j], dist[i][j-1], dist[i][j+1]))
        
        return dist
                                