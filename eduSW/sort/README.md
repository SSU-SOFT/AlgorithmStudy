# Sort
stable - bubble, merge
unstable - quick, simple

stable : 학번순 성적은 성적이 동일할때, 학번 순이 안바뀜.
unstable : 학번 순이 유지가 안될 수 있음. 조건을 추가로 주어 비교하여야 함.

```
#include <stdlib.h>

void qsort(void * b, size_t n, size_t s, int(*c)(const void*, const void*))

//void * b : 정렬하고자 하는 배열의 첫번째 요소의 주소
//size_t n : 요소 개수
//size_t s : 요소 type의 개수 (sizeof())
//int (*c) : 비교 함수.

// 오름차순
int compareMyType (const void * a, const void * b) {
    if (*a < *b) return -1;
    if (*a == *b) return 0;
    if (*a > *b) return 1;
}
// 4Byte 이하 type (long, int, short, char)는 연산만으로 가능
return a - b -> 오름차순
```


