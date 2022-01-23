def pairs(k, arr):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if((arr[j] - arr[i]) == k):
                count = count + 1
            elif((arr[j] - arr[i]) < k):
                continue
            else:
                break

    return count


if __name__ == "main":
    n, k = input("enter here").split()
    n = int(n)
    k = int(k)
    arr = [0 for i in range(n)]
    for i in range(n):
        arr[i] = int(input())
    pairs(k, arr)
