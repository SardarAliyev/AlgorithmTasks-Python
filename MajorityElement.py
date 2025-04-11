def majorityElement(nums):

    for i in range(len(nums)):
        count=0
        for j in range(i,len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count>len(nums)//2:
            return nums[i]
    
print(majorityElement([1,1,1,1,1,1,1,1,4,5,6,7,8,9]))