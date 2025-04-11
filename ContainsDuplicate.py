def containsDuplicate(nums):
    for i in range (len(nums)-1):
        for j in range(1,len(nums)):
            if nums[i]==nums[j] and i!=j:
                return True
                break
    return False
print(containsDuplicate([1,2,3,1]))
