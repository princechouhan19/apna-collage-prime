nums = [1, 2.5, 3, 5, 7, 8, 9, 21, 46, 60]

for i  in nums:
    print(i)

x=9
idx=0
for i in nums:
    idx+=1
    if(i==9):
        print(f"{x} is at index {idx}")
        break