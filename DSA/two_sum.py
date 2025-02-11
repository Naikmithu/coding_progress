#using hash_map 

nums = [2,3,7,8]
target = 10
hash_map = {}

for i,v in enumerate(nums):
    if target-v in hash_map:
        print(f"Target found at index {hash_map[target-v],i}")
    else:
        hash_map[v]=i

print(hash_map)

#fast lookup O(1) since keys are hashed
#insertion& deletion : O(1)
#space complexity : O(n)
