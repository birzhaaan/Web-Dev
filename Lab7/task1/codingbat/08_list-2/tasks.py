#1
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 ==0:
      count+=1
  return count

#2
def big_diff(nums):
  maximum = nums[0]
  for i in range(len(nums)):
    if nums[i] > maximum:
      maximum = nums[i]
  minimum = nums[0]
  for i in range(len(nums)):
    if nums[i] < minimum:
      minimum = nums[i]
  return maximum-minimum

#3
def centered_average(nums):
    nums.sort() 
    return sum(nums[1:-1]) // (len(nums) - 2)

#4
def sum13(nums):
    total = 0
    i = 0
    
    while i < len(nums):
        if nums[i] == 13:
            i += 2  
        else:
            total += nums[i]
            i += 1
    
    return total

#5
def sum67(nums):
    total = 0
    ignore = False  

    for num in nums:
        if num == 6:
            ignore = True  
        elif num == 7 and ignore:
            ignore = False 
        elif not ignore:
            total += num  

    return total

#6
def has22(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 2 and nums[i + 1] == 2:
            return True  
    return False