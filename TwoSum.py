#LEETCODE SOLUTION


# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]  
#         return []



#SOLUTION


arr = [1,2,3,4,5,6]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)): 
        a = arr[i]
        b = arr[j]
        
        if (a + b) == target:
            print(f"{a} + {b} = {target}")

# 3 + 6 = 9
# 4 + 5 = 9
