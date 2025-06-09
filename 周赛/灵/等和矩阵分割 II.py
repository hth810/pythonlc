class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total=sum(sum(row) for row in grid)
        def check(a):
            m,n=len(a),len(a[0])
            def f(a):
                st={0}
                s=0
                for i,row in enumerate(a[:-1]):
                    for j,x in enumerate(row):
                        s+=x
                        if i>0 or j==0 or j==n-1:
                            st.add(x)
                    if n==1:
                        if s*2==total or s*2-total==a[0][0] or row[0]:
                            return True
                        continue
                    if s*2-total in st:
                        return True
                    if i==0:
                        st.update(row)
                return False
            return f(a) or f(a[::-1])
        return check(grid) or check(list(zip(*grid)))
