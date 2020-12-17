# find whether the given array is monotonic or not

arr = [10, 8, 8, 2]
inc = 0
dec = 0
no = len(arr) - 1

for i in range(0, len(arr) - 1):
    if arr[i] > arr[i + 1]:
        dec += 1
        inc = 0
    elif arr[i] < arr[i + 1]:
        inc += 1
        dec = 0
    else:
        inc += 1
        dec += 1

if inc == no and dec == 0:
    print("Array {} is increasing monotones! ".format(arr))
elif dec == no and inc == 0:
    print("Array {} is decreasing monotones! ".format(arr))
else:
    print("Array {} is not monotones! ".format(arr))


# in pythonic way

def check_monoton(l1):
    if all(l1[k] <= l1[k + 1] for k in range(len(l1) - 1)):
        return "Increasing monotones!"
    elif all(l1[k] >= l1[k + 1] for k in range(len(l1) - 1)):
        return "Decreasing monotones!"
    return "Not monotones!"


print(check_monoton(arr))
