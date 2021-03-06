----------------
title : 씹어먹는 C 언어 - <9. 만약에... 2탄 (switch 문)>
cat_title: 9. 만약에... 2탄 (switch 문)
next_page : 17
publish_date : 2009-08-15
--------------

* `switch` 문에 대한 이해, 내부적 처리에 대한 간단한 설명

![씹어먹는 C 언어](/img/ChewingClogo.png)

안녕하세요 여러분. 그 동안 잘 지내셨는지요? 제가 그 동안 바뻐서 글을 많이 못 올렸으나 일이 잘 해결되어서 이제 더이상 이전처럼 바쁘지 않겠네요. 아무튼, 지금까지 제 강좌를 보시느라 오랫동안 기다려 주신 분들께 정말 감사하다고 생각되고 아직까지도 C 언어를 배우고자 하는 열정이 사그라들지 않은 여러분들은 최고의 C 언어 프로그래머가 될 것이라 믿습니다.

이번 강좌에서는 `if` 문의 친구인 `switch` 문에 대해 배워 보도록 하겠습니다. `switch` 문이 `if` 문의 친구라고 한 이유는 하는 일이 정말로 `if` 문과 비슷하기 때문이죠. 일단, 아래의 초-간단한 강아지 시뮬레이션을 보세요.

```cpp-formatted
/* 마이펫 */
#include <stdio.h>
int main() {
  int input;

  printf("마이펫 \n");
  printf("무엇을 하실 것인지 입력하세요 \n");
  printf("1. 밥주기 \n");
  printf("2. 씻기기 \n");
  printf("3. 재우기 \n");

  scanf("%d", &input);

  if (input == 1) {
    printf("아이 맛있어 \n");
  } else if (input == 2) {
    printf("아이 시원해 \n");
  } else if (input == 3) {
    printf("zzz \n");
  } else {
    printf("무슨 명령인지 못 알아 듣겠어. 왈왈 \n");
  }
  return 0;
}
```

성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F166415244A8684E746F97D)

와 같이 3 가지 명령에 대해 반응하고 알 수 없는 명령은 '무슨 명령인지 못 알아 듣겠어. 왈왈' 라고 내보냅니다.

그런데, 만약 강아지가 위 3 가지 명령만 반응하는 것이 아니라 10 가지 명령에 반응하게 하고 싶다고 합시다. 그렇다면 여러분은 아마도 아래와 같이 할 것 입니다. (참고로 아래 '...' 인 부분은 필자가 쓰기 귀찮아서 생략한 부분 입니다.)

```info
   if (...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
    else if(...)
    {
        ...
    }
```

음, 아마도 위 소스코드를 보는 사람이 상당히 불편하게 느낄 것이라고 생각되지 않나요? 물론 보는 이에 따라 다르겠지만 아마 대부분의 사람이 그렇게 생각할 것 입니다. 아마 실제로 사람들과 함께 프로젝트를 진행 할 때 위와 같은 소스를 남발하게 된다면 읽는이도 불편하고 쓰는 사람도 손목이 많이 아플 것 입니다. (물론 `Ctrl + v` 신공이 있기는 하지만...)

따라서, 위와 같이 동일한 변수에 대해 비교문이 반복되는 경우에 아래와 같이 깔끔한 `switch` 문을 적용 시킬 수 있습니다.

```cpp-formatted
/* 업그레이드 버전 */
#include <stdio.h>
int main() {
  int input;

  printf("마이펫 업그레이드\n");
  printf("무엇을 하실 것인지 입력하세요 \n");
  printf("1. 밥주기 \n");
  printf("2. 씻기기 \n");
  printf("3. 재우기 \n");

  scanf("%d", &input);

  switch (input) {
    case 1:
      printf("아이 맛있어 \n");
      break;

    case 2:
      printf("아이 시원해 \n");
      break;

    case 3:
      printf("zzz \n");
      break;

    default:
      printf("무슨 명령인지 못 알아 듣겠어. 왈왈 \n");
      break;
  }

  return 0;
}
```

아마 컴파일 된 결과는 위와 동일하게 나올 것 입니다. 이제, 위 소스 코드에서 가장 중요한 부분인 `switch` 문 부분을 살펴보도록 합시다.

```cpp-formatted
switch (input) {
  case 1:
    printf("아이 맛있어 \n");
    break;

  case 2:
    printf("아이 시원해 \n");
    break;

  case 3:
    printf("zzz \n");
    break;

  default:
    printf("무슨 명령인지 못 알아 듣겠어. 왈왈 \n");
    break;
}
```

`switch` 문의 기본 구조는 아래와 같습니다.

```info
    switch(변수)
    {
    case 값1:
        명령들;
        break;
    case 값2:
        명령들;
        break;
        .. (생략) ..
    }

```

이 때, 변수 부분에는 값1, 값2, ... 들과 비교할 변수가 들어가게 됩니다. 위 예제의 경우 `input` 을 1 과 2 와 3 과 비교해야 했으므로 변수 부분에는 `input` 이 들어가게 됩니다. 이 때 `switch` 문에 사용될 변수로는 반드시 정수 데이터를 보관하는 변수여야 합니다. 다시말해 '변수' 부분에 들어가는 변수들의 타입은 `char, short, int, long` 중의 하나여야 합니다. 만약 `input` 이 `float` 이나 `double` 이라면 컴파일시 오류가 발생되게 됩니다.

`변수 ==  값1` 일 때, 가장 맨 위의 `case` 의 명령이 실행됩니다. 위 예제의 경우 1 이 입력되면 `case 1:` 이 참이 되므로 그 `case` 안의 내용들이 모두 실행됩니다. 이 때 각 명령들을 모두 실행한 후 `break` 를 만나면 `switch` 문을 빠져 나가게 됩니다.

예를 들어서 1 이 입력되었다면 `case 1:` 이 참이므로  `printf("아이 맛있어 \n");`  와 `break;` 가 실행되어 "아이 맛있어" 를 출력하고 `break` 를 통해 `switch` 문을 빠져 나가게 됩니다.

만약 `변수 == 값2` 라면 `case` 값1 은 실행되지 않고 `case` 값2 만 실행되게 됩니다.

또한 주의할 점으로는 '값' 에 위치하는 것들이 무조건 상수 이여야 한다는 것입니다. 만약 '값' 부분에 변수들이 오게된다면 오류가 발생하게 되는데 그 이유는 `switch` 문의 내부적인 처리 방법 때문입니다. (아래쪽 설명 되어 있습니다.)

마지막으로 `switch` 문의 `default` 는 `if` 문의 `else` 와 같은 역할을 합니다. 이도 저도 아닌 것들이 오는 `case` 이죠. 즉 위 예제의 경우 `input` 이 1 도 2 도 3 도 아닐 때 도달하는 경우가 됩니다.

그런데 위 `switch` 문에서 등장한 `break` 는 어디서 많이 본 것 같지 않습니까? 만약 그런 생각이 들었다면 당신은 C 언어 공부를 아주 충실히 하고 있다고 생각 됩니다. (만약 잘 모르겠다면 [여기](http://itguru.tistory.com/entry/%EC%94%B9%EC%96%B4%EB%A8%B9%EB%8A%94-C-%EC%96%B8%EC%96%B4-7-%EB%B1%85%EA%B8%80-%EB%B1%85%EA%B8%80-for-while)를 클릭하세요) break; 문을 실행하면 아래의 모든 `case` 들을 무시하고 `switch` 밖으로 빠져나가기 때문에 밥을 주었는데 강아지가 '아이 맛있어' 라고 할 일은 없게 됩니다.

하지만 만약 여러분이 `break;` 문을 빠뜨리게 되면 위와 같은 상황이 벌어질 수 있습니다.

```cpp-formatted
/* 실패작 */
#include <stdio.h>
int main() {
  int input;

  printf("마이펫 업그레이드\n");
  printf("무엇을 하실 것인지 입력하세요 \n");
  printf("1. 밥주기 \n");
  printf("2. 씻기기 \n");
  printf("3. 재우기 \n");

  scanf("%d", &input);

  switch (input) {
    case 1:
      printf("아이 맛있어 \n");

    case 2:
      printf("아이 시원해 \n");

    case 3:
      printf("zzz \n");

    default:
      printf("무슨 명령인지 못 알아 듣겠어. 왈왈 \n");
  }

  return 0;
}
```

성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F13554E114A8689A11652B4)

와 같이 웃지 않을 수 없는 상황이 벌어집니다. 여러분들이 1 을 입력한다면 `case 1:` 이 실행되어 그 내용들이 모두 실행되지만 `break` 문으로 `switch` 문을 빠져 나가지 못해서 아래 `case` 들 까지 줄줄이 실행되어 위와 같은 꼴을 볼 수 있습니다.

```cpp-formatted
/* 영어 말하기 */
#include <stdio.h>
int main() {
  char input;

  printf("(소문자) 알파벳 읽기\n");
  printf("알파벳 : ");

  scanf("%c", &input);

  switch (input) {
    case 'a':
      printf("에이 \n");
      break;

    case 'b':
      printf("비 \n");
      break;

    case 'c':
      printf("씨 \n");
      break;

    default:
      printf("죄송해요.. 머리가 나빠서 못 읽어요  \n");
      break;
  }

  return 0;
}
```

  성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F197F17254A868D363ED3F5)

와 같이 나옵니다.

사실, 여기에 의문이 드는 사람들도 있습니다. '아까 위에서 `switch` 문은 정수 데이터만 처리한다고 했는데 왜 여기서는 문자 데이터도 처리가 되는 것인가?' 그런데, 안타깝게도 이러한 의문이 5 초 이내로 해결되지 않으면 아마 앞에서 배운 내용을 까먹으셨을 것입니다. (그 내용을 보려면 [여기](http://itguru.tistory.com/entry/%EC%94%B9%EC%96%B4%EB%A8%B9%EB%8A%94-C-%EC%96%B8%EC%96%B4-3-%EB%B3%80%EC%88%98%EA%B0%80-%EB%AD%90%EC%A7%80)를 클릭하세요) 왜냐하면 컴퓨터는 문자와 숫자를 구분 못합니다. 컴퓨터는 문자를 모두 숫자로 처리한 뒤, 우리에게 보여줄 때 에만 문자로 보여주는 것이지요. 따라서, 문자 = 정수 라고 생각해도 거의 무방합니다.

이쯤 `switch` 문을 배우고 나면 드는 의문이 하나 있습니다.

"정말로 `switch` 문이 우리에게 필요한가? `if - else` 로 다 해결되는데 왜 귀찮게 `switch` 문을 만들었을까? 차이는 단지 겉으로 얼마나 깔끔한지가 다를 뿐인데... 내부적으로 `switch` 문과 `if-else` 와는 차이가 없나요?"

정말로, 훌륭한 생각이라고 생각합니다. 위 질문에 대한 답변을 정확하게 이해하려면 어셈블리어에 대한 이해가 필요로 합니다.
(참고로 `if` 문과 `switch` 문의 차이에 대한 설명을 자세하게 잘 다루는 곳 : [http://blog.naver.com/kki2406?Redirect=Log&logNo=80041410085](http://blog.naver.com/kki2406?Redirect=Log&logNo=80041410085)` )`

위에 링크 걸은 사이트에 들어가 내용을 모조리 이해한다면 더할 나위 없이 좋겠으나 아마 C 언어를 처음 배우는 사람들의 경우 거의 이해를 못할 것이니 제가 간단하게 설명 드리겠습니다. (만약 아래의 내용을 이해하지 못하더라고 그냥 넘어가세요. 사실 어셈블리어를 배우지 않은 이상 이해하기 힘듭니다)

![switch 문을 이용하여 case 1, case 2 등 쭉 코드를 짠 것입니다. ](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F1812271B4A8699234673BF)

`switch` 문 이용![if 문과 else if, else 문을 이용하여 코드를 짠 것입니다. 왼쪽의 코드와 동일합니다.](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F201F881B4A869924227727)

위 두 그림은 같은 소스 코드를 `switch` 문과 `if` 문을 이용하여 나타난 것입니다. 사실, 외형적으로 동작하는 것은 차이가 없습니다. 단지 내부적으로 어떻게 처리되냐가 다를 뿐이지요.

일단 `if` 문의 경우 각 경우 마다 값들을 비교 합니다. 위 경우 값을 3 번 비교하겠네요. 왜냐하면 `if` 가 1 번, `else if` 가 2 번이고 `else` 의 경우 값의 비교 없이 자동으로 처리되는 것이므로 총 3 번 비교하게 됩니다. 즉, `if` 문을 이용하면 각 `case` 의 경우 비교하게 되므로 최악의 경우 모든 `case` 에 대해 값을 비교하는 연산 (어셈블리어에서는 `CMP` 연산을 합니다.) 을 시행하게 됩니다.

그런데 `switch` 문은 사뭇 다릅니다. `switch` 의 경우 내부적으로 `jump table` 이라는 것을 생성합니다. 이 때, `jump table` 의 크기는 `case` 의 값들에 따라 달라지는데, 예를 들어서 어떤 `switch` 문의 경우 `case 1: ~ case` 10: 까지 있었다고 합시다. 그렇다면 `jump table` 에는 값들이 0 부터 9 까지 들어가게 됩니다. 여기서 우리는 왜 `case` 값: 할 때, '값' 부분에 변수가 위치하면 안되는지 알게 됩니다. `jump table` 은 프로그램 초기에 작성 되기 때문에 이미 `switch` 문이 실행되기 전에 `jump table` 이 작성되게 됩니다. 따라서, '값' 부분에 변수가 들어가게 되면 `jump table` 에 무엇이 올지 알 수 없으므로 변수를 사용하면 안되는 것입니다.

이 값들은 무엇을 의미하냐면 각 `case` 별로 명령들이 위치한 곳의 주소를 가리키는데 예를 들어서 1 인 지점으로 점프하게 되면 "아이 시원해" 가 나오고 0 인 지점으로 점프하게 되면 "아이 맛있어" 라고 출력하라는 내용의 명령문들이 나옵니다. 이제, 변수의 값에 따라 변수가 3 이라면 `jump table` 의 3 번째 원소를 찾아서 그 값에 해당하는 곳으로 점프하게 됩니다.

(실제로 `switch` 문이 처리되는 과정은 이보다 약간 더 복잡하지만 어셈블리어를 배우지 않은 현재 상황으로써는 최선이라 생각됩니다)

따라서, `switch` 문을 이용하면 `case` 에 따라 `CMP` 연산이 늘어나는 것이 아니라 `jump table` 의 크기만 커질 뿐 성능에 있어서는 전혀 영향을 받지 않게 됩니다.

결론적으로 이야기 하자면 `switch` 문이 효과적으로 처리되기 위해서는 `case` 의 '값' 들의 크기가 그다지 크지 않아야 하고, '값' 들이 순차적으로 정렬되어 있고, 그 '값' 끼리의 차이가 크지 않다면최고로 효율적인 `switch` 문을 이용할 수 있게 됩니다.

###  생각해 보기

#### 문제 1

`switch` 문의 '값' 부분에 왜 정수만 와야 되는지 아십니까?(난이도 : 中上)

#### 문제 2

앞서, `switch` 문이 내부적으로 처리 되는 부분에서 `case 1: ~ case 10:` 일 때 만 생각하였는데, 만약 `case 1:, case 3:, case 4:, case 10:` 과 같이 불규칙 적으로 `switch` 문이 적용된다면 컴퓨터는 `jump table` 를 어떻게 작성할까요 (난이도 : 最上)

##@ chewing-c-end