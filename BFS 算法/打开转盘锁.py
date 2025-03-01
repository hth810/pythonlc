class Solution:
    def plusOne(self,s,j):
        ch=list(s)
        if ch[j]=='9':
            ch[j]='0'
        else:
            ch[j]= str(int(ch[j])+1)
        return ''.join(ch)

    def minusOne(self,s,j):
        ch=list(s)
        if ch[j]=='0':
            ch[j]='9'
        else:
            ch[j] = str(int(ch[j]) - 1)
        return ''.join(ch)

    def openLock(self, deadends: List[str], target: str) -> int:
        deads=set(deadends)
        visits=set()
        from collections import deque
        q=deque()
        step=0
        q.append('0000')
        visits.add('0000')

        while q:
            sz=len(q)
            for _ in range(sz):
                cur=q.popleft()
                if cur in deads:
                    continue
                if cur==target:
                    return step
                for j in range(4):
                    up=self.plusOne(cur,j)
                    if up not in visits:
                        q.append(up)
                        visits.add(up)
                    down=self.minusOne(cur,j)
                    if down not in visits:
                        q.append(down)
                        visits.add(down)

            step+=1
        return -1
