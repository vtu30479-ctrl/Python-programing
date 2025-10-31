def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def find_sequence(arr):
    smallest = arr[0]
    largest = arr[-1]
    print("Sequence of integers:", smallest, "to", largest)

n = int(input("Enter the number of integers: "))
integers = []

print("Enter the integers:")
for _ in range(n):
    integers.append(int(input()))

bubble_sort(integers)   
find_sequence(integers)  
