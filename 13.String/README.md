# String

## Python String

### 파이썬 String의 특징
- 원시 자료형이자, 불변 타입이다.
- 큰 따옴표 " 혹은 작은 따옴표 ' 로 표기된다.
- 따옴표를 3개 연달아 쓰면 여러줄을 넣을 수 있다.
    - """text""", '''여러줄 적기'''
- Indexing 밑 Slicing이 가능하다.
- 덧셈 및 곱셈이 가능하다
- in & not in 연산이 가능하다.
    - tuple과 다르게 작동. 문자열간의 포함관계를 체크
- Unicode로 처리된다.

__Escape 문자__
|문자|설명|
|---|---|
|\ [Enter] |다음 줄과 연속임을 표현|
|\\|\문자|
|\'|'문자|
|\"|"문자|
|\b|백스페이스|
|\n|줄 바꾸기|
|\t|TAB키|
|\e|ESC키|
-> repr(str) : 원본 객체를 복구할 수 있게 하는 것이 원칙
### Raw String
: `r"<TEXT>"`형태로 \를 무시하고 문자 그대로 취급 가능. 주로 정규 표현식에서 사용.

### String Functions
- len(string) : 문자 개수 반환
- string.upper() : 대문자로 변환
- string.lower() : 소문자로 변환
- string.capitalize() : 문자열 시작 문자를 대문자로 변환
- string.title() : 단어 시작을 대문자로 변환
- string.strip() : 좌우 공백 제거
- string.lstrip(), string.rstrip() : 왼쪽, 오른쪽 공백 제거
- string.isdigit() : 숫자 형태인지 확인
- string.isupper() : 대문자로만 이루어져 있는지 확인
- string.islower() : 소문자로만 이루어져 있는지 확인

### String Pattern Matching
- string.count(pattern) : 문자열 string 내에 pattern 등장 횟수 반환
- string.find(pattern) : 첫 등장 위치 반환(앞에서)
- string.rfind(pattern) : 첫 등장 위치 반환(뒤에서)
- string.startswith(pattern) : 문자열 string이 pattern으로 시작하는지 확인
- string.endswith(pattern) : 문자열 string이 pattern으로 끝나는지 확인

### String Split & Join
- string.split() : 공백을 기준으로 문자열 나누기
- string.split(pattern) : Pattern을 기준으로 문자열 나누기
- string.join(iterable) : String을 중간에 두고 iterable 원소들 합치기

### String Formatting
- Print등을 할 때 보기 좋게 값들을 확인하고 싶은 경우
- + 를 써서 구현은 할 수 있지만 formatting 방식을 사용

__%-formating__
- `"%datatype"%variables` 형태로 표현
- c나 Java에서 주로 쓰이는 방식
```
>>> "Art:%5d, Price per Unit:%8.2f" % (453, 59.058)"
Art:  453, Price per Unit:   59.06
```
> Padding
`"%[padding]datatype"`형태로 패딩 가능
`"%[padding].[precision]datatype"` 형태로 정확도 지정

__String.format Method__
- `"{0}.format(variables)"` 형태로 표현
- 순서와 패딩 설정이 가능.
```
"Art : {0:5d}, Price per Unit:{1:8.2f}".format(453, 59.058)
```

> Naming : 순서가 헷갈리지 않게 각 위치에 이름을 붙이는 방식
`%([name])format`형태 -> %-formatting
`%{[name]:format}`형태 -> String.format Method

__F-string__ -> Pythonic 함
- `f"{variable}"`형태로 표현
- Python 3.6 이상부터 지원
- 변수 위치에 원하는 변수를 위치하면 됨.
```
f"{a} : {b} - {c}"
f"{value*10:8.3f}+{value:8.3f}+{value/10:8.3f}"
```

## Finding Patterns
> 야 이거 #%이름#거 아니냐?
#%이름#에게 물어봐봐
#%이모티콘#

문자열에서 #%SOMETHING#을 찾거나 치환할 수 있는 방법은?
- Find 메소드는 정확히 일치하는 문자열만 찾을 수 있음.
- 문자열에서 특정한 패턴을 정의하고 찾는 방법이 필요.
-> 정규 표현식을 사용

## Regular Expression (정규표현식)
- 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
- 많은 텍스트 편집기와 프로그래밍 언어에서 문자열 검색과 치환에 활용.
- Stephen Cole Kleene가 만듦
- 문법이 매우 방대하기에 연습장을 활용할 것 (https://www.regexr.com/)

1. 일반 텍스트 패턴
    - 정확히 일치되는 문자열 찾음.
    - find와 동일
2. 특수 문자
    - 정규식에서만 쓰이는 문자
    - 공백, 영단어 등
    - 일반 문자와 섞어 씀.
3. 메타 문자
    - 정규식의 문법적인 요소를 담당하는 문자
    - `. ^ $ * + ? { } [ ] \ | ( )`
    - 해당 문자는 특수한 의미의 문자이므로 그대로 매칭하고 싶으면 Escape문자를 붙여 사용.

- 문자 클래스 [] 
    - [와 ] 사이의 문자들 중 하나와 매칭
    - "-"를 사용하여 범위를 지정 가능
    - [a-z] [A-Z0-9] [\d\s]
- 부정 [^ ]
    - [^ 와] 사이의 없는 문자를 매칭
    - "-"를 사용하여 범위를 지정 가능
    - [^a-z] [^A-Z0-9] [^\s]

__Repetition__

- 문자 .
    - 아무 문자나 하나를 매칭
    - 줄 바꿈 문자 \n는 제외
- 0회 이상 *
    - 앞의 문자를 0개 이상 포함
- 1회 이상 +
    - 앞의 문자를 1개 이상 포함
- 0 또는 1회 ?
    - 앞의 문자가 없을 수도 있음.
- 반복 횟수 지정 {m,n}
    - m번 이상 n번 이하 반복.
    - 숫자가 하나만 주어졌을 경우
        -> {m} m번 반복
        -> {m,} m번 이상 반복
        -> {,n} n번 이하 반복

> 전화번호 점화식 : 0\d{1,2}-\d{3,4}-\d{4}
IP : \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

- Lazy Matching ?
    - *+{}와 같은 반복 연산은 최대한 길게 반복되기 때문에 최대한 짧게 매칭하기 위해서 ?를 삽입
    - 어떤 글자가 없는것을 검색하는 것이 더 옮바름.

__Boundary__
- 선택 | : 여러 식 중 하나를 선택
- 단어 경계 \b : 단어의 경계 지점인지 확인
- 줄의 시작 ^ : 줄이나 문자열의 시작점으로 Multiline flag 필요.
- 줄의 끝 $ : 줄이나 문자열의 끝. Multiline flat 필요.

__Capture__
- 그룹 캡쳐 ()
    - 괄호이므로 우선 순위가 있음.
    - 해당 문자열을 캡쳐한다.
    - 캡쳐된 텍스트를 불러올 수 있다.
        - \1, \2, \3, ... \ [number]
- 비 그룹 캡쳐 (?:)
    - 괄호이므로 우선 순위가 있음
    - 캡쳐를 하지는 않는다
    - 그냥 괄호다

__Condition__
- 뒷 패턴 확인 D(?=R)
    - R이 바로 뒤에 있는 D를 매칭
    - R 부분은 포함되지 않음.
/`\w+(?=ism)`/gm -> __tour__ ism

- 앞 패턴 확인 (?<=R)D
    - R이 바로 앞에 있는 D를 매칭
    - R 부분은 포함되지 않음.

## Python in regex
- 파이썬 표준 re 패키지를 사용.

탐색 - search
모두 탐색 - finditer
치환 - sub
나누기 - split

- 정규 표현식을 평가하는 것은 오래걸림 
-> 반복적으로 정규표현식을 사용한다면 미리 컴파일하여 사용하는 것이 빠름.(parsing 과정이 빠짐)

```
for string in dataset:
    match = re.search(pattern, string, re.MULTILINE)
    print(match.group(0))
```

```
compiled = re.compile(pattern, flags=re.MULTILINE)
for string in dataset:
    match = compiled.search(string)
    print(match.group(0))
```
