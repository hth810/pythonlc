class OrderedStream:

    def __init__(self, n: int):
        self.res=['']*n
        self.ptr=0

    def insert(self, idKey: int, value: str) -> List[str]:
        ans=[]
        self.res[idKey-1]=value
        for i in range(self.ptr,len(self.res)):
            if not self.res[i]:
                self.ptr=i
                break
            else:
                ans.append(self.res[i])

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)