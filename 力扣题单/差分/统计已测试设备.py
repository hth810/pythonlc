class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n=len(batteryPercentages)
        cnt=0
        for i in batteryPercentages:
            if i>cnt:
                cnt+=1

        return cnt