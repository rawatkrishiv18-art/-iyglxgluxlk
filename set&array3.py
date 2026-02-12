import array as arr

arr_num = arr.array('i',[1,3,5,7,9,3])
print("origional array:", str(arr_num))

print("number of occurrences of the number 3 in the said array:" +str(arr_num.count(3)))

arr_num.reverse()
print("reversed array:")
print(arr_num)