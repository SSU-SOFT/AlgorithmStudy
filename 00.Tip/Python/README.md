# Python(파이썬)

## Overview
1989년 크리스마스에 연구실이 닫혀있어 심심해서 프로그래밍 언어를 만듦. 영국 코미디 그룹 몬티 파이썬에서 이름을 땀.

## Features of Python
- 플랫폼 독립적인 인터프리터 언어
: 코드와 인터프리터만 있으면 윈도우, 안드로이드, ios등 어디에 있던 실행 가능.
- 완전 객체 지향 언어
: 모든 것이 객체이다.
- 동적 타이핑 언어
: 코드를 실행하던 중에 타이핑하며, 덕 타이핑 기능에 따라 타이핑함(?)

- 쉬운 문법 & 다양한 기능 -> 높은 생산성
- 다양한 라이브러리
    - 쉬운 라이브러리 설치 및 관리
    - 수많은 사람들이 다양한 라이브러리에 기여 및 공개
- 널리 쓰임 -> 구글링으로 대부분의 문제를 해결 가능.

> Jupyter Notebook
: 파이썬의 기본 실행 환경은 Interactive Shell 이지만, 일반적으로 .py파일로 실행하기 때문에 Interactive 하지 않다. 이를 살리기 위한 Ipython 커널을 기반으로한 Interactive 파이썬 셀 프로그래밍이다.

## 변수(Variable)
: 값을 저장하는 공간 = 연산자로 대입 연산

### 파이썬 변수의 특징
- 모든 변수는 메모리 주소를 가르킴(모든 것은 포인터)
- 변수명 <- 일종의 이름표
    - 선언한 변수에 특정 공간이 생기는 개념이 아님.
    - 필요하면 공간을 만들고 변수명을 붙이는 격.
- 알파벳, 숫자, 언더스코어로 선언.
- 변수명은 가독성을 중요시하고 대소문자가 구분된다.
- 변수명으로 쓸 수 없는 예약어가 존재함.
- C와 달리 대입연산이 딱히 반환값을 가지지 않음.
- 연속해서 대입 가능.(뒤에서 부터 대입)
- (:= 연산으로 대입과 동시에 반환 가능)
### 원시 자료형(Primitive Data Type)
: 가장 기본이 되는 자료형
- int, float, complex
- String, bool, None

__불변타입(Immutable Type)이다.__
- 불변타입들은 저장된 값이 변하지 않는다.
- 물리적 메모리 주소를 가르침.
- 원시 자료형과 Tuple을 제외한 다른 모든 파이썬 객체는 모두 가변타입이다.(Mutable Type)

```
>>> a = 10
>>> b = a
>>> a += 1
>>> a, b, a is b
(11, 10, False)

>>> a = [1,2,3]
>>> b = a
>>> a += [4]
>>> a, b ,a is b
([1,2,3,4], [1,2,3,4], True)

>>> a = a + [5]
>>> a, b, a is b
([1,2,3,4,5], [1,2,3,4], False)
```
- 파이썬에서는 적당한 크기의 원시 자료형 대입은 기존 객체를 할당
```
>>> a = 1   #INT는 255를 기준.
>>> b = 1
>>> a is b
True

>>> a = 12345
>>> b = 12345
>>> a is b
False

>>> a = 'text'
>>> b = 'long-long-text'
>>> a is 'text', a=='text', b is 'long-long-text', b == 'long-long-text'
True, True, False, True

a = True
a is True

a = None
a is None # 더 Conventional한 방식
```

__산술연산자()__
- +, -, *, **, /, //, %

__비트연산자(Bit Operators)__
- NOT ~ -> 비트 부정
- OR |  -> 비트 합
- AND & -> 비트 곱
- XOR ^ -> 배타적 비트합
- SHIFT >> << -> 비트 시프트

In-place vs Out-place
```
a += 1
a = a + 1
```

__비교연산자(Condition Operators)__
- <, >, ==, <=, >=
- == : 값이 같다. is : 주소가 같다. != : 값이 다르다. is not 주소가 다르다.
- in : 포함된다. not in : 포함되지 않음.

bool 끼리의 연산을 위해서 논리 연산자를 활용.
- not : 부정
- or : 논리합
- and : 논리곱

python은 비교연산을 한번에 평가하기 때문에 `2 < a < 4` 같은 표현이가능하다.

### Dynamic Typing
: 코드 실행 지점에서 데이터의 타입을 결정함. 따로 데이터 타입을 명시하지 않아도 됨.

__Implicit Type Conversion__
- bool -> int -> float -> complex
- None과 String은 별개
- int 간의 나누기는 float

__Explicit Type Conversion__
:`[Type]([value])`로 명시적 형 변환 가능. Initializer라고 생각하면 좋을 듯.
- int(a), float(text), str(value)
- 적절한 text는 적절한 값으로 변형.
- 실수 -> 정수 : 내림.
    - round : 반올림
- 빈 문자열, 0, None은 False로 변환

__Type Checking__
- type 함수로 변수의 타입 확인 가능
- isinstance 함수로 변수가 지정 타입인지 확인
    - `isinstance([variable], [type])`

## Data Structure

배열 : 일련의 데이터를 하나로 묶음.

List indexing & Sliding

- `seq[index]`형태로 요소 하나 접근
- 0부터 숫자세기 시작
- 음수 가능

- `seq[start:end:step]` 형태로 List 자르기

파이썬에서 제공되는 기능은 일반적으로 `예약어`, `내장함수`, `메소드`의 형태를 지닌다.
예약어 -> 문법
내장함수 -> General Class
메소드 -> 특정 Class

