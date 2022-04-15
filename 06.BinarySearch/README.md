# 이분탐색 (Binary Search)

이진 검색 알고리즘(binary search algorithm)은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다. 처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식을 채택하고 있다. 처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최댓값이 되며, 작으면 그 값은 새로운 최솟값이 된다. 검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만, 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.

[나무 자르기](https://www.acmicpc.net/problem/2805)

### psuedo code (의사코드)
```
BinarySearch(A[0..N-1], value, low, high) {
  if (high < low)
    return -1 // not found
  mid = (low + high) / 2
  if (A[mid] > value)
    return BinarySearch(A, value, low, mid-1)
  else if (A[mid] < value)
    return BinarySearch(A, value, mid+1, high)
  else
    return mid // found
}
```

### python 코드
```
def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) / 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid
```


# 투포인터 (Two Pointer)

[수들의 합2 문제 링크](https://www.acmicpc.net/problem/2003)

시간제한이 0.5초인걸 보면 n^2으로는 해결할 수 없음

### 알고리즘 동작 순서
1. 현재 부분합이 M 이상이거나, 이미 e = N이면 s++
2. 그렇지 않다면 e++
3. 현재 부분합이 M과 같으면 결과++

```
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
```

# 인덱스 트리(세그먼트 트리)

[구간 합 구하기4](https://www.acmicpc.net/problem/11659)