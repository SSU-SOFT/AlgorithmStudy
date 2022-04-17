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
- SErver 코드가 Protected Memory에서 실행되므로, 검증된 S/W 분야에 적합.

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


__Process Control Block__
: 각각의 Process마다 저으이가 필요하다고 생각해 구조체를 생성

### Context Switching : 여러 개의 프로세스를 Switch 하는 방법.
CPU가 새로운 프로세서로 전환할 때, 커널은 이전 프로세서의 상태를 저장하고, 새로ㅗ운 프로세서의 상태를 불러와서 저장해야 한다.

프로세서 구조에 따른 문맥 전환의 차이가 있다.

CISC (Complex Instruction Set Computing)
- 복잡한 명령어 셋 구성으로 효율은 높으나 클럭 속도 저하
- 복잡한 회로로 물리적인 공간차지가 많아 레지스터 용량이 저하

RISC (Reduced Instruction Set Computing)
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
DMA vs Polling
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
