numbers = [2,1,3,4,2,3]
greater_than = lambda x,y: x if x > y else y

def maximum(nums, greater_than):
    max = nums[0]
    for x in nums[1:]:
        max = greater_than(x, max)
    return max


max_num = maximum(numbers, greater_than)
print(max_num)