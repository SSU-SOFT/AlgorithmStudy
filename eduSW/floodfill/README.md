# FloodFill
- 특정 지점을 기준으로 홍수가 범람(flood fill)하듯 인접한 정보들을 찾아가는 Algorithm
- 응용 사례
    - 그림판의 `채우기`(paint bucket) 기능
    - 게임 `뿌요뿌요`에서 4개 이상의 같은 색 `뿌요`의 연결 판정
- 구현 방법
    - 재귀적 방법 (DFS) / Queue 기반의 구현 (BFS) 방식 사용
    -> 구현 심플 but, Stack Overflow 발생가능 -> C/C++ stack이 1MB 만번정도 중찹가능</br>
    -> Java 는 BFS로 구현. </br>

- 표시, 개수 파악
