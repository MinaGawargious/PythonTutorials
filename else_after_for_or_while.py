# obvious:
if 3 < 2:
    print("3 < 2")
else:
    print("3 is not less than 2")

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    # if i == 3: # Causes else statement to not run
    #     break
    if i == 6: # 6 never hit in list, so else still executes
        break
    if i == 3: # Still hits else. Only breaks, not continues, prevent execution
        continue
    print(i)
else: # It should have been named no_break
    print("Hit the For/Else Statement! No break statement hit in for loop")
    

i = 1
while i <= 5:
    print(i)
    # if i == 3: # Causes else statement to not run
    #     break
    i+=1
    if i == 7: # 7 never hit, so else still executes
        break
    if i == 3: # Still hits else. Only breaks, not continues, prevent execution
        continue
else:
    print("Hit the While/Else Statement! No break statement hit in while loop")
    
    
# Practical example:
def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            break
    else: # no break = no find = return -1
        return -1
    return i

def find_index_my_way(to_search, target):
    index = -1
    for i, value in enumerate(to_search):
        if value == target:
            index = i
            break
    return index

my_list = ['Corey', 'Rick', 'John']

print(f"Location of target is index: {find_index(my_list, 'Rick')}")
print(f"Location of target is index: {find_index_my_way(my_list, 'Rick')}")