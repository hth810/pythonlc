def _sort(nums):
    n=len(nums)
    sortedIndex=0
    while sortedIndex<n:
        for i in range(sortedIndex,0,-1):
            if nums[i]<nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            else:
                break
        sortedIndex+=1