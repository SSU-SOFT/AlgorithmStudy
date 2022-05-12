def pprint(arr):
    for line in arr:
        print(line)

def Rotate(arr):
    row = len(arr)
    col = len(arr[0])
    tmp = 0
    
    # Top
    tmp1 = arr[0][col-1]
    for i in range(1, col):
        arr[0][col-i] = arr[0][col-i-1]
    arr[0][0] = arr[1][0]
    
    # Right
    tmp2 = arr[row-1][col-1]
    for i in range(1, row):
        arr[row-i][col-1] = arr[row-i-1][col-1]
    arr[1][col-1] = tmp1
    
    #Bottom
    tmp1 = arr[row-1][0]
    for i in range(col-1):
        arr[row-1][i] = arr[row-1][i+1]
    arr[row-1][col-2] = tmp2
    
    # Left
    for i in range(row-1):
        arr[i][0] = arr[i+1][0]
    arr[row-2][0] = tmp1
    # pprint(arr)

    return arr

def ShiftRow(arr):
    last = arr.pop()
    arr = [last, *arr]
    return arr
    
def solution(rc, operations):
    answer = [[]]
    oper = {'Rotate' : Rotate, 'ShiftRow' : ShiftRow}
    for operation in operations:
        rc = oper[operation](rc)
    return rc

