def copy(T,n):
    New = [None for _ in range(n)]
    for i in range(n):
        New[i] = T[i]
    return New


def merge_sort_launcher(T):

    def merge_sort(T, Backup, l, r):
        if r - l == 1:
            return

        mid = (l + r - 1)//2
        merge_sort(T,Backup, l, mid)
        merge_sort(T, Backup, mid + 1, r)
        merge1(T,Backup,l,r,mid)

    def merge(T, Backup, l, r, mid):
        p,k = l, mid + 1
        for j in range(l,r + 1):
            if p < mid and (k == r + 1 or Backup[p] <= Backup[k]):
                T[j] = Backup[p]
                p += 1

            elif k <= r and Backup[k] < Backup[p]:
                T[j] = Backup[k]
                k += 1

    def merge1(A, B, beg, mid, end):  # merge from arg A to arg B, beg is inclusive, end is exclusive
        j = beg
        k = mid

        for i in range(beg, end):

            if (k == end or A[j][0] <= A[k][0]) and j < mid:
                B[i] = A[j]
                j += 1
            else:
                B[i] = A[k]
                k += 1

    n = len(T)
    Backup = copy(T, n)
    l, r = 0, n - 1
    merge_sort(T, Backup, l, r)



tab = [7, 23, 13, 29, 19, 8, 2, 1, 18, 88, 15, 3, 5, 29, 30, 24]
merge_sort_launcher(tab)
print(tab)