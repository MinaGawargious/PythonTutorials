my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#		 -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list)
print(my_list[0:6]) # 0-5
print(my_list[:6]) # 0-5. Leaving out start index defaults to 0
print(my_list[3:6]) # 3-5
print(my_list[-7:6]) # 3-5, same as above
print(my_list[3:-4]) # 3-5, same as above
print(my_list[1:10]) # 1-9
print(my_list[1:]) # 1-9. Leaving out end index defaults to len(list)
# print(my_list[-11]) # error
print(my_list[-15:-11]) # Neither index in list, but with slicing, this is not an error
print(my_list[-15:-7]) # Negative number beyond list makes it start at 0

print(my_list[2:9:2]) # 2, 4, 6, 8. 
print(my_list[2:9:2]) # 2, 4, 6, 8. Left out end so default to n (10)

print(my_list[2:9:-1]) # Empty. We try to go 2-8 inclusive, but going backwards, it has no way to get there
print(my_list[9:2:-1]) # 9 to 3 inclusive, going backwards. Now we can get there
print(my_list[9:2]) # 9 to 3 inclusive, going forwards now. Error again

print(my_list[::-1]) # entire list reversed

print(my_list[:6] + my_list[6:]) # end index being non inclusive means my_list[:a] + my_list[a:] always = my_list