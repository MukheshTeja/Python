array = []
for i in range(1, 27):
    str = ''
    for j in range(i):
        str += chr(96 + i)  # Append the character corresponding to the current 'i'
    array.append(str)  # Append the string 'str' to the array

print(array)
