# 선형대수(Linear Algebra)

## Elements in Linear Algebra
### Elements in Linear Algebra
- Scalar : 크기만 있고 방향을 가지지 않은 물리량.
- Vector : 크기와 방향을 둘다 가지고 있는 물리량.
- Matrix : 2차원의 숫자 배열 `[[1,6][3,4][5,2]]`
  - Row vector : a horizontal vector
  - Column vector : a vertical vector
  - $A^T$ : Transpose of matrix (전치행렬)
  - `A[i][j]` : (i, j) th component
  - `A[i,]` : i-th row vector
  - `A[,j]` : j-th column vector

### Vector/Matrix Operation
- C = A+B
- ca, cA
- C = AB
  - Matrix 곱은 교환법칙이 성립되지 않음. AB != BA 
- $A(B + C) == AB + AC$ : 분배법칙
- $A(BC) == (AB)C$ : 결합법칙
- $(AB)^T$ == $B^TA^T$ : 전치 성질

- 행렬 곱은 사상의 합성으로 `A하고 B하고 C하는 것은 CBAx 로 표현할 것`

### Linear Equation (선형 방정식)
- $a_1x_1 + a_2x_2 + ... + a_nx_n = b$ 형식으로 만들어진 방정식.
- $a^Tx = b$ 
- 선형 방정식은 Matrix로 표현될 수 있다.
```
A = [[60 5.5 1], [35 5.0 0], [55 6.0 1]]
x = [x, y, z]
b = [66, 74, 78]
```

### Set of Equations (연립 방정식)
- 같은 변수를 포함하는 선형 방정식의 집합.
- Multiple Equations를 Single Matrix Equation으로 바꿀 수 있음.
  -> 어떻게 해결할 것인가? Inversed Matrix 이용.

__Identity Matrix(단위 행렬/항등행렬)__
- diagonal entries가 1이고 나머지가 0인 행렬을 의미함
- ex) `[[1,0,0], [0, 1, 0], [0, 0, 1]]`

__Inverse Matrix__ (역행렬)
- Square Matrix에서 곱했을 때 단위 행렬이 나오는 행렬. $A^{-1}$
- $A^{-1} = {1\over {ad-bc}} \begin{bmatrix}d&-b\\-c&a\\ \end{bmatrix}$

### Non-Invertible Matrix A for Ax=b
- determinant of A, or $det A$ 가 0 이면, Inversed Matrix가 존재하지 않음.
  - det A가 0일 때, 변수가 equation보다 많으면, 무수히 많은 해가 존재한다.
  - det A가 0일 때, equation이 변수보다 많으면, 해가 존재하지 않는다.  
- det A가 0이 아니면, Inversed Matrix를 갖고 있어, 해가 1개 존재한다.

## Linear Combination
- 가중치나 계수와 같이 선형으로 결합된 벡터를 의미.
$c_1v_1 + c_2v_2 + ... + c_pv_p$
- $Ax = b$ __->__ $a_1x_1 + a_2x_2 + a_3x_3 = b$


### Span
- 주어진 벡터로 이루어진 모든 선형 결합의 집합



### Matrix Multiplication

__Linear combinations of Vectors__

__Column Combinations of Vectors__

__Row Combinations of Vectors__

__Sum of Outer Products__





### Linear Independence
- Linearly independent : v1, v2, v3로 표현할 수 있는 solution이 오직 하나
- Linearly dependent : v1, v2, v3로 표현할 수 있는 0을 제외한 여러 solution이 존재하는 경우.
  - dependent한 vector는 span을 증가시키지 않는다.

__SubSpace__
- Span 벡터의 부분집합을 subspace라고 하며, linear combination에 닫혀있다.

__Basis of a SubSpace__
- subspace를 생성하는 기저벡터를 의미함.
  1. Basis는 해당 Subspace를 span해야 한다.
  2. Basis를 이루는 vector들은 서로 Linearly independent해야 한다.

__Dimension of a Subspace__
- subspace를 이루는 basis의 갯수가 dimension이 된다.
- dimension은 unique하다

__Column Space of Matrix__
- column으로 span된 subspace를 의미.
- $\begin{bmatrix}1&1\\1&0\\0&1\\ \end{bmatrix}$ -> Col A = Span {$\begin{bmatrix}1\\1\\0\\ \end{bmatrix} \begin{bmatrix}1\\0\\1\\ \end{bmatrix}$}

__Rank of Matrix__
- dimension of the column space of A
