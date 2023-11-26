def twoSum( nums, target):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if(x == y):
                continue
            else:
                if(nums[x] + nums[y] == target):
                    print (x)
                    print (nums[x])
                    print (y)
                    print (nums[y])
                    return [x,y]
                else:
                    continue
print(twoSum([7,27,6,4,5,566,7,7],11))


