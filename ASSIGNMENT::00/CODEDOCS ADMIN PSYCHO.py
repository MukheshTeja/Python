print("codedocs admin psycho")
num_of_elements=int(input("enter the number of elements needed in the array::"))
array=[]
count=0
print("enter the elements into the array::")
for i in range(num_of_elements):
    inpt=int(input("enter the number into the array:->"))
    array.append(inpt)
print(array)
mini=array[0]
n=0
for i in range(num_of_elements):
    min_index = i
    for j in range(i + 1, num_of_elements):
        if array[j] < array[min_index]:
            min_index = j
    if min_index != i:
        array[i],array[min_index]=array[min_index],array[i]
        count+=1
print("the number of times the swap occurs",count)
print(array)
