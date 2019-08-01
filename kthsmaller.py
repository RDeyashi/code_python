# Find the Kth smaller element of a list



def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def partition(A, l, r):
    i = l
    pivot = A[r]
    for j in range(l,r):
        if A[j] < pivot:
            swap(A,i,j)
            i += 1
    swap(A,i,r)
    return i

def ksmall(A, l, r, k):
    if k>=0 and k <= r-l+1:
        pos = partition(A, l, r)
        #print(A, l, r)
        #print(pos, k)
        if pos-l == k-1:
            #print("eq")
            return A[pos]
        elif k-1 < pos-l:
            #print("left")
            # Left array
            return ksmall(A, l, pos-1, k)
        # Right array
        #print("right")
        return ksmall(A, pos+1, r, k-1-pos+l)
    
    return 10000


#driver program
T = int(input("\nEnter number of iteration : "))
i = 0
while i<T:
    print("Iteration No #%d:\n"%(i+1))
    ln = int(input("Array Size : "))
    print("Enter %d Elements with <space> : "%ln, end='')
    A = list(map(int, input().split()))[:ln]
    #A = [int(x) for x in A]
    k = int(input("Enter Kth value : "))
    out = ksmall(A, 0, ln-1, k)
    print("Kth Smallest = %d\n"%out)
    i += 1
