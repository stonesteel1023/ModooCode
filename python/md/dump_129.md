----------------
title : 씹어먹는 C 언어 - <24. 더 빠르게 실행되는 코드를 위하여 (C 코드 최적화)>
cat_title : 24. 더 빠르게 실행되는 코드를 위하여 (C 코드 최적화)
next_page : 130
publish_date : 2011-01-18
--------------



이번 강좌에서는

* C 언어 코드의 최적화 기법에 대해 살펴본다 C 언어 코드의 최적화 기법에 대해 살펴본다.


![씹어먹는 C 언어](/img/ChewingClogo.png)


안녕하세요 여러분~ 이제 저의 마지막 강의(총 41 강)가 되겠네요. 그럼, 오늘도 강의를 시작해 볼까요?


우리의 컴퓨터는 무한정 빠르지 않습니다. 따라서 동일한 작업을 시키더라도 어떠한 방식으로 시키냐에 따라서 그 속도가 엄청나게 차이가 나게 됩니다. 우리는 언제나 코드를 만들 때 '과연 어떻게 해야지 이 작업을 가장 빠르게 할 수 있도록 코드를 만들 수 있을까?' 를 고민 해야 합니다. 이렇게 똑같은 일이라도 더 빠르게 수행할 수 있도록 코드를 짜는 행위를 '코드 최적화' 라고 부릅니다.

  참고적으로 아래의 내용은 대부분 [http://www.codeproject.com/KB/cpp/C___Code_Optimization.aspx](http://www.codeproject.com/KB/cpp/C___Code_Optimization.aspx)에서 가져왔으며, 특히 한국어로 번역된 자료는 [http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/C/Documents/COptimization](http://www.joinc.co.kr/modules/moniwiki/wiki.php/Site/C/Documents/COptimization)에서 보실 수 있습니다. 저는 여러분들께 여기에서 가장 중요하다고 생각되는 몇 가지 부분만을 쉽게 이야기 하고자 합니다.

### 산술 연산 관련

#### 부동 소수점 (float, double) 은 되도록 사용하지 말자

  예전에 [10 강에서 부동 소수점 수의 구조](http://itguru.tistory.com/17)에 대해 이야기 한 적이 있습니다. 그 때 강좌를 잘 보셨던 분은 알겠지만 부동 소수점 수는 그 구조가 매우매우 복잡합니다. 정수 자료형(int, `short, ... )` 의 경우 단순히 2 진수를 나타낸 것에 불과하지만 부동 소수점은 그 수의 특정한 규격이 정해진 것이기 때문에 상당히 복잡하지요.

  따라서 부동 소수점 수를 가지고 하는 연산 자체도 매우 느릴 수 밖에 없습니다. 여러분들은 꼭부동 소수점 연산은 오직 '반드시 필요할 때 에만' 사용하시기 바랍니다. 여기서 반드시 필요할 때 라면 소수점 몇 째 자리 까지 정밀도를 요구할 때에나 매우 큰 수를 다룰 때 입니다. 만일 소수점 둘째 자리나 첫째 자리 정도의 정밀도를 요구한다면 단순히 그 수에 `x 10, x 100` 을 하셔서 정수 자료형으로 다루는 것이 오히려 좋습니다.

#### 나눗셈을 피해라 (1)

아래는 초 를 증가시켜주는 함수 입니다.

```cpp-formatted
int inc_second(int second) { return (++second) % 60; }
```

  초의 범위는 0 부터 59 이므로 1 증가시킨 뒤에 만일 60 을 넘었을 때를 대비하여 위와 같이 60 으로 나눈 나머지를 구해야 되겠지요. 그런데 여기서 문제는 나눗셈은 매우매우 느린 연산이라는 것입니다. 다른 덧셈 뺄셈에 비해 몇 배 가까이 느리기 때문에 엄청난 시간 손해가 있겠지요. 우리가 만약 `second` 가 60 보다 커질 일이 없다는 것을 알고 있다면 굳이 60 으로 나눌 필요 없이 `if` 문으로 60 일 때만 0 을 리턴해주면 되는 것입니다. 왜냐하면 `if` 문은 나눗셈 보다는 훨씬 빠르게 처리가 되기 때문이지요.

```cpp-formatted
int inc_second(int second) {
  ++second;
  if (second >= 60) return 0;
  return second;
}
```


따라서 위와 같이 하면 훨씬 시간을 아낄 수 있습니다.

#### 나눗셈을 피해라 (2)

  앞에서도 말했듯이 나눗셈은 시간이 매우매우 오래 걸리는 작업이라고 했습니다. 그런데 놀랍게도 2 의 멱수들 (2,4,8,16,32 ...)  로 나눌 때에는 굳이 나눗셈을 사용하지 않고도 매우 간단하게 처리할 수 있는 방법이 있습니다. 바로 '쉬프트' 연산을 사용하는 것입니다. 쉬프트는 컴퓨터 연산 중에서도 가장 빠른 연산이므로 이를 잘만 활용한다면 시간을 엄청나게 절약할 수 있습니다.

2 의 멱수들을 이진수로 표현해 보면 1, 10, 100, 1000 등이 될 것입니다. 그럼 감이 오시나요? 우리가 만일 10 진수로 생각할 때 7865 를 100 으로 나누면 몫이 얼마가 될까요? 우리는 별로 고민하지 않고도 78 이라고 말할 수 있을 것입니다. 왜냐하면 단순히 끝의 두 자리를 버려버리면 되기 때문이지요. 이진수도 마찬가지 입니다. 11101010 을 1000 으로 나눈 몫은 얼마일까요? 이는 단순히 마지막 세자리를 버리면 되므로 11101 이 되겠지요.

  이 아이디어를 이용하면 1000 (이진수) 으로 나눌 때 에는 수를 오른쪽으로 3 칸 쉬프트 해버리면 됩니다. 즉, 오른쪽으로 3 칸 밀어버리는 것이지요 (쉬프트가 기억이 나지 않으면 [4 강 계산하리](http://itguru.tistory.com/8)를 보시기 바랍니다) 아래 예제는 32 로 나누는 것입니다. 32 는 2 의 5 승이므로 오른쪽으로 5 칸 쉬프트 해버리면 됩니다.

```cpp-formatted
#include <stdio.h>
int main() {
  int i;
  printf("정수를 입력하세요 : ");
  scanf("%d", &i);

  printf("%d 를 32 로 나누면 : %d \n", i, i / 32);
  printf("%d 를 5 칸 쉬프트 하면 : %d \n", i, i >> 5);

  return 0;
}
```


성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F123D4E494D3405F70A846B)


두 결과가 일치함을 보실 수 있습니다.

#### 비트 연산 활용하기 (1)

  비트 연산(OR, `AND, XOR` 등등) 은 컴퓨터에서 가장 빠르게 실행되는 연산들 입니다. 이러한 연산들을 잘 활용하면 좋겠지요. 일단 비트연산은 다음과 같이 여러가지 정보를 하나의 변수에 포함하는데 자주 사용됩니다. 예를 들어서 우리가 하나의 사람에 대한 여러가지 상태에 관한 정보를 나타내는 변수를 만든다고 합시다. 구조체를 배운 여러분으로써는 아래와 같이 만들 것입니다.

```cpp-formatted
struct HUMAN {
  int is_Alive;
  int is_Walking;
  int is_Running;
  int is_Jumping;
  int is_Sleeping;
  int is_Eating;
};
```

이는 상당한 메모리 낭비가 되겠지요. 6 가지 정보를 나타내는데 192 개의 비트나 소모하였기 때문이지요. 물론 이를 `char` 로 바꾸면 되지 않나 라고 물어볼 수 있지만 결국은 같은 얘기 입니다. 굳이 하나의 정보를 한 개의 비트에 대응시켜서 사용할 수 도 있는데 이를 각각의 변수에 모두 대응 시켜서 사용한 것이 문제이지요. 하지만 비트 연산을 잘 이용하면 이를 해결할 수 있습니다. 아래의 예제를 보세요

```cpp-formatted
#include <stdio.h>
#define ALIVE 0x1      // 2 진수로 1
#define WALKING 0x2    // 2 진수로 10
#define RUNNING 0x4    // 2 진수로 100
#define JUMPING 0x8    // 2 진수로 1000
#define SLEEPING 0x10  // 2 진수로 10000
#define EATING 0x20    // 2 진수로 100000
int main() {
  int my_status = ALIVE | WALKING | EATING;

  if (my_status & ALIVE) {
    printf("I am ALIVE!! \n");
  }
  if (my_status & WALKING) {
    printf("I am WALKING!! \n");
  }
  if (my_status & RUNNING) {
    printf("I am RUNNING!! \n");
  }
  if (my_status & JUMPING) {
    printf("I am JUMPING!! \n");
  }
  if (my_status & SLEEPING) {
    printf("I am SLEEPING!! \n");
  }
  if (my_status & EATING) {
    printf("I am EATING!! \n");
  }
  return 0;
}
```

성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile27.uf.tistory.com%2Fimage%2F203281334D3409E03A15C4)


와 같이 단순히 하나의 `int` 변수에 위 모든 데이터를 나타낼 수 있었습니다. 그 이유는 아래와 같이

```cpp-formatted
#define ALIVE 0x1     // 2 진수로 1
#define WALKING 0x2   // 2 진수로 10
#define RUNNING 0x4   // 2 진수로 100
#define JUMPING 0x8   // 2 진수로 1000
#define SLEEPING 0xC  // 2 진수로 10000
#define EATING 0x10   // 2 진수로 100000
```

`define` 을 이용해 여러개의 변수에 값을 대응시켰는데 한가지 특징은 각 데이터에는 오직 한 개의 비트만 1 이고 나머지는 모두 0 인 것입니다. 예를 들면 `JUMPING` 을 보면 16 진수 8 을 대응시켰는데, 이를 2 진수로 보면 끝에서 4 번째 자리만 1 이고 나머지 모든 자리는 0 인 수가 됩니다. 따라서 이와 같은 방식으로 수를 대응시키고

```cpp-formatted
int my_status = ALIVE | WALKING | EATING;
```

와 같이 `my_status` 에 `OR` 연산을 시켜주게 되면 각 데이터들이 나타내는 자리만 1 이 되고 나머지 모든 자리는 0 이 됩니다. 따라서 `my_status` 에는 `0...0100011` 이 되겠지요. 이제 이를 이용하여 `if` 문에서도 쉽게 사용할 수 있는데 단순히 유무를 파악하고자 하는 데이터와 `AND` 연산을 시키면 됩니다.

```cpp-formatted
if (my_status & WALKING) {
  printf("I am WALKING!! \n");
}
```


  예를 들면 위와 같이 내가 현재 `WALKING` 중인지 아닌지 파악하기 위해 `WALKING` 과 `AND` 연산을 시켜보면 만일 내가 `WALKING` 중이였다면 `AND` 연산시 '나머지 부분은 모두 0 이고, `WALKING` 에 해당하는 자리수만  1 이 될 것' 이여서 `if` 문에서 참으로 판단되고 (if 문은 0 이 아닌 모든 값을 참으로 생각한다) , 내가 `WALKING` 중이 아니였다면 '나머지 부분은 모두 0 이고 `WALKING` 에 해당하는 자리수 조차 0 이 될 것' 이므로 0 이 되어서 `if` 문에서 거짓으로 판단됩니다. 참으로 재밌는 일이지요. 참고로 비트 연산에 관련하여 아래의 내용을 기억하시면 편합니다.

1. 어떠한 정수의 특정 자리를 1 로 만들고 싶다면 그 자리만 1 이고 나머지는 0 인수와 `OR` 하면 됩니다.

1. 어떠한 정수의 특정 자리가 1 인지 검사하고 싶다면 그 자리만 1 이고 나머지는 0 인 수와 `AND` 하면 됩니다.

#### 비트 연산 활용하기 (2)

비트 연산을 가장 많이 활용하는 예로 또한 홀수/짝수 판별이 있습니다. 여태까지 여러분들은 아마 홀수 짝수 판별을

```cpp-formatted
if (i % 2 == 1)  // 이 수가 홀수인가
{
  printf("%d 는 홀수 입니다 \n", i);
} else {
  printf("%d 는 짝수 입니다 \n", i);
}
```

와 같이 만드셨을 것입니다. 그런데 제가 앞에서 계속 강조해 왔던 것이지만, 나눗셈 연산은 매우 느립니다! 하지만 놀랍게도 단순한 `AND` 연산 한번으로 이를 해결할 수 있습니다.

```cpp-formatted
if (i & 1)  // 이 수가 홀수인가
{
  printf("%d 는 홀수 입니다 \n", i);
} else {
  printf("%d 는 짝수 입니다 \n", i);
}
```

  만일 어떤 정수가 홀수라면, 2 진수로 나타냈을 때 맨 마지막 자리가 1 이여야 합니다 (당연하지요?) 이를 이용해서 단순히 어떤 정수의 맨 마지막 비트가 1 인지만 확인하면 되지요? 근데 위에서 강조했듯 것을 보면 맨 마지막 비트가 1 인지 확인하려면 맨 마지막 비트만 1 인 수(즉 `1)` 과 `AND` 하면 됩니다. 아래 소스로 컴파일해서 실행해보면 잘 됨을 알 수 있습니다.

```cpp-formatted
#include <stdio.h>
int main() {
  int i;
  scanf("%d", &i);

  if (i & 1)  // 이 수가 홀수인가
  {
    printf("%d 는 홀수 입니다 \n", i);
  } else {
    printf("%d 는 짝수 입니다 \n", i);
  }
  return 0;
}
```


성공적으로 컴파일 하였다면


![""](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F1938A6594D34119938AE3D)


### 루프(loop) 관련

#### 알고 있는 일반적인 계산 결과를 이용하라

대표적으로 이야기 하자면 1 부터 `n` 까지 더하는 함수를 만들 때 입니다. 일반적으로 이러한 작업을 하는 코드를 짤 때에는

```cpp-formatted
for (i = 1; i <= n; i++) {
  sum += i;
}
```

위와 같이 `for` 문으로 구현하는 경우가 대부분 입니다. 하지만 여러분이 초등학생 가우스 정도의 머리를 가졌더라면 위와 같이 일일히 더하는 것 말고도

```cpp-formatted
sum = (n + 1) * n / 2;
```


로 간단히 나타낼 수 있겠지요. 이렇게 하게 될 경우 많은 계산 시간을 절약하게 됩니다.

#### 끝낼 수 있을 때 끝내라

아래 코드는 특정한 문자열에 'a' 라는 문자가 포함되어 있는지 검사하는 코드 입니다.

```cpp-formatted
while (*pstr) {
  if (*pstr != 'a') {
    does_string_has_a = 1;
  }

  pstr++;
}
```

위 코드에서 `does_string_has_a` 가 한 번 1 이 되었다면 뒤에서 바뀔 일이 없으므로 굳이 루프를 끝까지 실행하는 것은 무의미한 짓입니다. 이 때 이런 곳에 `break` 문을 넣어서 빠져 나갈 수 있게 한다면 불필요한 실행을 줄일 수 있습니다.

```cpp-formatted
while (*pstr) {
  if (*pstr != 'a') {
    does_string_has_a = 1;
    break;
  }

  pstr++;
}
```

위 코드 처럼 말이지요.

#### 한 번 돌 때 많이 해라.

  하나의 루프에서 동일한 일을 2 번 하는 것과, 하나의 루프에서 동일한 일을 한 번 하고 루프를 두번 돈다면 전자의 경우가 훨씬 효율적이라 말할 수 있습니다. 왜냐하면 루프를 한 번 돌 때 여러가지 조건들이 맞는지 비교하는 부분에서 시간이 약간 소모되기 때문이지요. 따라서 되도록이면 루프 한 번에 안에서 많은 일을 해버리는 것이 중요합니다.

  아래 코드는 정수 `n` 에서 값이 1 인 비트가 몇 개나 존재하는지 세는 프로그램 입니다.

```cpp-formatted
while (n != 0) {
  if (n & 1) {
    one_bit++;
  }
  n >>= 1;
}
```

   위 코드에서는 맨 끝 한개의 비트를 검사하고 오른쪽으로 쉬프트 해서 또 다시 맨 끝 비트를 검사하는 식으로 해서 결과적으로 모든 비트를 검사하여 값이 1 인 것의 개수를 셉니다. 하지만 우리는 C 언어에서 모든 정수 자료형의 크기가 8 비트의 배수 임을 알고 있습니다. 예를 들면 `char` 은 1 바이트로 8 비트, `int` 는 4 바이트로 32 비트 이지요. 따라서 굳이 1 개 비트씩 검사할 필요 없이 8 비트를 한꺼번에 묶어서 검사해도 상관이 없다는 말입니다. 이 때 8 비트를 한꺼번에 비교하면 너무 난잡하므로 4 비트씩 비교하는 것으로 하지요.

```cpp-formatted
while (n != 0) {
  if (n & 1) {
    one_bit++;
  }
  if (n & 2) {
    one_bit++;
  }
  if (n & 4) {
    one_bit++;
  }
  if (n & 8) {
    one_bit++;
  }
  n >>= 4;
}
```

와 같이 하면 됩니다. 사실 C 언어에서 `if` 문이나 `for` 문 다음에 한 줄만이 올 경우 중괄호를 생략해도 되는데,

```cpp-formatted
while (n != 0) {
  if (n & 1) one_bit++;
  if (n & 2) one_bit++;
  if (n & 4) one_bit++;
  if (n & 8) one_bit++;
  n >>= 4;
}
```

로 쓰셔도 됩니다. 아무튼 위와 같이 할 경우 루프 도는 회수를 줄일 수 있게 되므로 어느 정도의 시간 절약 효과를 보게 됩니다.

`4.` 루프에서는 되도록 0 과 비교하여라

```cpp-formatted
for (i = 0; i < 10; i++) {
  printf("a");
}

for (i = 9; i != 0; i--) {
  printf("a");
}
```

위 두 개의 `for` 문 중에서 무엇이 더 빠르게 실행될까? 실제로는 그리 큰 차이는 없을 테지만 엄밀히 따지고 보면 아래의 루프가 더 빠르게 돌아갑니다. 왜냐하면 위 루프의 경우 `i` 가 10 보다 작은지 비교하고 있고, 아래 루프에서는  `i` 가 0 과 다른지 비교하고 있는데 일반적으로 0 과 비교하는 명령어는 `CPU` 에서 따로 만들어져 있기 때문에 더 빠르게 작동될 수 있습니다.

#### 되도록 루프를 적게 써라

루프문을 굳이 쓰지 않고 쓸 수 있는 문장들은 되도록 직접 쓰는 것이 좋습니다. 예를 들어

```cpp-formatted
int i;
for (i = 1; i <= 3; i++) {
  func(i);
}
```


보다는

```cpp-formatted
func(1);
func(2);
func(3);
```

와 같이 루프를 풀어버리는 것이 더 좋을 때가 있습니다. 물론 루프를 쓰면 무엇을 하는지 한눈에 알 수 있지만 `for` 문 자체에서 여러가지 비교를 수행하는데 시간이 들기 때문에 위와 같이 간단히 루프를 쓰지 않고도 나타낼수 있다면 그 방법을 선택하시기 바랍니다.

### `if` 및 `switch` 문 관련

#### if 문을 2 의 배수로 쪼개기

예를 들면 아래와 같은 비교 명령들이 있다고 합시다.

```cpp-formatted
if (i == 1) {
} else if (i == 2) {
} else if (i == 3) {
} else if (i == 4) {
} else if (i == 5) {
} else if (i == 6) {
} else if (i == 7) {
} else if (i == 8) {
}
```

(물론 위와 같은 명령들은 `switch` 문을 이용하는 것이 훨씬 바람직합니다)
위 경우 `if` 문에서는 최악의 경우 최대 8 번의 비교작업을 해야 하는 상황이 발생합니다. 이는 엄청난 낭비가 아닐 수 없죠.

```cpp-formatted
if (i <= 4) {
  if (i <= 2) {
    if (i == 1) {
      /* i is 1 */
    } else {
      /* i must be 2 */
    }
  } else {
    if (i == 3) {
      /* i is 3 */
    } else {
      /* i must be 4 */
    }
  }
} else {
  if (i <= 6) {
    if (i == 5) {
      /* i is 5 */
    } else {
      /* i must be 6 */
    }
  } else {
    if (i == 7) {
      /* i is 7 */
    } else {
      /* i must be 8 */
    }
  }
}
```

하지만 `if` 문을 위와 같이 구성하게 된다면 어떨까요? 이와 같이 `if` 문을 쪼개는 것을 `Binary Breakdown` 이라고 하는데 이진의 형태로 쪼갠 것이지요. 이럴 경우 `i` 가 1 에서 8 까지 어떠한 값을 가지더라도 3 번만의 비교로 값을 알아낼 수 있습니다. 참고로 이전의 `if` 문의 형태로는 평균적으로 4 번의 비교가 필요했지요.

#### 순차적 비교에서는 `switch` 문을 사용해라

  사실 위의 `if` 문 예제에서는, 즉 위와 같이 순차적인 정수 값을 비교하는 경우에는 `switch` 문을 사용하는 것이 매우 요긴합니다. 왜냐하면 `switch` 문에서는 단 한번의 비교만으로 우리가 실행될 코드가 있는 곳으로 ‘점프’ 하기 때문이지요. `switch` 문의 원리는 9강 – 만약에.. 2 탄 [http://itguru.tistory.com/16](http://itguru.tistory.com/16)에서 보시기 바랍니다.

  즉 아래와 같은 코드가 훨씬 더 효율적입니다.

```cpp-formatted
switch (i) {
  case 1:
    break;
  case 2:
    break;
  case 3:
    break;
  case 4:
    break;
  case 5:
    break;
  case 6:
    break;
  case 7:
    break;
  case 8:
    break;
}
```



#### 룩업 테이블(look `up table,` LUT)을 사용할 수 있으면 사용해라

  룩업 테이블이란, 원론적으로 설명하면 특정 데이터에서 다른 데이터로 변환할 때 사용되는 테이블이라 할 수 있습니다. 말만 들으면 조금 어려운데요, 사실 컴퓨터에서 매우 자주 사용되고 있습니다. 예를 들어 컴퓨터에서 `3D` 처리를 할 때 많은 수의 `sine` 이나 `cosine` 연산들이 들어가게 됩니다. 이 때 `sin` 값 계산은 꽤 오랜 시간 걸리는 계산인데 `sin 1` 값이 필요할 때 마다 계산을 하게 된다면 아주 시간 낭비가 심하겠지요. 이를 막기 위해 프로그램 실행 초기에 `sin 1` 부터 `sin 90` 까지 미리 다 계산해 둔 뒤 표로 만들어 버리면 나중에 `sin 1` 값이 필요하면 단순히 표에서 1 번째 값을 찾으면 되니까 아주 편하겠지요.

  이렇게 만들어 놓은 테이블을 룩업 테이블이라고 부릅니다. 즉, 필요한 데이터를 쉽게 ‘찾을 수 있도록’ 만들어 놓은 표라고 보시면 됩니다. 예를 들면 아래와 같은 경우 사용할 수 있습니다.

```cpp-formatted
char* Condition_String1(int condition) {
  switch (condition) {
    case 0:
      return "EQ";
    case 1:
      return "NE";
    case 2:
      return "CS";
    case 3:
      return "CC";
    case 4:
      return "MI";
    case 5:
      return "PL";
    case 6:
      return "VS";
    case 7:
      return "VC";
    case 8:
      return "HI";
    case 9:
      return "LS";
    case 10:
      return "GE";
    case 11:
      return "LT";
    case 12:
      return "GT";
    case 13:
      return "LE";
    case 14:
      return "";
    default:
      return 0;
  }
}
```


위 코드의 경우 꽤 괜찮지만 아래 처럼 훨씬 간단하게 만들 수 있습니다.

```cpp-formatted
char* Condition_String2(int condition) {
  if ((unsigned)condition >= 15) {
    return 0;
  }
  return "EQ\0NE\0CS\0CC\0MI\0PL\0VS\0VC\0HI\0LS\0GE\0LT\0GT\0LE\0\0" +
         3 * condition;
}
```



위에서 주목할 부분은 룩업 테이블을 이용한 것인데, 위 코드에서 룩업 테이블은

```cpp-formatted
"EQ\0NE\0CS\0CC\0MI\0PL\0VS\0VC\0HI\0LS\0GE\0LT\0GT\0LE\0\0"
```



을 가리킵니다. 이 것이 룩업 테이블인 이유는 `condition` 값을 알면 바로 위 테이블에서 문자열을 찾아낼 수 있기 때문이지요. 위 `switch` 문을 룩업 테이블로 만들어 버릴 수 있었던 이유가 바로 리턴되는 문자열의 크기가 모두 동일해서 인데 이를 통해 위 룩업 테이블의 시작 주소값에서 `3 * condition` 을 더하면 우리가 원하는 문자열의 시작 주소값이 나오게 됩니다.

이 때 위와 같이 룩업 테이블을 이용하면 좋은 점이 코드의 길이가 훨씬 짧아진다는 점이고 실제 프로그램의 크기도 줄어든다는 점에 있습니다.

### 함수 관련

#### 함수를 호출할 때에는 시간이 걸린다.

```cpp-formatted
#include <stdio.h> void print_a();

int main() {
  int i;
  for (i = 0; i < 10; i++) {
    print_a();
  }
  return 0;
}
void print_a() { printf("a"); }
```



위 코드와 아래 코드를 보면 무엇이 더 빠르게 작동할까요?

```cpp-formatted
#include <stdio.h>
void print_a();
int main() {
  print_a();
  return 0;
}
void print_a() {
  int i;
  for (i = 0; i < 10; i++) {
    printf("a");
  }
}
```



그 답은 바로 아래 코드 입니다. 왜냐하면 함수를 호출하는 데에도 꽤 많은 시간이 걸리기 때문이지요. 함수를 호출하기 위해서는 여러가지 작업이 필요한데 이 부분에 대한 설명은 생략하고 아무튼 위와 같이 동일한 작업을 위해 함수를 반복적으로 호출하기 보단 차라리 그 함수 내에서 반복적인 작업을 처리하는 것이 훨씬 더 효율적입니다.

#### 인라인(inline) 함수를 활용하자

```cpp-formatted
#include <stdio.h>
int max(int a, int b) {
  if (a > b) return a;
  return b;
}
__inline int imax(int a, int b) {
  if (a > b) return a;

  return b;
}
int main() {
  printf("4 와 5 중 큰 것은?", max(4, 5));
  printf("4 와 5 중 큰 것은?", imax(4, 5));
  return 0;
}
```



  위 두 개의 `printf` 문 중에서 더 빠르게 실행되는 문장은 어떤 것일까요? 바로 아래의 `inline` 함수를 이용한 것입니다. 위와 같이 `max` 와 같은 단순한 작업을 함수로 만들 때 에는 인라인 함수를 사용하는 것이 훨씬 더 효율적입니다. 이미 잘 알고 계시겠지만 인라인 함수는 함수가 아니지요 (자세한 설명은 [21 강 – 매크로 함수, 인라인 함수](http://itguru.tistory.com/99)참조). 반면에 `max` 함수는 실제로 함수의 호출 과정 부터 해서 여러가지 작업이 필요한데, 정작 내부에서 수행하는 작업은 매우 단순하여 오히려 함수 내부에서 하는 작업 시간 보다 호출하는데 걸리는 시간이 더 큰 배보다 배꼽이 더 큰 격이 됩니다. 따라서 위와 같이 단순한 작업을 함수로 만들 경우 인라인 함수를 이용하는 것이 더 좋습니다.

#### 인자를 전달할 때에는 포인터를 이용해라

```cpp-formatted
struct big {
  int arr[1000];
  char str[1000];
};
```



위와 같은 매우 거대한 구조체가 있다고 합시다. 만일 이 구조체 변수의 `arr[3]` 값을 얻어 오는 함수를 만들고 싶다면 어떻게 해야 할까요? 물론 아래와 같이 프로그램을 짜는 사람도 있을 것입니다.

```cpp-formatted
void modify(struct big arg) { /* 무언가를 한다 */ }
```


하지만 이 함수를 호출하게 될 경우 `modify` 함수의 `arg` 인자로 구조체 변수의 모든 데이터가 복사가 되야 하는데 이는 엄청난 시간이 걸리게 됩니다. 말그대로 5000 바이트나 되는 데이터의 복사를 수행해야 할 뿐더러 `modify` 변수의 메모리 공간을 위한 할당도 따로 필요하기 때문이지요. 그렇다면 아래의 코드는 어떨까요?

```cpp-formatted
void modify(struct big *arg) { /* 무언가를 한다 */ }
```


위 함수는 구조체 변수의 주소값을 얻어옵니다. 이는 단순히 4 바이트의 주소값 복사만이 일어날 뿐 이전의 예와 같은 무지막지한 복사는 일어나지 않습니다. 뿐만 아니라 동일하게 인자로 전달된 구조체 변수의 데이터들도 손쉽게 읽어들일 수 있게 됩니다. 단순히 `arg->arr[3]` 과 같은 방식으로 말이지요. 여러분들은 언제나 이 점을 명심하시고 되도록 인자를 전달할 때에는 포인터를 자주 활용하시기 바랍니다.

그럼 이것으로 마지막 강좌를 끝내도록 하겠습니다~ 혹시 1 강 부터 시작해서 여기까지 도달하신 분이라면 [http://itguru.tistory.com/notice/126#/](http://itguru.tistory.com/notice/126#/)에 가셔서 자유 게시판에 꼭 글을 남겨주시기 바랍니다~


### 생각해보기

#### 문제 1

 다음의 글들을 읽어보세요
 [http://decoder.tistory.com/529](http://decoder.tistory.com/529)
 [http://www.azillionmonkeys.com/qed/optimize.html](http://www.azillionmonkeys.com/qed/optimize.html)


##@ chewing-c-end