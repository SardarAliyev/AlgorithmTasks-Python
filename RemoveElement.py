def removeElement(nums, val):

    for i in nums:
        if i == val:
           nums.remove(i)

    return len(nums),nums

print(removeElement([3,2,2,3],3))
