### Immutable vs mutable
: 객체 지향 프로그래밍에 있어서 immutable object는 생성 후 그 상태를 바꿀 수 없는 객체를 말한다. 반대 개념으로는 mutable object로 생성 후에도 상태를 변경할 수 있다. 대부분의 객체 지향 언어에서 객체는 참조 형태로 전달하고 받기 때문에 참조를 통해 공유돼 있다면 그 상태가 언제든지 변경될 가능성도 커지므로 문제가 된다. 불변 객체는 객체를 복제할 때 객체 전체가 아니라 단순히 참조만 복사하고 끝난다. 참조는 보통 객체 그 자체보다 훨씬 작아서 메모리가 절감되며 프로그램의 성능에도 좋다. 

- Immutable : 숫자(number), 문자열(string), 튜플(tuple)
- Mutable : 리스트(list), 딕셔너리(dictionary), 세트(set)


Python에서 각 자료형마다 특징이 다르기 때문에 잘 알아두는 것이 좋다. 