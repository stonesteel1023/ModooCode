----------------
title : 씹어먹는 C 언어 - <13 - 2. 마술 상자 함수 2 (function)>
cat_title : 13 - 2. 마술 상자 함수 2 (function)
next_page : 28
publish_date : 2009-12-19
--------------


이번 강좌에서는

* 포인터로 받는 인자

* 함수의 원형

* 배열을 인자로 받기

![씹어먹는 C 언어](/img/ChewingClogo.png)


안녕하세요 여러분. 이전에 함수에 대해선 잘 이해하셨는지요? 그리고, 마지막에 던진 의미 심장한(?) 질문에는 답을 구하셨나요? 우리는 이전 12 강에서 포인터에 대해서 다루어왔습니다. 그 때 동안 늘 머리속에 맴돌았던 생각은 "도대체 이거 어따가 써먹는거야?" 였죠. 하지만, 이번 강좌에서 그 질문에 대한 해답을 찾을 수 있기 바랍니다.

일단, 간단히 이전에 포인터에 대해서 배웠던 내용을 리뷰 하자면

포인터는 특정한 변수의 메모리 상의 주소값을 저장하는 변수로, `int` 형 변수의 주소값을 저장하면 `int*, char` 이면 `char*` 형태로 선언된다. 또한 `*` 단항 연산자를 이용하여, 자신이 가리키는 변수를 지칭할 수 있으며 `&` 연산자를 이용하여 특정한 변수의 주소값을 알아낼 수 있다.

만일 위 내용중에 한 마디라도 이해가 안되는 부분이 있다면 [12 강 포인터 강좌](http://itguru.tistory.com/23)를 다시 읽어 보시기를 강력하게 권합니다. 그렇지 않다면 아래의 내용을 계속 읽어가도록 하죠. 우리는 지난 강좌에서 다음과 같이 단순한 형태로는 다른 함수에서 정의된 변수의 값을 바꿀 수 없다고 했습니다.

```cpp-formatted
/* 이상한 짓 */
#include <stdio.h>
int change_val(int i) {
  i = 3;
  return 0;
}
int main() {
  int i = 0;

  printf("호출 이전 i 의 값 : %d \n", i);
  change_val(i);
  printf("호출 이후 i 의 값 : %d \n", i);

  return 0;
}
```


왜 `main` 함수 안에서 정의된 `i` 의 값이 바뀌지 않는지는 잘 아시겠지만 그래도 한 번 확인해봅시다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F17797D264B2784B213E5BE)

`i` 의 값이 전혀 바뀌지 않았음을 알 수 있습니다. 그 이유는 함수 `change_val` 을 호출 할 때, `change_val` 함수 안에서 정의된 변수 `i` 는 `main` 함수의 `i` 의 값을 전달 받은 후에, `change_val` 함수 안에서 정의된 변수 `i` 의 값을 3 으로 변경하게 됩니다. 여기서 중요한 점은 'main 함수의 `i` 가 아닌 `change_val` 함수 안에서 정의된 변수 `i` 의 값이 3 으로 변경' 된다는 것이지요. 결론적으로 `main` 함수의 `i` 의 값에는 아무런 영향도 미치지 못하고 위와 같은 현상이 벌어지는 것입니다.

위 과정을 그림으로 표현하면 아래와 같습니다.


![main 에서 int i 를 정의하였다. 이제 change_val 을 호출하면 chagne_val 자체의 int i 로 i 의 값이 전달 된다. 이제, change_val 의 i 의 값을 3 으로 변경한다. 물론 main 의 i 와는 다른 변수 이기 때문에 return 후 다시 main 에서 i 의 값을 확인하면 그대로 0 이다.](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F1101E7024B2787A13420C3)

하지만, 여러분은 지난 3 개의 강좌를 통해 포인터에 대해 귀가 아플 만큼 들어 보았을 것입니다. 그리고, 여기에서 그 아이디어를 적극적으로 활용하고자 합니다. 이전의 방법을 통해서 다른 함수에 정의된 변수들의 값을 변경할 때 직면했던 문제는 바로 각 함수는 다른 함수의 변수들에 대해 아는 것이 아무것도 없다는 것이였습니다. 즉 `A` 라는 함수에서 `i` 라는 변수를 이용한다면 컴파일러는 이 변수 `i` 가 오직 `A` 함수에서만 정의되었다고 생각하지 다른 함수에서 정의되었는지는 상관하지 않다는 것입니다.

그렇지만 궁여지책으로 유일하게 가능했던 것은 인자를 이용해서 다른 함수에 정의된 변수들의 '값' 을 전달하는 것이였습니다. 하지만 그렇게 해도 여전히 불가능해 보였습니다.

```cpp-formatted
/* 드디어 써먹는 포인터 */
#include <stdio.h>
int change_val(int *pi) {
  printf("----- chage_val 함수 안에서 -----\n");
  printf("pi 의 값 : %d \n", pi);
  printf("pi 가 가리키는 것의 값 : %d \n", *pi);

  *pi = 3;

  printf("----- change_val 함수 끝~~ -----\n");
  return 0;
}
int main() {
  int i = 0;

  printf("i 변수의 주소값 : %d \n", &i);
  printf("호출 이전 i 의 값 : %d \n", i);
  change_val(&i);
  printf("호출 이후 i 의 값 : %d \n", i);

  return 0;
}
```


  성공적으로 컴파일 하면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F1811EC054B278ADA18779C)

여러분의 출력결과와 다를 수 있습니다.

헉! 눈으로 보고도 믿기지 않으십니까? 호출 이후의 `i` 의 값이 0 에서 3 으로 바뀌었습니다~~ 이게 무슨일 입니까? 이건 우리가 여태까지 꼭 하고야 말겠던 바로 그 작업 아닙니까. 바로 다른 함수에서 정의된 변수의 값을 바꾸는 것 말이죠. 그런데, 위 코드를 조금씩 뜯어 들여보다 보면 방법은 매우 간단하다는 것을 알 수 있습니다. 물론, 이 강의를 보고 계시는 일부 똑똑한 독자들은 이미 짐작 했을 것이지만요.

```cpp-formatted
int change_val(int *pi)
```


일단, 함수의 정의부분을 살펴보자면 `int` 형의 변수를 가리키는 `pi` 라는 이름의 포인터로 인자를 받고 있습니다. 그리고 `main` 함수에서 이 함수를 어떻게 호출했는지 보면

```cpp-formatted
change_val(&i);
```

즉, 인자에 `main` 함수에서 정의된 `i` 라는 변수의 '주소값' 을 인자로 전달하고 있습니다. 따라서  `change_val` 함수를 호출하였을 때 `pi` 에는 `i` 의 주소값이 들어가게 됩니다. 즉, `pi` 는 `i` 를 가리키게 됩니다.

```cpp-formatted
{
  printf("----- chage_val 함수 안에서 -----\n");
  printf("pi 의 값 : %d \n", pi);
  printf("pi 가 가리키는 것의 값 : %d \n", *pi);

  *pi = 3;

  printf("----- change_val 함수 끝~~ -----\n");
  return 0;
}
```

`pi` 가 `i` 의 주소값을 가지고 있으므로 `pi` 를 출력했을 때 그 값은 `i` 의 주소값과 같을 수 밖에 없습니다. 이는 두 번째 `printf` 문장에서 확인할 수 있습니다. 또한 그 아래 `*pi` 를 통해서 `i` 를 간접적으로 접근할 수 있습니다. 왜냐하면 `*` 라는 단항 연산자의 의미가 '내가 가지는 주소값에 해당하는 변수를 의미해라' 이기 때문에 `*pi` 는 `pi` 가 가리키고 있는 변수인 `i` 를 의미할 수 있게 됩니다. 즉, `pi` 를 통해서 굳게 떨어져 있던 `main` 과 `change_val` 함수의 세계 사이에 다리가 놓이게 되는 것이지요.

간혹 `pi` 가 `main` 함수에서 정의된 것이라고 착각하는 분들이 있는데, `pi` 역시 `change_val` 함수 내에서 정의된 변수 입니다.

또한 `*pi = 3` 을 통해 'pi 가 가리키고 있는 변수' 의 값을 3 으로 변경할 수 있습니다. 여기서 `pi` 가 `i` 를 가리키므로 `i` 의 값을 3 으로 변경할 수 있겠네요. 따라서,

```cpp-formatted
printf("호출 이후 i 의 값 : %d \n", i);
```

에는 `i` 의 값이 성공적으로 변경되어 3 이 출력되는 것입니다. 위 과정을 그림으로 나타내면 아래와 같습니다.


![main 함수에 변수 i 가 있다. change_val 에 i 의 주소값을 전달한다. change_val 은 포인터 pi 에 전달 받은 i 의 주소값이 들어가 있다. 이제, pi 가 가리키는 것의 값을 3 으로 바꾸면, pi 가 가리키는 것이 main 의 변수 i 였으므로 실제로 return 후 확인해 보면 main 의 변수 i 의 값이 바뀐다.](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F1836411A4B279039965794)

```cpp-formatted
/* 두 변수의 값을 교환하는 함수 */
#include <stdio.h>
int swap(int a, int b) {
  int temp = a;

  a = b;
  b = temp;

  return 0;
}
int main() {
  int i, j;

  i = 3;
  j = 5;

  printf("SWAP 이전 : i : %d, j : %d \n", i, j);

  swap(i, j);  // swap 함수 호출~~

  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
```

  성공적으로 컴파일 했으면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F1155830F4B2791D864F629)

흠. 일단 우리가 원하던 결과가 나오지 않았습니다. 소스 상단의 주석에서도 볼 수 있듯이 `swap` 함수는 두 변수의 값을 교환해 주는 함수 입니다. 우리가 원하던 것은 `SWAP` 이후에  `i` 에는 5 가 `j` 에는 3 이 들어 있는 것인데 전혀 바뀌지 않았습니다. 이에 대해 이야기 하기 전에 소스 코드에서 보이는 새로운 것들에 대해 이야기 해봅시다.

```cpp-formatted
int swap(int a, int b)
```

`swap` 함수의 정의를 보면 직관적으로 인자가 2 개나 있다는 것을 알 수 있습니다. 맞습니다. 이 `swap` 함수는 호출시 2 개의 인자를 전달해주어야 합니다. 물론 인자가 더 늘어난다면 반점(,) 을 이용해서 계속 늘려나가면 됩니다. 예를 들어서

```cpp-formatted
int this_function_has_many_argumenets(int a, char b, int* k, long d, double c,
                                      int aa, char bb, int* kk, double cc)
```

  와 같이요. 아무튼, `swap` 함수를 살펴 보면

```cpp-formatted
int swap(int a, int b) {
  int temp = a;

  a = b;
  b = temp;

  return 0;
}
```

로 두 개의 `int` 형 인자를 받아 들이고 있습니다. 이 때, 내부를 보면 `temp` 라는 변수에 `a` 의 값을 저장합니다. 그리고 변수 `a` 에 변수 `b` 의 값을 넣습니다. 이제, 변수 `b` 에 `a` 의 값을 넣어야 하는데, 현재 변수 `a` 에는 `b` 의 값이 이미 들어가 있으므로 이전에 저장하였던 `a` 의 값인 `temp` 변수의 값을 `b` 에 넣으면 됩니다. 일단, 내용상으로는 전혀 하자가 없어 보입니다.

```cpp-formatted
printf("SWAP 이전 : i : %d, j : %d \n", i, j);

swap(i, j);  // swap 함수 호출~~

printf("SWAP 이후 : i : %d, j : %d \n", i, j);
```

그런데, 말이죠. `main` 함수에서 `i,j` 의 값을 바꾸려고 `swap` 함수를 호출하였더니 전혀 뒤바뀌지 않은 채로 출력되었습니다. 도대체 왜 그런가요? 물론, 여러분은 다 알고 있겠지요. `swap` 함수의 변수 `a,b` 가 모두 `swap` 함수 내부에서 선언된 변수들이란 것입니다. 다시말해 변수 `a` 와 `b` 는 `i` 와 `j` 와 어떠한 연관도 없습니다. 다만, `a` 와 `b` 의 초기값이 `i, j` 와 동일하였다는 것만 빼고요.

이는 마치 아래의 작업을 한 것과 같습니다.

```info
    int i, j;
    int temp, a, b;
    /* 함수를 호출하여 함수의 인자를 전달하는 부분 */
    a = i;
    b = j;
    /* 함수 몸체의 내용을 실행 */
    temp = a;
    a = b;
    b = temp;
```

그러니 `i` 나 `j` 의 값이 바뀔리 만무하죠. 아무튼, 위 함수가 호출되는 과정을 그림으로 표현하면 아래와 같습니다.


![main 에서 int i,j 를 정의하며 swap 에 넣으면 swap 의 int a,b 는 각각 swap 내의 변수들 이므로, swap 내에서 아무리 a,b 를 바꿔보았자 main 의 i,j 는 바꾸지 않는다. 결국 역시 포인터를 이용해야 한다.](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F1358AE044B28794034405F)

  그렇다면 어떻게 해야 할까요? 다 알고 있겠죠? 포인터를 이용합시다~~

```cpp-formatted
/* 올바른 swap 함수 */
#include <stdio.h>
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
int main() {
  int i, j;

  i = 3;
  j = 5;

  printf("SWAP 이전 : i : %d, j : %d \n", i, j);

  swap(&i, &j);

  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
```

  성공적으로 컴파일 하면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile29.uf.tistory.com%2Fimage%2F181E71014B2879A8A8E568)

오오오.. 드디어 우리가 원하던 것이 이루어졌습니다. 바로 `i` 와 `j` 의 값이 서로 뒤바뀐(swap) 것이지요. 아.. 정말 기쁩니다. 그런데, 이전에 이야기 하였던 내용을 잘 숙지하였더라면 위 함수가 왜 제대로 호출하는지 쉽게 알 수 있습니다.

```cpp-formatted
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
```

먼저 `swap` 함수를 살펴 봅시다. 이는 `int` 형을 가리키는 포인터 변수를 인자로 가지고 있습니다. 일단, `swap` 함수 내에서 두 변수를 교환하는 과정은 위와 동일하니 이에 대해서는 이야기 하지 않도록 하겠습니다. 이 때, `main` 함수에서는 `swap` 함수를 아래와 같이 호출합니다.

```cpp-formatted
printf("SWAP 이전 : i : %d, j : %d \n", i, j);

swap(&i, &j);  // 호출

printf("SWAP 이후 : i : %d, j : %d \n", i, j);
```

바로 `a` 와 `b` 에 `i` 와 `j` 의 주소값을 전달하여 `a` 와 `b` 로 하여금 `i` 와 `j` 를 가리키게 만든 것입니다. 따라서, `swap` 함수 내부에서는 `a` 와 `b` 의 값을 교환하는 것이 아니라 `a` 와 `b` 가 가리키는 두 변수의 값을 교환했으므로 `(*a, *b)` 결과적으로 `i` 와 `j` 의 값이 바뀌게 된 것입니다. 어때요, 간단하지요?

  결론적으로 정리하자면

```warning
어떠한 함수가 특정한 타입의 변수/배열의 값을 바꾸려면 함수의 인자는 반드시 그 타입을 가리키는 포인터를 이용해야 한다!
```

포인터를 인자로 받은 함수에 대해선 지속적으로 이야기 할 것이므로 지금 막상 이해가 잘 안된다고 해도 큰 걱정할 필요는 없습니다.



###  함수의 원형

우리가 여태까지 사용하였던 함수들은 모두 `main` 함수 위에서 정의되고 있었습니다. 그러면, 그 정의를 `main` 함수 아래에서 한다면 어떻게 될까요? 사실, 대부분의 사람들의 경우 `main` 함수를 제일 위에 놓고 나머지 함수들은 `main` 함수 뒤에 정의하게 됩니다. 아무튼, 위의 코드를 살짝 바꿔보면 아래와 같습니다.

```cpp-formatted
/* 될까? */
#include <stdio.h>
int main() {
  int i, j;
  i = 3;
  j = 5;
  printf("SWAP 이전 : i : %d, j : %d \n", i, j);
  swap(&i, &j);
  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
```

  컴파일 하게 되면 아래와 같은 경고 창을 볼 수 있습니다.

```warning
warning C4013: 'swap'이(가) 정의되지 않았습니다. extern은 int형을 반환하는 것으로 간주합니다.
```

  흠, 일단은 무시하고 실행해 보도록 하죠.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F193957054B28F5AA356F43)

어랏, 잘만 됩니다. 그렇다면 아무런 문제가 없는 것일까요? 사실, 함수를 적절히 잘 이용하기만 하면 큰 문제는 발생하지 않습니다. 그런데 말이죠. 사람도 역시 사람인지라, 프로그래밍 하다가 실수로 인자의 개수를 부족하게 쓰거나, 올바르지 않는 타입의 변수 (예를 들어 인자가 `int*` 인데, `int` 변수를 썼다든지) 를 사용하는 수가 발생하게 됩니다. 더군다나, 우리의 예제에서는 함수가 겨우 한 개 밖에 없었지만 실제 프로그래밍 시에는 수십개의 함수를 이용하기 때문이죠. 그렇다면, 여러분이 완벽한 인간이 아니라는 가정 하에 인자 하나를 누락시켜 봅시다.

위 코드의 함수 호출 부분을

```cpp-formatted
`swap(&i,` &j);
```

에서

```cpp-formatted
swap(&i);
```

로 변경해봅시다.

 컴파일 하면 여전히 위와 동일한 경고가 나오는데 특별히 내가 인자를 누락 했다는 말은 하지 않습니다. 그리고, 실행해보면


![오류!!](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F2058CD244B28F6B3757FDA)

  허걱! 컴파일시 아무런 오류 메세지도 없었는데 실행해 보면 위와 같이 덜컹 오류가 나타납니다. 이런 해괴한 일이 아닐 수 없군요. 게다가, 컴파일러는 내가 인자를 어디서 인자를 누락했는지 조차 표시해주지 않기 때문에 오류를 찾기 힘들어 질 수 밖에 없습니다. 물론, 우리의 예제는 짧기 때문에 찾기 쉽지만 진짜 같은 프로그램을 제작하면 코드가 보통 수천~수만 줄에 달한다는 것만을 기억하세요.

이번에는 `swap` 함수 호출 부분을 `swap(&i, j);` 로 변경해보세요.


![오류!!](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F11259D264B28F73D04A618)

뜨아아. 역시 이번에도 동일한 형태의 프로그램 오류가 컴파일시 오류 하나 없었는데도 불구하고 나타났습니다. 이 역시 포인터 전달 해야 되는데, 그냥 정수값을 전달해서 포인터 `b` 가 메모리의 올바르지 않은 공간에 접근하여 발생한 일입니다. 참으로 곤욕스러운 일이 아닐 수 없습니다. 우리가 아무리 대단하다고 해도 실수를 할 수 있는 법인데, 컴파일러는 이러한 실수를 하나도 잡아내지 못하고 있습니다.

그러나, 우리의 C 언어가 이를 용납할 수 있나요? C 언어에서는 멋진 해결책이 있습니다. 바로, 함수의 **원형(prototype)** 를 이용하는 것입니다.

```cpp-formatted
/* 함수의 원형 */
#include <stdio.h>
int swap(int *a, int *b);  // 이 것이 바로 함수의 원형
int main() {
  int i, j;
  i = 3;
  j = 5;
  printf("SWAP 이전 : i : %d, j : %d \n", i, j);
  swap(&i, &j);
  printf("SWAP 이후 : i : %d, j : %d \n", i, j);

  return 0;
}
int swap(int *a, int *b) {
  int temp = *a;

  *a = *b;
  *b = temp;

  return 0;
}
```

  성공적으로 컴파일 하면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F1450EB274B28F80D374EDF)

오, 역시 잘 출력됩니다. 이번에는 컴파일시 경고나 오류의 흔적 조차 찾아볼 수 없었습니다.

```cpp-formatted
#include <stdio.h>
int swap(int *a, int *b);  // 이것이 바로 함수의 원형
int main() {
  int i, j;
  i = 3;
  j = 5;
  // ... (생략)
```

소스 코드의 제일 윗부분을 보면 위와 같이 한 줄이 추가된 것을 볼 수 있습니다. 이는 바로 '함수의 원형' 이라 부르는 것입니다. 이는 사실 함수의 정의 부분을 한 번 더 써준 것 뿐입니다 (주의할 점은 함수의 원형에는 정의와는 달리 뒤에 ; 를 붙인 다는 것입니다). 그런데, 이 한줄이 컴파일러에게 다음과 같은 사실을 알려줍니다.

  "야, 이 소스코드에 이러 이러한 함수가 정의되어 있으니까 잘 살펴봐"

다시말해, 컴파일러에게 이 소스코드에 사용되는 함수에 대한 정보를 제공하는 것입니다. 다시 말해 실제 프로그램에는 전혀 반영되지 않는 정보지요. 그렇지만, 우리가 앞서 하였던 실수들을 하지 않도록 도와줍니다. 만일, 위와 같이 함수의 원형을 삽입한 상태에서 인자를 `&i` 하나로 지워 봅시다. 즉, `swap(&i, &j)` 를 `swap(&i);` 로 변경해봅시다.

  그럼 컴파일 시 아래와 같은 오류를 만나게 됩니다.

```warning
 error C2198: 'swap' : 호출에 매개 변수가 너무 적습니다.
```

와우! 우리가 앞서 함수의 원형을 집어 넣지 않았을 때 에는 인자(매개 변수)를 하나 줄여도 아무말 하지 않던 컴파일러가 원형을 삽입하고 나니 위와 같이 정확한 위치에 내가 어딜 잘못했는지 잡아냅니다. 이것이 가능한 이유가 바로 컴파일러에게 내가 무슨 무슨 함수를 이용할 것인지 함수의 원형을 통해 이야기 하였기 때문입니다. 내가, `int swap(int *a, int *b)` 라는 함수가 있다는 것을 원형을 이용해 알려주었기 때문에 컴파일러는 우리가 `swap` 함수를 사용하면 꼭 2 개의 인자를 이용한다는 사실을 알게 되어 내가 인자를 하나만 적었을 때 틀렸다고 알려 준 것입니다.

그렇다면 `swap(&i, &j)` 를 `swap(&i, j)` 로 바꿔보면 어떻게 될까요?

```warning
warning C4047: '함수' : 'int *'의 간접 참조 수준이 'int'과(와) 다릅니다.
warning C4024: 'swap' : 형식 및 실제 매개 변수 2의 형식이 서로 다릅니다.
```

실질적인 오류는 발생하지 않았지만 일단, 내가 잘못하였다는 것을 알려줍니다. 컴파일러는 역시 원형을 통해 두 번째 매개 변수의 타입이 무엇인지 알고 있기에 그냥 `int` 를 사용하면 함수의 두번째 매개변수와 내가 인자에 전달하는 변수의 형과 다르다는 사실을 알려 줍니다. 다만, 여기서 아까와 같이 오류가 출력되지 않는 이유는 `int*` 도 사실 `int` 형 데이터 이기 때문에 `j` 가 `(int *)` 로 캐스팅 되어 전달되므로, 아까와 같은 강한 오류 메세지는 출력되지 않습니다. 그러나, 여전히 프로그래머의 잘못을 지적하고 있습니다.

이러한 연유에서, 함수의 원형을 집어넣는 일은 여러분들이 '반드시' 하셔야 되는 일입니다. 물론, `main` 함수 위에 함수를 정의하면 상관 없지만 사실 `99.9%` 의 프로그래머들은 함수를 `main` 함수의 뒤에 정의하고 원형을 앞에 추가하는 것을 선호하니 여러분들도 트렌드를 따르시기 바랍니다.



###  배열을 인자로 받기

이번에는 배열을 인자로 받아 들이는 함수에 대해서 생각해봅시다. 이번 예제에서 우리가 만들게 된 함수는 바로, 배열을 인자로 받아서 그 배열의 각 원소의 값을 1 씩 증가시키는 함수 입니다.

```cpp-formatted
#include <stdio.h>

int add_number(int *parr);
int main() {
  int arr[3];
  int i;

  /* 사용자로 부터 3 개의 원소를 입력 받는다. */
  for (i = 0; i < 3; i++) {
    scanf("%d", &arr[i]);
  }

  add_number(arr);

  printf("배열의 각 원소 : %d, %d, %d", arr[0], arr[1], arr[2]);

  return 0;
}
int add_number(int *parr) {
  int i;
  for (i = 0; i < 3; i++) {
    parr[i]++;
  }
  return 0;
}
```

  성공적으로 컴파일 했으면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F143DB51F4B29C0FE38D124)

음, 역시 함수가 잘 작동하는 군요. 우리가 `10, 11, 15` 를 입력했을 때, 함수를 통해서 각 원소가 1 씩 증가하여 `11, 12, 16` 이 되었습니다. 일단, `add_number` 함수 부터 살펴 보도록 하죠.

```cpp-formatted
int add_number(int *parr)
```

우리가, 앞서 말한 내용에 따르면 '특정한 타입의 값을 변경하는 함수를 제작하려면, 반드시 그 타입을 가리키는 포인터를 인자로 가져야 한다' 라고 했습니다. 그렇다면, 우리가 `arr` 이라는 배열을 가리키는 포인터가 바로 `add_number` 의 인자로 와야 하는데, 우리가 `12 - 3` 강에서 배운 내용에 따르면 `int arr[3]` 와 같은 일차원 배열을 가리키는 포인터는 바로 `int*` 형이라 했습니다. (잘 모르겠다면 [여기를 눌러서 강의](http://itguru.tistory.com/25)를 다시 보시기 바랍니다)

따라서, `add_number(int *parr)` 이라 하면 `arr` 을 가리키도록 인자를 받을 수 있습니다. 함수를 호출 할 때 아래와 같이 하였습니다.

```cpp-formatted
add_number(arr);
```

그런데, 우리가 이전에 배운 바에 따르면 `arr` 은 배열의 시작 주소 값을 가지고 있다고 하였습니다. 즉, `arr = &arr[0]` 인 것이지요. 따라서, `parr` 에는 `arr` 배열의 시작 주소, 즉 배열 `arr` 을 가리키게 됩니다.

```cpp-formatted
{
  int i;
  for (i = 0; i < 3; i++) {
    parr[i]++;
  }
  return 0;
}
```

마지막으로 함수의 몸체를 살펴봅시다. `parr[i]` 를 통해 `parr` 이 가리키는 배열의 `(i + 1)` 번째 원소에 접근할 수 있습니다 (`arr[1]` 이 배열의 두 번째 원소 이므로). 따라서, `parr[i]++` 을 통해서 배열의 각 원소들의 크기를 모두 1 씩 증가시키게 됩니다. 사실, 위 함수가 어떻게 돌아가는지 잘 이해하기 위해서는 포인터와 배열에 대한 거의 완벽한 이해를 필요로 합니다. 만약 그러지 않는다면 모래사장에 빌딩 짓는 것처럼, C 언어에 대한 개념을 완전히 잊어버릴 수 있으니 모른 다면 꼭 뒤로 가기를 하여 복습을 하시기 바랍니다.

```cpp-formatted
/* 입력 받은 배열의 10 개의 원소들 중 최대값을 출력 */
#include <stdio.h>
/* max_number : 인자로 전달받은 크기 10 인 배열로 부터 최대값을 구하는 함수 */
int max_number(int *parr);
int main() {
  int arr[10];
  int i;

  /* 사용자로 부터 원소를 입력 받는다. */
  for (i = 0; i < 10; i++) {
    scanf("%d", &arr[i]);
  }

  printf("입력한 배열 중 가장 큰 수 : %d \n", max_number(arr));
  return 0;
}
int max_number(int *parr) {
  int i;
  int max = parr[0];

  for (i = 1; i < 10; i++) {
    if (parr[i] > max) {
      max = parr[i];
    }
  }

  return max;
}
```

  성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F141500234B29C0F0734344)

이번 예제는 사용자들로 부터 정수 10 개를 입력 받아서, 그 수들 중 가장 큰 수를 뽑아내는 프로그램 입니다. 먼저 `max_number` 함수 부터 살펴봅시다.

```cpp-formatted
int max_number(int *parr) {
  int i;
  int max = parr[0];

  for (i = 1; i < 10; i++) {
    if (parr[i] > max) {
      max = parr[i];
    }
  }

  return max;
}
```


음.. 일단, 소스 코드를 해석하는데에는 큰 어려움이 없을 것 같네요. 일단 처음 `max` 에 `parr` 이 가리키는 배열의 `[0],` 즉 첫번째 원소의 값을 넣었습니다. 그리고 아래 `for` 문에서 만약 `parr[i]` 가 `max` 보다 크면 `max` 의 값을 `parr[i]` 로 대체하고 있군요. 결과적으로 `i` 값이 9 까지 되었을 때에는 `max` 에 `parr` 중 가장 큰 원소의 값이 들어가게 됩니다. 만일, `max` 보다 더 큰 원소가 `parr` 에 있다면 `max` 의 값은 그 큰 원소의 값으로 바뀌었기 때문에 모순이지요.

  결과적으로 우리가 입력한 10 개의 원소들 중 가장 큰 원소가 출력됩니다.

###  함수 사용 연습하기


사실, 아직까지 함수가 왜 이리 중요한 것인지 감이 잘 오지 않는 분들이 있을 것입니다. 그래서, 그러하신 분들을 위해 함수의 중요성을 절실히 느낄 수 있는 예제를 준비하였습니다.

  다음의 두 소스 코드를 비교해 보면서 어떤 것이 나은지 생각해보세요

```cpp-formatted
/* 함수를 이용하지 않은 버전 */
#include <stdio.h>
int main() {
  char input;

  scanf("%c", &input);

  if (48 <= input && input <= 57) {
    printf("%c 는 숫자 입니다 \n", input);
  } else {
    printf("%c 는 숫자가 아닙니다 \n", input);
  }

  return 0;
}
```


```cpp-formatted
/* 함수를 이용한 버전 */
#include <stdio.h>
int isdigit(char c);  // c 가 숫자인지 아닌지 판별하는 함수
int main() {
  char input;

  scanf("%c", &input);

  if (isdigit(input)) {
    printf("%c 는 숫자 입니다 \n", input);
  } else {
    printf("%c 는 숫자가 아닙니다 \n", input);
  }

  return 0;
}
int isdigit(char c) {
  if (48 <= c && c <= 57) {
    return 1;
  } else
    return 0;
}
```

 일단, 첫번째 소스의 경우 길이가 짧습니다. 다만 이해하기가 힘듧니다.

```cpp-formatted
if (48 <= input && input <= 57) {
}
```

`printf` 문이 없다고 했을 때 위 코드가 `input` 이 숫자인지 아닌지 판별하는지 쉽게 구분이 가나요? 이는 특별히 주석을 넣지 않는 한 매우 어렵습니다. 사실, 숫자의 경우 아스키 코드의 값이 48 에서 57 이기 때문에 위 코드를 사용하였는데 아스키 코드표를 외우고 다니지 않는 한 이해하기 상당히 어렵습니다.

  그렇다면 함수를 이용한 버전을 살펴 봅시다.

```cpp-formatted
if (isdigit(input)) {
}
```

일단 `isdigit` 라는 이름만 보고도 이 함수는 `input` 이 숫자 인지 아닌지 (is digit? ) 판별하는 함수 임을 알 수 있습니다. 물론, `isdigit` 함수 내부에도 첫번째 소스와 동일한 과정이 진행되지만 이 함수가 무슨 작업을 하는지 알기 때문에 소스를 이해하기 훨씬 쉬워집니다. 뿐만 아니라, 어떠한 문자가 숫자인지 반복해서 확인하는 경우에도 함수를 이용하면 편히 사용할 수 있습니다.

  아직까지도 왜 함수를 써야 하는지 모르겠다고 해서 큰 문제는 아닙니다. 나중에 가면 자연스럽게 깨닫게 될 것입니다. 그럼, 이번 강의는 여기까지에서 줄이겠습니다.

### 생각 해보기

#### 문제 1

위 10 개의 원소들 중 최대값 구하는 함수를 이용하여, 10 개의 원소를 입력 받고 그 원소를 큰 순으로 출력하는 함수를 만들어보세요. (난이도 : 中)

#### 문제 1

2 차원 배열의 각 원소에 1 을 더하는 함수의 인자는 어떤 모양일까요? (난이도 : 中下 2 차원 배열의 각 원소에 1 을 더하는 함수의 인자는 어떤 모양일까요? (난이도 : 中下)

##@ chewing-c-end