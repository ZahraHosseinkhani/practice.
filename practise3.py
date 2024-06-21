def heap(A, num , i):
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2

    if left < num   and   A[left] > A[largest] :
        largest = left

    if right < num  and  A[right] > A[largest] :
        largest = right

    if largest != i :
        A[i], A[largest] = A[largest], A[i]
        heap(A, num , largest)


def heap_sort (A) :
    num = len(A)

    for i in range(num // 2 - 1 , -1 , -1) :                     # maxheap
        heap(A , num , i)

   
    for i in range (num-1 , 0 , -1) :                           # Extract elements one by one
        A[0], A[i] =A[i],A[0]
        heap(A, i, 0)


A = [8, 596, 0, 56, 99, 3]                                      # Input A of numbers
heap_sort(A)

print("Sorted array is:")
for i in range ( len(A) ) :
    print(A[i])

