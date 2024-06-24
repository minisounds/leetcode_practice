def hasDuplicate(nums: list[int]) -> bool:
        # sort
        # iterate through (2*O(n))
        # watch out for edge cases: empty list, length 1 list
        # iterate once through array

    nums.sort() #O(n)
    if len(nums) == 0 or len(nums) == 1: # empty or length 1
        return True 
        
    for i in range(1, len(nums)): 
        prev = i-1
        if nums[prev] == nums[i]: 
            return False 
    
    return True

print(hasDuplicate(nums=[1,2,3,3]))