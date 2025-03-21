class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x:x[0])
        cover=ans=l=0
        for tl,tr in tiles:
            cover+=tr-tl+1
            while tiles[l][1]<tr-carpetLen+1:
                cover-=tiles[l][1]-tiles[l][0]+1
                l+=1
            uncover=max(tr-tiles[l][0]+1-carpetLen,0)
            ans=max(ans,cover-uncover)

        return ans