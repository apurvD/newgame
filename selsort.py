A = []
n=int(input("Enter the number of elements to be sorted:"))

for temp in range(n):
    A.append(int(input("Enter element ")))

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[min_idx],A[i] = A[i],A[min_idx]
    
print ("Sorted array : ")
for i in range(len(A)):
    print(A[i],end=" ")
