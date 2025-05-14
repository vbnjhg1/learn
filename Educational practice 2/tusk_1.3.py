nums = [1,1,1,3,3,4,3,2,4,2]
def flcomb(nums):
    nums.sort()
    point = nums[0]
    count = 0
    flag = False
    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                count += 1
            if count == 2:
                flag = True
        return flag

print(flcomb(nums))
