class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if (color==newColor):
            return image
        image[sr][sc] = newColor
        if ((sr>0) and (image[sr-1][sc]==color)):
            image = self.floodFill(image, sr-1, sc, newColor)
        if ((sc>0) and (image[sr][sc-1]==color)):
            image = self.floodFill(image, sr, sc-1, newColor)
        if ((sr<m-1) and (image[sr+1][sc]==color)):
            image = self.floodFill(image, sr+1, sc, newColor)
        if ((sc<n-1) and (image[sr][sc+1]==color)):
            image = self.floodFill(image, sr, sc+1, newColor)
        return image