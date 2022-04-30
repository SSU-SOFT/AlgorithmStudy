# 운영체제(Operation System)

### 운영체제란?
> 하드웨어를 효율적이고 손쉽게 사용할 수 있는 Abstraction(추상화)을 제공. 
자원의 공유 및 분배를 위한 Policy를 결정한다. 

|CPU|Memory|Disk|Network|
|-----|----|----|----|
|Process|Address Space|File|Port|

__Abstraction이 필요한 이유__
-  CPU나 메모리, 디스크의 기능이 담긴 바이너리 부분을 서로 어떤 역할을 하는지 구분하기 위한 기능.

1. Process 추상화
Program
    - 컴퓨터를 실행시키기 위한 일련의 `순차적으로 작성된 명령어의 모음`
    - 컴퓨터 시스템의 Disk와 같은 Secondary Storage에 바이너리 형태로 저장되어 있다.
Process
    - 실행되고 있는 프로그램의 추상화
    - Program Counter, Stack, Data Section 으로 구현된다.
    -> CPU와 같은 Hardware Component로 하여금 각 Program을 구분하여 인식/실행할 수 있도록 하기 위함.

2. Abstraction (추상화) : Address Space
- Process가 차지하는 메모리 공간
-> Protection domain : 서로의 주소 공간을 침범할 수 없음. (구분 짓는 것.)
실행 context의 보호 & Privacy Issue 때문
-> (Memory Mapped) I/O Device의 관리 ex) 마우스, 키보드, 모니터…

3. Abstraction (추상화) : File
- Process에서 읽고 쓸 수 있는 Persistent Storage (반영구적인 저장소)
- 실제 저장되는 위치를 Process는 알지 않음.
- 어디까지가 Process의 Binary Data인지, 해당 Binary Data가 어디에 저장되어 있는지 구분하고, 관리/유지 필요.

4. Abstraction (추상화) : Port
- 컴퓨터 시스템이 메시지를 주고 받는 Communication Endpoint
- 어떤 Process (또는 User)사이의 통신인지 구분 필요. (Privacy Issue 포함.)

### Process 처리방식

__Batch System__ (일괄 처리)
- 일단 시작한 job을 끝내야 다음 job이 수행 되는 방식으로 punch card를 제출하면 메모리에 적재, 수행의 순서로 결과를 받기까지 중간에 User Interactino이 불가능함.
- 사람이 Job을 Scheduling함.
- 입출력 하는 동안 CPU는 빈번히 Idle 한 상태로 전환

__Automatic Job Sequencing__
- 사람의 관여 없이 여러개의 프로그램을 순차적으로 실행하여 이전 작업 종료 직후 다음 작업을 실행하기때문에 성능이 향상했지만, I/O에 의해 CPU가 Idle 상태로 전환되는 문제는 해결되지 않음.

__Pooling__
- I/O의 delay로 인한 CPU동작의 비효율을 해결하기 위해 등장하여 I/O와 Compuation을 동시에 진행 할 수 있음.
ex) 프린터 Spooling

__Multiprogramming__ 
:2개 이상의 작업을 동시에 실행. 다음 작업을 실행할 수 있도록 미리 세팅. CPU 활용도를 증가시키나 여전히 실행중인 작업에 대해서는 관여할 수 없음.

__Timesharing__ 
:CPU의 실행 시간을 타임 슬라이스로 나누어 실행. 모든 프로그램은 타임 슬라이스 동안 CPU를 점유하고, 그 시간이 끝나면 CPU를 양보. 여러 개의 작업들이 CPU 스위칭을 통해 동시에 실행됨. CPU 스위칭이 매우 빈번하게 일어남. 
- 사용자는 실행중인 프로그램에 관여가 가능. I/O 사이사이에 들어갈 수 있음.

__Multitasking__
:여러개의 Task들이 CPU와 같은 자원을 공유하는 방법. 하나의 작업은 동시에 실행할 수 있는 Task로 나눠질 수 있음. Multitasking은 사용자가 여러개의 프로그램을 실행할 수 있도록 하며, CPU가 Idle 상태일 때는 Background작업을 실행 가능하도록 함.

> Issue with Multitasking
>- 복잡한 메모리 관리 시스템
>- CPU 스케줄링이 필요.
>- 동기화, Deadlock이 발생

__OS Design Principle__
- Policy : 무엇이 기능하게 할 것인가?
- Mechanism : 무엇을 어떻게 할 것인가?

__Usermode vs Kernel Mode__
:CPU의 2가지 이상의 실행 모드

Kernel Mode
- 모든 권한을 가진 실행 Mode
- 운영체제가 실행되는 Mode
- Privilege 명령어 실행 및 레지스터 접근 가능
:I/O 장치 제어 명령어, Memory Management Register

Usermode
- Kernel Mode에 비해 낮은 권한의 실행 Mode
- 어플리케이션이 실행되는 Mode
- Privilege 명령어 실행 불가능

System Call
- User Mode에서 Kernel Mode로 진입하기 위한 통로 -> Kernel에서 제공하는 Protected 서비스를 이용하기 위해 필요.

__Method for Operating System Design__
__Layering__ : OS의 복잡도를 낮추기 위한 방안으로 위 아래에 인접한 Layer와만 통신하며, 2단계 이상 건너뛴 Layer와 직접적으로 통신하지 않음. Layer들이 서로 독립적이라 설계와 유지보수의 장점이 있음.

-> 설계의 복잡도를 낮출 수 있으나 그로인해 function call이 많아져 Overhead가 발생함.

### Kernel Design
__Monolithic Kernel__
- Kernel의 모든 Service가 같은 주소 공간에 위치.
- 어플리케이션은 자신의 주소 공간에 커널 코드 영역을 맵핑하여 커널 서비스를 이용
- H/W 계층에 관한 단일한 Abstraction을 정의
:이를 사용하기 위해, 라이브러리나 어플리케이션에서 단일한 이터페이스 제공.

장점
- 어플리케이션과 모든 Kernel 서비스가 같은 주소 공간에 위치하여 시스템 콜 및 kernel 서비스 간의 데이터 전달의 Overhead가 적음.

단점
- 모든 서비스 모듈이 하나의 바이너리로 이루어져 있기 때문에 일부분의 수정이 전체에 영향을 미침.
- 각 모듈이 유기적으로 연결되어 있기 때문에 Kernel 크기가 커질수록 유지/보수가 어려움.

__Micro Kernel__
- Kernel Service 를 기능에 따라 모듈화 하며 각각 독립된 주소 공간에서 실행.
- 이러한 모듈을 서버라 하며, 서버들은 독립된 프로세스를 구현.
- 마이크로 커널은 서버들간의 통신(IPC : Inter Process Communicator)
:어플리케이션의 서비스 콜 전달과 같은 단순한 기능만을 제공.

장점
- 각 Kernel 서비스가 따로 구현. 서로간의 의존성 낮음. Kernel의 개발 및 유지 보수가 상대적으로 용이
- Kernel 서비스 서버의 간단한 시작/ 종료 가능
- 문제있는 서비스는 서버를 재시작하여 해결할 수 있어 이론적으로 Monolithic보다 안정적
- Server 코드가 Protected Memory에서 실행되므로, 검증된 S/W 분야에 적합.

단점
- Monolithic Kernel보다 낮은 성능을 보임.
:독립된 서버들 간의 통신 및 Context Switching으로 인해 전달횟수가 많아질수록 Overhead가 많아짐.

__Hypervisor__
- 가상화된 컴퓨터 H/W 자원을 제공하기 위한 관리 계층.
- 게스트 OS와 H/W사이에 위치하여 H/W에 대한 접근은 Hypervisor에게 할당 받은 자원에 대해서만 수행.
- Hypervisor는 각 게스트 OS간의 CPU, 메모리 등 시스템 자원을 분배하는 등 최소한의 역할을 수행.

장점
- 하나의 물리컴퓨터에서 여러 종류의 게스트 OS 운용이 가능
:한 서버에서 다양한 서비스를 동시에 제공.
- 실제의 컴퓨터가 제공하는 것과 다른 형태의 명령어 집합 구조(Instruction Set Achitecture)를 제공.
:다른 H/W환경으로 컴파일된 게스트 OS 및 응용 프로그램도 실행 가능

단점
- H/W를 직접적으로 사용하는 다른 운영체제에 비해 성능이 떨어짐
-> 반가상화(Para-Virtualization)로 성능저하 문제를 해결함.
단, 게스트OS의 H/W 의존적인 코드에 대한 수정이 요구됨.
- 높은 기술적인 능력, OS의 소스가 없다면, 게스트 OS로 수정 불가능.

### Process 

__Process Management__
컴파일러 -> 링커 -> 로더

- 컴파일러 : 프로그래밍 언어로 작성된 Source code를 컴퓨터가 이해할 수 있는 기계어로 표현된 Object 파일로 변환
- 링커 : 관련된 여러 Object 파일들과 라이브러리들을 연결하여 메모리로 로드 될 수 있는 하나의 Executable로 변환.
- 로더 : Executable을 실제 메모리에 올려주는 역할을 담당

Process란? Abstraction for 
- Execution Unit : 스케줄링의 단위
- Protection Domain : 메모리에 로드된 기계어를 구분할 수 있도록 protection

__Process State__ : Time slice 활용에 필요한 Process Manage.
- New : 프로세스가 생성된 상태
- Running : 명령어가 실행되는 상태
- Waiting : I/O등의 이벤트로 발생되면서 프로세스가 기다리는 상태
- Ready : 프로세서에 의해 할당을 기다리는 상태
- Terminated : 프로세스가 실행을 마친 상태

__Process Control Block__
: 각각의 Process마다 정의가 필요하다고 생각해 구조체를 생성

### Context Switching : 여러 개의 프로세스를 Switch 하는 방법.
CPU가 새로운 프로세서로 전환할 때, 커널은 이전 프로세서의 상태를 저장하고, 새로ㅗ운 프로세서의 상태를 불러와서 저장해야 한다.

프로세서 구조에 따른 문맥 전환의 차이가 있다.

`CISC` (Complex Instruction Set Computing)
- 복잡한 명령어 셋 구성으로 효율은 높으나 클럭 속도 저하
- 복잡한 회로로 물리적인 공간차지가 많아 레지스터 용량이 저하

`RISC` (Reduced Instruction Set Computing)
- 간단한 명령어 셋 구성으로 클럭 속도가 높아 빠른 수행 속도를 지님
- 절약된 물리적 공간에 많은 레지스터를 장착하지만, Context Switching시 레지스터 내용 변경에 더 큰 오버헤드가 발생한다.

__Bus__
:CPU, RAM, I/O 장치 간 데이터가 전송되는 통로
- 하나의 시스템 버스가 여러가지 모듈이 연결
- 각 장치의 속도가 비슷했던 초창기에 생성했으나, 속도 격차가 증가하면서 병목현상 발생

>__병목현상__
>- 같은 버스에 연결된 디바이스(하드웨어)들 사이의 속도 차이로 인해 발생.
>- CPU > Memory > I/O 순서로 속도의 격차가 커짐.

1. 하드웨어적인 해결법 (계층적 버스 구조)
- 세분화된 버스 채용 : CPU Local Bus, Memory Bus, PCI Bus etc..

2. 이중버스
- CPU와 I/O 속도 격차로 인한 병목 현상 해결하고자 함.
- 빠른 CPU와 메모리는 시스템 버스에 연결하고 I/O는 I/O버스에 연결

3. 이벤트 처리 기법 (Interrupt)
- 외부로 부터 발생하는 비동기적 이벤트(네트워크 패킷 도착, I/O 요청)를 처리하기 위한 기법

4. 이벤트 처리 기법 (Trap)
- 의도적으로 생성한 동기적 이벤트를 처리하기 위한 기법. Trap Handler에 의해 처리
ex) Divide by Zero, Segmentation Fault 와 같은 프로그램 에러

5. I/O Device Basic Concepts
Device Registers
- 보통 하드웨어 장치는 4종류의 Register를 가짐
  :Control, Status, Input, Output Register
- Register들은 메인 메모리의 일부 영역에 mapping
  :Mapping된 영역의 주소만 알면, CPU에서 접근 가능.
I/O Controller
- High-Level의 I/O요청을 Low-level Machine Specific Instruction으로 해석하는 회로
- 장치와 직접 상호작용.

6. I/O처리 기법 : Polling
- Loop안에서 특정 이벤트의 도착 여부를 CPU가 확인하면서 기다리는 방법.
- Interrupt Handler를 등록하는 방식과 반대되는 개념. : Polling은 매 순간 이벤트의 발생 여부를 확인.
- Controller나 장치가 매우 빠른 경우, Polling은 Event 처리 기법으로 적당함.
- 이벤트 도착 시간이 길 경우, Polling은 CPU Time을 낭비
 : 컴퓨터 시스템에서 CPU Time은 매우 귀중한 자원
- Polling은 흔히 Programmed I/O로 알려진 방식

7.	I/O처리 기법 : Direct Memory Access (DMA) – 하드웨어적으로 병목현상을 해결하기 위한 방안
DMA Controller라는 프로세서 사용.
- CPU와 DMA Controller 간의 통신으로 I/O를 수행.
- CPU가 DMA Controller에게 I/O를 요청하면, DMA Controller는 CPU를 대신하여 I/O Device와 Main Memory 사이의 데이터 전송을 수행 : CPU는 I/O시간 동안 다른 일을 수행할 수 있음.
Polling을 사용할 경우, 모든 I/O연산은 CPU에 의해 진행되는데, 전송할 데이터가 클 경우 CPU가 Polling을 위해 I/O Device의 상태 확인 및 버스에 데이터를 쓰는 행위 (PIO)에 사용하는 것은 낭비.

> DMA vs Polling
DMA – 추가적인 Hardware(Cost)가 필요하다. 
성능 – DMA를 최대한 활용하기 위해서는 적당한 Parallelism이 필요하다. 
예) Smartphone Camera Pixel(I/O)를 읽어 들이려 할 때 DMA가 필요한가?
 -> Application Policy에 따라 다르다, 카메라를 찍는 사이에 다른 동작이 필요하면 DMA, 필요 없으면, Polling 
 
8.	I/O Device Access 기법 : I/O Instruction 
- Controller는 보통 1개 혹은 그 이상의 Register를 가짐. Data, Control Signal을 처리하기 위함.
- CPU는 Controller의 Register의 Bit Pattern을 읽고 씀으로써 장치와 통신함.
 : 이러한 기능을 수행하기 위한 hardware Architecture가 I/O Instruction을 제공. Ex) Intel CPU의 IN, OUT
장점 – 프로그래머 입장에서 간단.
단점 – 컴퓨터 구조가 복잡해 질 수 있음.

9.	I/O Device Access 기법 : Memory Mapped I/O
Device Register들을 Memory 공간에 Mapping하여 사용. Register들은 주소 공간의 일부로 여겨짐..
- Disk Register, Print Register등을 미리 Mapping. CPU는 이 메모리에 Status를 이용하여 I/O작업수행.
CPU는 일반적인 명령어를 사용하여 I/O작업을 수행. ex) mov, and, or ,택
장점 - 하드웨어 설계가 쉬워짐
단점 – 컴파일러의 설계가 어려워짐.

## CPU Scheduling
: 어떻게 Process에게 CPU의 사용을 할당할 것인가? Multiprogramming에 기반함. Memory내의 실행 준비된(Ready State)의 Process들 가운데 하나에게 CPU를 할당함.
- 목표 : CPU사용률과 처리량의 최대화

CPU Scheduling의 결정은 다음 시점에 따라 이루어짐.
1) 

### 비선점형 스케줄링(Non-preemptive Scheduling)__
: 이미 진행되고 있는 Process의 대해서 건들지 않고, 수행하는 Scheduling 기법.

### 선점형 스케줄링(preemptive Scheduling)__
: OS가 현재 CPU를 사용하고 있는 Process의 수행을 정지하고, 우선순위가 더 높은 Process를 수행하는 Scheduling 기법

__First-Come, First-Served Scheduling (FCFS)__ - 비선점형
- 먼저 CPU 할당을 요청한 Process에 CPU를 먼저 할당한다.
- FIFO Queue를 사용하여 간단하게 구현가능
- 작업의 수행 순서에 따라 대기 시간이 변할 수 있음.

__Shortest Job First Scheduling (SJFS)__ - 비선점형, 선점형
- 다음 CPU Burst Time이 가장 짧은 Process에 CPU를 먼저 할당. 최소의 평균 대기 시간을 제공.
- 비선점형 방식 : 한번 CPU를 할당받으면 자신의 CPU time이 끝나기 전까지 놓지 않음.
- 선점형 방식 : CPU를 할당받아 수행중이더라도 CPU BurstTime이 자신의 현재 남은 시간보다 짧은 시간을 가진 프로세스가 새로 생성되면 CPU를 양보. 
- SRTF(Shortest Remaining Time First Scheduling)

__Priority Scheduling__ - 비선점형, 선점형
- 미리 주어진 Priority에 따라 CPU를 할당.
- 비선점형 방식과 선점형 방식이 둘다 있음.

__Round Robin Scheduling__ - 선점형
- CPU를 시간 단위(Time Quentum)로 할당하여 Process를 수행.
- Time Quantum 만큼 수행한 Process는 Ready Queue의 끝으로 들어가 다시 할당을 기다림.
- 보통 Time Quantum은 10-100 milliseconds

__Multilevel Queue Scheduling__
- Ready Queue를 여러 개의 Queue로 분리하여, 각각에 대해 다른 Scheduling Algorithm을 사용하는 기법이다.
- Foreground Queue : Interative한 동작이 필요한 Process를 위한 Queue -> Round Robin 기법 사용.
- Background Queue : CPU 연산 작업을 주로 수행하는 Process를 위한 Queue -> FCFS 기법 사용.

__Multilevel Feedback Queue Scheduling__
- Multilevel Queue에서 Process들이 서로 다른 Queue로 이동할 수 있도록 한 Scheduling 기법
- Aging의 한 방법으로 사용됨.


## Inter Process Communication (IPC)
: Process들 간에 데이터 및 정보를 주고 받기 위한 Mechanism


### IPC 방식

__공유 메모리 (Shared Memory)__
- Process의 특정 메모리 영역을 공유하여 읽기/쓰기를 통해 통신을 수행.
- 응용프로그램 레벨에서 통신 
- Memory 영역에 대한 동시적인 접근을 제어하기 위한 방법으로 Locking이나 세마포어(Semaphore) 방법이 있음.
- 활용 예) 데이터베이스

__메시지 교환(Message Passing)__
- Process간 Memory 공유 없이 동작 가능.
- 고정 길이 메시지, 가변길이 메시지를 송/수신자끼리 주고 받음.
- Kernel을 통한 메시지 통신 기능을 제공.
- 활용 예) 클라이언트-서버 방식의 통신

__Pipe (Message Passing)__
- 하나의 Process가 다른 Process로 데이터를 직접 전달하는 방법.
- 데이터가 한쪽 방향으로만 이동하기 때문에 양방향 통신을 위해서는 두 개의 Pipe가 필요(Half Duplex)
- 1:1 의사소통만 가능하며, 용량 제한이 있음.

__Signal (Message Passing)__
- 특정 Process에게 Kernel을 통해 Event를 전달하는 방법.

__Message Queue(Message Passing)__
- 고정된 크기를 갖는 Message의 연결 리스트를 이용하여 통신하는 방법
- 여러 Process가 동시에 접근 가능 - 동기화필요 (N:M 방식)
  
__Socket(Message Passing)__
- 운영체제가 제공하는 Port를 이용하여 통신하려는 상대 Process의 Socket을 찾아가는 끝단 커뮤니케이터 방식.
- 다른 IPC와 달리 Process의 위치에 Independent함.
  

## Thread

### Process vs Thread
- Process
  - Execution Unit
  - Protection domain
  - Process간의 Memory는 독립적이므로, 서로의 영역에 접근하기 어려움.
  - Process간의 Switch 비용이 큼 (상대적으로 Heavy Weight)
- Thread
  - Execution unit
  - Process 내의 실행 흐름.
  - Process의 Code 영역과 Data 영역을 Thread간의 공유하므로 Switch 비용이 적음.

-> 하나의 Process에는 하나의 Control만 존재하였기 때문에 여러개로 작업을 나눈 후에 각각을 Thread화 한다면, 병렬적으로 작업을 완수. ex) Thread-1 : I/O, Thread-2 : Calculate

> MultiProcessing과 MultiThreading의 차이점
> - MultiProcessing 은 IPC가 필요.
> - Process 사이의 Context Switching 비용
> - Process 내에서 Cooperation하는 Thread를 만든다면? Process보다 적은 비용으로 Cooperative Process가 하는 일을 동일하게 수행 가능.

Thread의 수가 증가할수록, CPU의 Utilization이 증가
- 임계값을 넘어가면 다시 감소 -> Thread Switching 비용이 점점 증가하기 때문.

## 동기화

### Race Condition
- 서로 다른 Process가 동시에 접근하여 데이터를 변경하는 상황
- 공유 데이터에 대한 동시 접근은 데이터의 일관성(Consistency)를 해치는 결과를 낳을 수 있음.

__Critical Section__
- 여러 Process들이 공유하는 데이터에 접근하는 Code 영역
- 한 번에 오직 하나의 Process만이 Critical Sections에 진입해야 함.
- Critical Section 문제를 해결하기 위한 Algorithm은 아래와 같은 세 가지 조건을 만족해야 함.
  - Mutual Exclusion(상호 배제) : 만약 Process A가 Critical Section에 진입해 있다면, 다른 모든 Process는 진입할 수 없어야 함.
  - Progress(진행) : 어떤 Process도 Critical Section내에 있지 않고, 진입하려는 Process가 존재한다면, Remainder Section에서 실행중이 아닌 Process들 만이 누가 진입할지 결정할 수 있어야함.
  - Bounded Waiting : Process가 Critical Section에 진입할 때까지 걸리는 시간에 Limit이 존재해야 함.

### Mutex with Test and Set
- CPU에서 지원하여 원자적으로 수행되는 명령어를 이용. Lock을 잡는 변수 조차 다른 프로세스와 동시 접근이 되면 안되기 때문에 하드웨어 instruction을 사용.
- Bounded Waiting 같은 조건은 User Program에서 제공. 좀 더 잘 사용할 수 있는 동기화 방법이 필요.
```
boolean TestAndSet(boolean *target) {
    boolean rv = *target;
    *target = true;
    return rv;
}

do {
  while (TestAndSet(&lock));
      critical section
  lock = false;
      remainder section
}
```

### Semaphores (세마포어)
- 두개의 원자적 연산을 갖는 정수 변수
  - 원자적인 연산:
    - Wait() or P() : lock을 잡는 용도
    - Signal() or V() : lock을 해제하는 용도
  - 이 변수는 2개의 원자적인 연산에 의해서만 접근 됨.
- P는 Critical Section 들어가기 전에, V는 나와서 수행함.

__Busy Waiting__
- loop를 돌면서 요청.
- Critical Section에 진입할 조건이 될 때까지 Loop를 돌며 기다린다.
  - CPU Cycle을 낭비할 수 있음.
  - 대기 중인 Process 중 누가 Critical Section에 진입할 지 결정하지 않음.

__Sleep Queue__
- Busy Waiting 방식의 CPU Cycle을 낭비하는 문제를 해결.
- Semaphore의 자료구조에 Sleep Queue를 추가하여, 대기중인 Process 관리.
- Semaphore의 값이 양수가 되어 Critical Section에 진입이 가능하게 되면 대기중인 Process를 깨워 실행.

### Semaphores의 단점
- Deadlock이 발생할 가능성이 존재함. 
> Deadlock?
> 서로가 필요한 락을 반대로 잡고 있을 때, 어떤 것도 실행되고 있지 않은 경우. 두 개 이상의 Process들이 끝없이 이벤트를 기다리고 있는 상황.
- P와 V의 연산이 분리되어 있기 때문에 이를 잘 못사용할 경우에 대한 대책이 없음. -> High-level언어에서 동기화를 제공하는 방법 필요.

### Monitor
- High-level 언어에서의 동기화 방법. Java의 Thread에서 동기화를 위한 방법으로 Monitor가 사용됨.
- 한 순간에 하나의 Process만 Monitor에서 활동하도록 보장. Entry Queue에서 대기하고 있는 Process들은 Shared Data를 사용하기 위해서 Monitor에 진입해 제공되는 Operation을 통해야 함.

## Memory Management
- 여러 Program이 동시에 Memory에 적재되어 실행되면서, Memory를 공유할 필요가 생김.
- Computer의 Memory는 한정된 자원 -> 실행하는 Program이 많아지면 Memory 요구량이 증가.
- `제한된 물리메모리가 커져가는 가상 메모리량을 감당할 수 없게 되고, 각각의 프로그램에게 잘 할당해주기 위한 메모리 관리 필요.`

### 주소 공간
- Process에서 참조할 수 있는 주소들의 범위, Process와 1:1 관계
- CPU의 주소 버스의 크기에 의존함. 

__물리주소__
- 컴퓨터의 메인 메모리를 접근할 때 사용되는 주소
- 기억 장치의 주소 레지스터에 적재되는 주소

__가상 주소__
- Process의 관점에서 사용하는 주소
- Logical이기 때문에 주소 공간을 의미 있는 단위로 나누어 사용하지 않음.

> 초창기 컴퓨터의 주소 관리
> 물리 주소를 Compile Time에 생성했으나, 다양한 Program이 실행됨에 따라 Compile Time에 물리 주소를 정하기가 어려워짐. -> 가상 주소를 생성.

__Memory Management Unit(MMU)__
- Virtual Address와 Physical Address 간의 변환을 수행하는 Hardware 장치
- CPU로 부터 받은 virtual address를 physical address로 번역하여 memory로 보낸다.

### 가상 메모리
- Memory로서 실제 존재하지는 않지만, 사용자에게 Memory로서의 역할을 하는 Memory
- Process가 수행 되기 위해서 Program의 모든 부분이 실제 메모리(Physical Memory)에 있을 필요는 없다.
  - 현재 실행되고 있는 Code 부분만이 실제 Memory에 있으면 Process는 실행이 가능.

### Paging 기법
- 주소 공간을 동일한 크기인 Page로 나누어 관리
  - 보통 1 Page의 크기는 4KB로 나누어 사용.
  - 프레임(Frame)
    - 물리 Memory를 고정된 크기로 나누었을 때, 하나의 Block
  - 페이지 (Page)
    - 가장 Memory를 고정된 크기로 나누었을 때, 하나의 Block
  - 각각의 프레임 크기와 페이지 크기는 같다.
- Page가 하나의 Frame을 할당 받으면, 물리 Memory에 위치하게 된다.
  - Frame을 할당 받지 못한 Page들은 외부 저장장치(Backing Storage)에 저장된다.

__Page번호와 Offset__
- Page 번호 : 각 Process가 가진 Page 각각에 부여된 번호
- Page 주소 : 각 Page의 내부 주소를 가리킴.

### Page Table
- 각 Process의 Page 정보를 저장함
  - Process마다 하나의 Page Table을 가짐.
- Index : Page 번호
- 내용 : 해당 Page에 할당된 물리 Memory(Frame)의 시작 주소
  - 이 시작 주소와 Page주소를 결합하여 원하는 Data가 있는 물리 Memory 주소를 알 수 있음.
  
### Multilevel Page Table
- System의 발전에 따라 가상 주소 공간도 매우 큰 용량을 요구하게 됨
- 그로 인해 Page Table의 크기도 커지고, 그 차지하는 공간에 의해 Paging이 잘 이루어 질 수 없게 되고 있음.
- Page Table 자체도 Paging된 공간에 저장됨.
- Outer Page Table을 하나 더 두어, Page Table들을 가리키도록 한다.

### Inverted Page Table
- Multilevel Page Table에서와 같은 Page Table의 용량 증가 문제를 해결하기 위한 다른 방법
- 64bit 주소 공간의 System에서 Multilevel Paging을 위한 정보의 크기는 32bit에 비해 현격하게 증가.
  - 아무리 가상 Memory 공간이 크더라도 , 물리 Memory의 크기에는 한계가 있음.
  - 모든 물리 Memory는 가상 Memory의 Page에 Mapping 될 확률이 높음.
- Page Table은 보다 적은 용량을 차지하지만, Table을 검색하는데 시간이 오래 걸린다. -> Hash Table을 사용하여 단축 가능.

### Page Replacement Algorithms.
- Page 교체에 의한 I/O 작업 수행 횟수를 최대한 줄이려는 목적을 갖고 있으며, 적합한 Algorithm의 사용은 System의 성능을 크게 좌우하는 요소임.

__LFU Algorithm (Least Frequently Used)__
- 사용 빈도가 가장 적은 Page를 교체하는 기법. 가장 적게 참조된 Page가 교체 대상으로 선택된다.
- 실행 초기에 많이 사용된 Page는 그 후로 사용되지 않더라도 Frame을 계속 차지하는 문제가 있음.
7 7 7 2 2 4
  0 0 0 0 0
    1 1 3 3

__NRU Algorithm (Not Recently Used)__
- 최근에 사용하지 않은 Page를 교체하는 기법
- Page마다 참조 bit과 변형 Bit을 두어 관리
- 참조 bit (Reference Bit)
  - 최초로 Frame에 Load 될 때와 Page가 참조 되었을 때마다 1
  - 일정 주기마다 다시 0으로 Reset
- 변형 Bit (Modified Bit)
  - 최초로 Frame에 Load 될 때는 0
  - Page의 내용이 바뀔 때 1

__LRU Algorithm (Least Recently Used)__
- 가장 오랜 시간 참조되지 않은 Page부터 먼저 교체
  - Page 사용의 지역성(Locality)을 고려하여, Optimal Algorithm과 유사하며 실제 구현 가능한 Algorithm

`7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`
7 7 7 2 2 4 4 4 0 1 1 1
  0 0 0 0 0 0 3 3 3 0 0
    1 1 3 3 2 2 2 2 2 7

### Swapping 
- Page Out으로 Memory 부족을 해결하지 못할 경우 필요한 기법
- Swap Out 대상이 된 Process 전체를 Secondary Storage로 보낸다.
- Swapping에 사용되는 Secondary Storage를 Swap 영역이라 함.




