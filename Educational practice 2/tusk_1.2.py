arr =  [10,1,2,7,6,1,4]
target = 8
arr.sort()
res = []
curr = []
def findComb(arr, index, target, curr, res):
    if target == 0:
        res.append(list(curr))
        return
    if target < 0 or index >= len(arr):
        return
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i - 1]:
            continue
        curr.append(arr[i])
        findComb(arr, i + 1, target - arr[i], curr, res)
        curr.pop()
    return res

res = findComb(arr, 0, target, curr, res)
for comb in res:
    print(comb)