def twoSum( nums, target):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if(x == y):
                continue
            else:
                if(nums[x] + nums[y] == target):
                    return [x,y]
                else:
                    continue

