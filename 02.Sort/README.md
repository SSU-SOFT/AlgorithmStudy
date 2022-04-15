# 정렬 (Sort)
컴퓨터 과학과 수학에서 정렬 알고리즘(sorting algorithm)이란 원소들을 번호순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘이다. 효율적인 정렬은 탐색이나 병합 알고리즘처럼 (정렬된 리스트에서 바르게 동작하는) 다른 알고리즘을 최적화하는 데 중요하다. 또 정렬 알고리즘은 데이터의 정규화나 의미있는 결과물을 생성하는 데 흔히 유용하게 쓰인다. 

이 알고리즘의 결과는 반드시 다음 두 조건을 만족해야 한다.
1. 출력은 비 내림차순(각각의 원소가 전 순서 원소에 비해 이전의 원소보다 작지 않은 순서)이다.
2. 출력은 입력을 재배열하여 만든 순열이다.
## 버블 정렬(Bubble Sort)
---
두 인접한 원소를 검사하여 정렬하는 방법이다. 시간 복잡도가 O(n^2)로 상당히 느리지만, 코드가 단순하기 때문에 자주 사용된다. 원소의 이동이 거품이 수면으로 올라오는 듯한 모습을 보이기 때문에 지어진 이름이다. 양방향으로 번갈아 수행하면 칵테일 정렬이 된다.
<Image src="./images/Bubble_sort_animation.gif">

__시간복잡도__
> 최악 시간복잡도	O(n^{2}) 비교, O(n^{2}) 교환
> 최선 시간복잡도	O(n) 비교, O(1) 교환
> 평균 시간복잡도	O(n^{2}) 비교, O(n^{2}) 교환
> 공간복잡도 O(1) 보조

```
def bubbleSort(arr):
  tmp = 0;
  for i in range(len(arr)):
      for j in range(i, len(arr)):
          if arr[j-1] > arr[j]:
              tmp = arr[j=1];
              arr[j-1] = arr[j]
              arr[j] = tmp
  return arr
```
## 선택 정렬(Select Sort)
### 1. 선택 정렬 과정
  1) 주어진 데어터 중, 최소값(min_idx)을 찾는다.
  2) 최소값을 리스트 맨 앞의 위치한 값과 바꾼다.
  3) 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복한다.

### 2. 선택정렬 예시
<img src="https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png" alt="" width="400" height="550">
  
### 3. 선택정렬 코드
```
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```
                                     
### 4. 알고리즘 분석
- 공간 복잡도 : O(1)
  -> 별도의 추가 공간 사용 X. 주어진 배열 공간 내에서 위치만 바꿈
- 시간 복잡도 : O(N^2)
  -> 이중 for문

  
  
---  
## 삽입 정렬(Insert Sort)

# Insertion Sort 삽입정렬

### summary : 이미 정렬된 array를 유지, 새로운 숫자가 "삽입"되면 정렬된 array 안에서 자기의 자리를 찾아가며 정렬
<br>

## 1. 원리 및 예시
<img src="https://postfiles.pstatic.net/MjAyMTAyMjdfMTg5/MDAxNjE0NDEyNTc2OTQx.aKYInKO1l_GhEyzK2ouylBe7XSSnCiS7kvMjzlXzKs4g.RWahau3NJx-VqWo4_FeSb-XoTjCR6AeXsKeZcdVlfjsg.PNG.comb0703/insertion_sort-recursion.png?type=w773"><br>
이미지 출처 : https://blog.naver.com/comb0703/222258698264
<br>

## 2. 코드 예시 - Python
``` py
def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val
```


## 3. Time Complexity
- O(n^2)
- best : O(n) => 이미 정렬되어 있을 때
- worst : O(n^2) => 역순으로 정렬되어 있을 때
  
## 병합 정렬(Merge Sort)

### 1.병합정렬의 정의

-재귀용법을 활용한 정렬 알고리즘 
  
  1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
  2. 각 부분 리스트를 재귀적으로 합병정렬을 이용해 정렬한다.
  3. 두 부분 리스틀르 다시 하나의 리스트로 합병한다.

---

### 2. 알고리즘의 구성

-병합정렬은 크게 2가지의 부분으로 나눌 수 있다.

  * 1단계 : 정렬되지 않은 배열을 끝까지 분리하는 단계
  * 2단계 : 분리한 데이터를 단계별로 합치는 단계
  
-예시 : 
  1. list[1,9,3,2]가 존재
  2. list를 우선 [1,9] 와 [3,2]로 나눈다. (1단계)
  3. 나눈리스트에서 다시 [1] [9]로 나눈다 (1단계)
  4. [1]과 [9]를 순서에 맞게 다시 합친다.(2단계)
  5. 위에서 구한 리스트 [1,9]를 뒤에서 정렬된 [2,3]과 합친다. -> 앞에서 부터 비교하며 붙여간다. (2단계)
  6. 위의 결과를 실행하여 정렬된 list [1,2,3,9]를 얻을 수 있다.
 
---

### 3. 코드의 구성 

* 재귀가 일어나는 함수 부분

<pre>
<code>
def merge_sort(list):
  if( len(list) <= 1 ) :
    return list
    
  medium = (int)len(list)/2
  
  left = []   <- 함수에 매개변수로 들어온 코드를 slicing을 통해 나누어 준다.
  right = []
  
  left = merge_sort(left)
  right = merge_sort(right) <- 재귀적 부분이 일어나는 부분
  
  return merge( left, right)
</code>
</pre>

* 정렬된 함수를 다시 합치는 부분

<pre>
<code>

def merge( left, right ):
  mergedList = []
  leftPoint = 0
  rightPoint = 0
  
  while ( len(left) > leftPoint && len(right) > rightPoint):
    if (left[leftPoint] > right[rightPoint] ):
      mergedList.append(right[rightPoint])
      rightPoint += 1
    else:
      mergedList.append(left[leftPoint])
      leftPoint += 1
   
   if ( len(right) > rightPoint ):
    나머지 부분 모두 mergedList에 삽입
   elif ( len(left) < leftPoint):
    나머지 부분 모두 mergedList에 삽입

</code>
</pre>

---

### 4.알고리즘 분석 

- 시간 복잡도
  1. 각 단계마다 배열의 길이가 반으로 나누어진다.   
  2. 각 단계마다 하나의 노드의 길이는 n / (2^i) 가 됨을 알 수 있다.
  3. 각 단계에는 2^i의 노드가 들어있다.
  4. 각 단계의 모든 값을 비교하므로 각 단계는 n / (2^i) * 2^i = O(n) 이다.
  5. 단계는 log(n) = O(logn) 만큼 만들어진다.
  6. 따라서 총 시간 복잡도는 O ( n * logn ) 이다.


## 힙 정렬 (Heap Sort)
힙 정렬(Heap sort)이란 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법으로서, 내림차순 정렬을 위해서는 최대 힙을 구성하고 오름차순 정렬을 위해서는 최소 힙을 구성하면 된다.
<Image src="./images/220px-Sorting_heapsort_anim.gif">

### 알고리즘
1. n개의 노드에 대한 완전 이진 트리를 구성한다. 이때 루트 노드부터 부모노드, 왼쪽 자식노드, 오른쪽 자식노드 순으로 구성한다.
2. 최대 힙을 구성한다. 최대 힙이란 부모노드가 자식노드보다 큰 트리를 말하는데, 단말 노드를 자식노드로 가진 부모노드부터 구성하며 아래부터 루트까지 올라오며 순차적으로 만들어 갈 수 있다.
3. 가장 큰 수(루트에 위치)를 가장 작은 수와 교환한다.
4. 2와 3을 반복한다.

__시간복잡도__
> 최악 시간복잡도	O(n log n)
> 최선 시간복잡도	O(n log n)
> 평균 시간복잡도	O(n log n)
> 공간복잡도 O(1)

```
import heapq as hq

arr = list(map(int, input().split(" ")))
hq.heapify(arr)

print(arr)
result = []
while arr:
    result.append(hq.heappop(arr))

print(result)
```

## 퀵 정렬(Quick Sort)
분할 정복 방법을 통해 리스트를 정렬한다. 퀵 정렬은 n개의 데이터를 정렬할 때, 최악의 경우에는 O(n2)번의 비교를 수행하고, 평균적으로 O(n log n)번의 비교를 수행한다.
퀵 정렬의 내부 루프는 대부분의 컴퓨터 아키텍처에서 효율적으로 작동하도록 설계되어 있고(그 이유는 메모리 참조가 지역화되어 있기 때문에 CPU 캐시의 히트율이 높아지기 때문이다.), 대부분의 실질적인 데이터를 정렬할 때 제곱 시간이 걸릴 확률이 거의 없도록 알고리즘을 설계하는 것이 가능하다. 또한 매 단계에서 적어도 1개의 원소가 자기 자리를 찾게 되므로 이후 정렬할 개수가 줄어든다.
5(1), 5(2), 3, 2, 1 를 정렬하면 1, 2, 3, 5(2), 5(1) 이다.
<Image src="./images/220px-Sorting_quicksort_anim.gif">

1. 리스트 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 피벗이라고 한다.
2. 피벗 앞에는 피벗보다 값이 작은 모든 원소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 모든 원소들이 오도록 피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 리스트를 둘로 나누는 것을 분할이라고 한다. 분할을 마친 뒤에 피벗은 더 이상 움직이지 않는다.
3. 분할된 두 개의 작은 리스트에 대해 재귀적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1이 될 때까지 반복된다.

재귀 호출이 한번 진행될 때마다 최소한 하나의 원소는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.

> 최악 시간복잡도	: O(n^{2})
> 최선 시간복잡도	: O(n log n)
> 평균 시간복잡도	: O(n log n)

- __소스코드__ 
```
def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)
```
- __소스코드__ (cache 없이)
```
# 2 8 7 1 3 5 6 4

arr = list(map(int, input().split()))

def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
            print(arr)
        A[left], A[hi] = A[hi], A[left]
        
        return left
    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot-1)
        quicksort(A, pivot+1, hi)
    

quicksort(arr, 0, len(arr)-1)
print(arr)
```

```
[2, 8, 7, 1, 3, 5, 6, 4]
[2, 8, 7, 1, 3, 5, 6, 4]
[2, 8, 7, 1, 3, 5, 6, 4]
[2, 1, 7, 8, 3, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 8, 7, 5, 6, 4]
[2, 1, 3, 4, 7, 5, 6, 8]
[2, 1, 3, 4, 7, 5, 6, 8]
[2, 1, 3, 4, 7, 5, 6, 8]
[1, 2, 3, 4, 7, 5, 6, 8]
[1, 2, 3, 4, 7, 5, 6, 8]
[1, 2, 3, 4, 7, 5, 6, 8]
[1, 2, 3, 4, 7, 5, 6, 8]
[1, 2, 3, 4, 5, 7, 6, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
```
