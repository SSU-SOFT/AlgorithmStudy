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

## Conditional & Loop

### Condition
: 특정 조건이 만족될 경우 실행할 문항을 설정. 들여쓰기와 :으로 구문을 구분.


## Function

- global : 최상위 변수 사용 선언
- nonlocal : 직상위 변수 사용 선언

### variable capture
- 몇몇 다른 프로그래밍 언어에서, 함수 안의 지역 변수들은 그 함수가 처리되는 동안에만 존재하게 되는데, Python, js의 경우 함수를 리턴하고, 리턴하는 함수가 closure를 형성하여 variable을 capture할 수 있는 것이다.

```
def print_closure_factory(number):
    def print_closure():
        print(number)

    return print_closure

print_5 = print_closure_factory(5)
print_10 = print_closure_factory(10)

number += 10
print_5() -> 5
print_10() -> 10
```

- 파이썬에서 Closure는 Factory 형식으로 사용.
- 파이썬에서는 함수도 일반 객체(일급 객체)이다.
    - 변수로 할당 가능 -> Argument & Return 가능.

__Closure Example__
```
def add(var):
    return var + 2
def multiply(var):
    return var * 2

def factory(function, n):
    def closure(var):
        for _ in range(n):
            var = function(var)
        return var
    return closure

print(factory(add, 4)(10)) -> 18
print(factory(multiply, 4)(3)) -> 48
```

### Decolator
- 함수 하나를 인자로 받아 같은 형태의 함수를 반환하는 함수. 
- @을 사용하여 함수를 꾸미는데 사용 가능
- Class를 사용할 시 Decorator에 인자 추가로 가능.
- Decolator에 인자를 넣고 싶은 경우에는 새로운 factory를 추가하면 된다.(한번 더 wrapping) 필요.
- 함수를 Wrapping하기 때문에 기존 함수에 접근 불가
    - Docstring 함수 이름 등 기존 함수의 특성을 가져올 필요가 있음.
    - functools 라이브러리의 wraps 데코레이터 사용.
    - torch를 사용할 때 사용.

### 재귀함수
- 자기 자신을 호출하여 반복적으로 수행.
- 수학의 점화식과 동일
- 재귀함수와 반복문은 수학적으로 동치(서로 변환 가능)

### Variable Length Parameter in Function
- 인자 개수가 정해져 있지 않다면..?
- *(Asterisk)를 사용하여 남은 여러 인자를 Packing 가능. `a, *b, c = [1,2,3,4,5]`
- 가변 인자는 맨 마지막에 단 한 개만 위치 가능.
```
def add_all(a, b, *args):
    print(args) # (3,4,5)
    sum = 0
    for elem in args:
        sum += elem
    return a + b + sum

print(add_all(1,2,3,4,5))
```

### Keyword Variable Length Parameter
- 명시적으로 지정된 파라미터가 남는다면? -> 키워드 가변인자
- ** (Double asterisk)를 사용하여 남은 키워드 변수를 dict 형태로 packing

```
def print_args(a, *args, **kwargs):
    print(args, kwargs)

print(print_args(1, 2, 3, var1=100, var2=200))
```
- 파라미터 순서 : 일반 인자 -> 기본값 인자 -> 가변인자 -> 키워드 가변인자
```
def print_args(var1, var2=10, *args, **kwargs):
    print(var1, var2=10, args, kwargs)

print_args(1,2, 3, var3=10)
```

### Unpacking
- 리스트에, 튜플에 적용가능.
```
def function(a, b, c):
    print(a, b, c)
l = [1,2,3]
function(*l)
```
- Dictionary에 **을 붙이면 Keyword unpacking.
```
def function(var1, var2, **kwargs):
    print(var1, var2, kwargs)
d = {
    'var1' : 10,
    'var2' : 20,
    'var3' : 30,
}

function (**d)
```

### Type hints
- 파이썬은 동적 타이핑 이지만 다소 interface를 알기 어려움. 가독성의 큰 문제.
- 함수에 타입 흰트 제공이 가능. `[function]([var]:[type], ...)` 의 형태
```
def multiply_text(text:str, n: int)-> str:
    return text * n
```
- 그러나 딱히 타입을 안맞춰도 에러가 안 남. 사람을 위한 용도이다.

## Pythonic Programming
- 더 Python 스럽게 프로그래밍 하는 것이 중요.

### Comprehension
- List, Dictionary 등을 빠르게 만드는 기법.
    - for + append 보다 속도 빠름.
```
result = [i*2 for i in range(10)]
result = {str(i):i for i in range(10)}
result = {str(i) for i in range(10)}
```
- if 문을 마지막에 달아 원하는 요소만 추가 가능
```
evens = [i for i in range(100) if i % 2 == 0]
```
- 겹 for 문 사용 가능
```
result = [(i, j) for i in range(5) for j in range(i)]
```
- 다차원 배열 만들기가 유용.
```
eye = [[int(i==j) for j in range(5)] for i in range(5)]
```

### Generator
```
def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1

for i in my_range(5):
    print(i)
```
- range 함수의 경우 숫자를 하나씩 생성하여 반환
    - 이러한 요소를 하나씩 생성해서 반환하는 객체.
- function에 yield를 사용할 시 Generator가 됨.
- yield 하는 위치에서 값을 반환.
- 다시 값을 요청 받을 시 yield 다음 줄 부터 실행
- Return이나 마지막에 온 경우 반복을 멈춤.
- Sequence 전체를 생성하는 것이 아니므로 메모리 효율적.
    - 매우 큰 데이터 셋을 처리할 땐 Generator 사용 권장.
- 괄호로 Generator Comprehension 형태로 선언 가능.
    - Function 등으로 이미 괄호 쳐져 있다면 괄호 생략 가능.
```
even_generator = (i * 2 for i in range(100))
```

### Built-in Functions
- __sum__
- __any, all__ : 하나라도 참 / 모두 참
- __max, min__ : 가장 큰 값 / 가장 작은 값

__zip__
2개 이상의 순환 가능한 객체를 앞에서부터 한번에 접근할 때 사용.
    - tuple로 반환
    - zip에서 길이가 안맞는 부분은 버린다.
```
arr= [[1,2,3], [4,5,6], [7,8,9]]
for row in array:
    print(row)

for col in zip(*array): # 열단위 접근
    print(col)
```

> seq2 = zip(*seq1)의 역연산은 seq1 = zip(*seq2) 이다. Transpose 하는 것

__enumerate__
- For문이 Sequence를 돌 때 그 index가 필요한 때 사용.
- zip과 enumerate를 동시에 사용하는 등 여러 Generator를 한번에 사용.
```
seq1 = ['This', 'sentence']
seq2 = [True, False]

for i, (a, b) in enmerate(zip(seq1, seq2))
    print(i, a, b)
```
- Generator는 List 형태로 출력하기 위해선 list로 변환 필요.

__Lambda Function__
- 함수의 이름 없이 빠르게 만들어 쓸 수 있는 익명 함수.
- 수학에서의 람다 대수에서 유래.
```
def add(a,b):
    return a + b
-> 
add = lambda a, b: a+b
```
- 여러줄을 쓸 수 없음. 공식적으로는 lambda의 사용을 권장하지 않음, 그러나 많이 씀.
    - 문서화 지원 미비
    - 이름이 존재하지 않는 함수 생성
    - 복잡한 함수 lambda로 작성할 시 가독성 하락.

__map__
- 각 요소에 function 함수를 적용하여 반환

__filter__
- 각 요소에 function 함수를 적용하여 참이 나오는 것만 반환