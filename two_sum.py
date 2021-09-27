#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
def twoSum(nums, target):
    complimentMap=dict()
    for i in range(len(nums)):
        compliment=target-nums[i]
        if nums[i] in complimentMap :
            return [complimentMap[nums[i]],i]
        else:
            complimentMap[compliment]=i
nums=[int(x) for x in input().split()]
target=int(input())
print(twoSum(nums,target))