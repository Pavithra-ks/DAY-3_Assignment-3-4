# Write a program to implement insertion sort

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

n = int(input('enter numbeer of element : '))
arr = []
for i in range(0,n):
    element = int(input())
    arr.append(element)

print(f'list you entered is {arr}')
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])