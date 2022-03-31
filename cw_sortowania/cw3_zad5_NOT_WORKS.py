'''Zad5.
Proszę przedstawić W jaki sposób zrealizować strukturę danych, która pozwala wykonywać
operacje:
1. Insert
2. RemoveMin
3. RemoveMax
tak, żeby wszystkie operacje działały w czasie O(log n).

Mamy dwa kopce MIN i MAX, które równiez balansujemy jak w zad6. tyle, że tym razem w MAX sa największe elementy, a w MIN najmniejsze
Operacje 2 i 3 to po prostu usunięcie korzeni i naprawienie kopca, insert to wstawienie do odp kopca, największa trudnosc to ich balanasowanie
Podobny pomysł wykorzystuje zadanie 6 więc sprobuje przeniesc to rozwiązanie takze tu, a to od kolegi z ASD załaączę w komentarzu'''


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i -1) // 2


def heapify_min(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] < T[m]:
        m = l
    if r < n and T[r] < T[m]:
        m = r

    if m != i:
        T[i],T[m] = T[m], T[i]
        heapify_min(T,n,m)


def buildheap_min(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):
        heapify_min(T,n,i)


def reverse_heapify_min(T, i):
    p = parent(i)
    m = i
    #print(p)
    if p >= 0 and T[p] > T[i]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_min(T,m)


def insert_to_heap_min(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_min(T,n -1)


def heapify_max(T,n,i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
        m = r

    if m != i:
        T[i],T[m] = T[m], T[i]
        heapify_max(T,n,m)


def buildheap_max(T):
    n = len(T)
    for i in range(parent(n - 1), - 1, -1):
        heapify_max(T,n,i)


def reverse_heapify_max(T, i):
    p = parent(i)
    m = i
    if p >= 0 and T[p] < T[i]:
        m = p

    if m != i:
        T[m], T[i] = T[i], T[m]
        reverse_heapify_max(T,m)


def insert_to_heap_max(T,el):
    T += [el]
    n = len(T)
    reverse_heapify_max(T,n-1)


def balance(min_heap, max_heap):
    if abs(len(min_heap) - len(max_heap)) <= 1:
        return min_heap, max_heap
    elif len(min_heap) > len(max_heap):
        #print("w balance")
        #print(min_heap)
        insert_to_heap_max(max_heap,min_heap[len(min_heap) - 1])
        min_heap = min_heap[:-1] #uznajmy za O(1) - ooo mona napisac pop i chuj i kozak
        reverse_heapify_min(min_heap, len(min_heap) - 1)
        #print(min_heap)
        #print(max_heap)
        return min_heap, max_heap
    else:
        insert_to_heap_min(min_heap,max_heap[len(max_heap) - 1])
        max_heap = max_heap[:-1]
        reverse_heapify_max(max_heap, len(max_heap)-1)
        return min_heap, max_heap


def remove_max(max_heap):
    print(max_heap[0])
    max_heap[0] = max_heap[len(max_heap)-1]
    max_heap = max_heap[:-1]
    heapify_max(max_heap, len(max_heap),0)
    return max_heap


def remove_min(min_heap):
    print(min_heap[0])
    min_heap[0] = min_heap[len(min_heap)-1]
    min_heap = min_heap[:-1]
    heapify_min(min_heap, len(min_heap),0)
    return min_heap


def controller(T):
    min_heap, max_heap = [], []
    n = len(T)
    for i in range(n):
        if len(min_heap) == 0 or T[i] < min_heap[len(min_heap) -1]:
            insert_to_heap_min(min_heap,T[i])
        else:
            insert_to_heap_max(max_heap, T[i])

        #print('before balance')
        #print('min:', min_heap)
        #print("max:", max_heap)
        min_heap, max_heap = balance(min_heap,max_heap)
        #print("after balance")
        #print('min:',min_heap)
        #print("max:",max_heap)
        #print(".....")


    print("-----")
    print('min:',min_heap)
    print("max:",max_heap)
    while len(min_heap) != 0 and len(max_heap) != 0:
        max_heap = remove_max(max_heap)
        min_heap, max_heap = balance(min_heap, max_heap)
        '''print("After remove max and balance")
        print('min:',min_heap)
        print("max:",max_heap)'''

    if len(min_heap) != 0:
        print(min_heap[0])

    if len(max_heap) != 0:
        print(max_heap[0])

    return


test = [7,5,1,8,3,1,2,4,5,6,3,9]

#import random
#test2 = random.sample(range(0,100),88)
#controller(test2)

'''def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def heapifyMin(A, i):
    l = left(i)
    r = right(i)
    size = A[0]
    if l <= size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        heapifyMax(A, smallest)


def heapifyMax(A, i):
    l = left(i)
    r = right(i)
    size = A[0]
    if l <= size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapifyMax(A, largest)


def balanceHeaps(minHeap, maxHeap):
    if abs(minHeap[0] - maxHeap[0]) <= 1:
        return
    elif maxHeap[0] > minHeap[0]:
        insertMin(minHeap, maxHeap[1])
        size = maxHeap[0]
        maxHeap[1] = maxHeap[size]
        maxHeap[0] -= 1
        maxHeap.pop()
        heapifyMax(maxHeap, 1)
    else:
        insertMax(maxHeap, minHeap[1])
        size = minHeap[0]
        minHeap[1] = minHeap[size]
        minHeap[0] -= 1
        minHeap.pop()
        heapifyMin(minHeap, 1)


def insertMin(minHeap, val):
    minHeap[0] += 1
    minHeap.append(val)
    i = minHeap[0]
    while i > 1 and minHeap[i] < minHeap[parent(i)]:
        minHeap[i], minHeap[parent(i)] = minHeap[parent(i)], minHeap[i]
        i = parent(i)


def insertMax(maxHeap, val):
    maxHeap[0] += 1
    maxHeap.append(val)
    i = maxHeap[0]
    while i > 1 and maxHeap[i] > maxHeap[parent(i)]:
        maxHeap[i], maxHeap[parent(i)] = maxHeap[parent(i)], maxHeap[i]
        i = parent(i)


def getMedian(maxHeap, minHeap):
    if maxHeap[0] == 0 and minHeap[0] == 0:
        return 0
    elif maxHeap[0] == minHeap[0]:
        return (minHeap[1] + maxHeap[1]) / 2
    elif maxHeap[0] > minHeap[0]:
        return maxHeap[1]
    else:
        return minHeap[1]


def insert(minHeap, maxHeap, val):
    median = getMedian(maxHeap, minHeap)

    if val > median:
        insertMin(minHeap, val)
    else:
        insertMax(maxHeap, val)
    balanceHeaps(minHeap, maxHeap)


if __name__ == '__main__':
    maxHeap = [0]
    minHeap = [0]

    insert(minHeap, maxHeap, 1)
    insert(minHeap, maxHeap, 2)
    insert(minHeap, maxHeap, 3)
    insert(minHeap, maxHeap, 4)
    insert(minHeap, maxHeap, 5)
    insert(minHeap, maxHeap, 6)
    insert(minHeap, maxHeap, 7)
    insert(minHeap, maxHeap, 8)
    insert(minHeap, maxHeap, 9)
    insert(minHeap, maxHeap, 10)

    print(getMedian(maxHeap, minHeap))'''