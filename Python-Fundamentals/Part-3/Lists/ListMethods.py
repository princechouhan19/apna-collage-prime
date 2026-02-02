# .append()  - add one element at end
# .insert(idx,val)   - insert element at idx
# .sort()   - arranges in increasing order 
# .reverse()  - reverse order

nums = [1,21,3,46,5,60,7,8,]

nums.append(9)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

nums.insert(2,2.5)
print(nums)

nums.sort() #[1, 2.5, 3, 5, 7, 8, 9, 21, 46, 60]
print(nums) 

nums.sort(reverse=True)#[60, 46, 21, 9, 8, 7, 5, 3, 2.5, 1]
print(nums) 

nums.reverse() #[1, 2.5, 3, 5, 7, 8, 9, 21, 46, 60]
print(nums)