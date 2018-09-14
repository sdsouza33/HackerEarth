n = int(input())             # Number of elements of array
array = [int(i) for i in input().split()]
def compare(array,val):
    return (all(val>=x for x in array))
a_1=array[:]           
for i in a_1:
    array.pop(0)
    if compare(array,i):
        print(i,end=" ")
