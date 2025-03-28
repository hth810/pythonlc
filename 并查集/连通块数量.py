class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n=len(properties)
        pa = list(range(n))
        size=[1]*n
        def find(x):
            if pa[x]!=x:
                pa[x]=find(pa[x])
            return pa[x]

        def merge(x,y):
            rx,ry=find(x),find(y)
            if rx!=ry:
                if size[rx]<size[ry]:
                    pa[rx]=ry
                else:
                    pa[ry]=rx
                    if size[rx]==size[ry]:
                        size[rx]+=1


        masks=[]
        for i in properties:
            temp=set(i)
            mask=0
            for num in temp:
                mask |=1<<(num-1)
            masks.append(mask)
        for i in range(n):
            for j in range(i+1,n):
                intersect=bin(masks[i]&masks[j]).count('1')
                if intersect>=k:
                    merge(i,j)
        roots=set()
        for x in range(n):
            roots.add(find(x))
        return len(roots)