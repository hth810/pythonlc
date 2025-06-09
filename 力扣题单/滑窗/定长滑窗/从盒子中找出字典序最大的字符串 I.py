class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n=len(word)
        k=n-numFriends+1
        ans=''
        temp=''
        for i,c in enumerate(word):
            temp+=c
            if i<k-1:
                continue
            ans=max(ans,temp)
            temp=temp[1:]
        if numFriends==1:
            return ans
        for i in range(len(temp)):
            ans=max(ans,temp[i:])
        return ans