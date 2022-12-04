file = open("Day4Input.txt")
count = 0
for line in file:
    nums = line.replace("-", ",").replace("\n", "").split(",")
    # print(nums)
    if(int(nums[2]) <= int(nums[1]) and int(nums[3]) >= int(nums[0])):
        count+= 1
print(count)
    

#Part 1 Solution
# file = open("Day4Input.txt")
# count = 0
# for line in file:
#     nums = line.replace("-", ",").replace("\n", "").split(",")
#     print(nums)
#     if((int(nums[0]) <= int(nums[2]) and int(nums[1]) >= int(nums[3])) or (int(nums[2]) <= int(nums[0]) and int(nums[3]) >= int(nums[1]))):
#         count+= 1
# print(count)
