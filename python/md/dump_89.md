----------------
title : 씹어먹는 C 언어 - <19. main 함수의 인자, 텅 빈 void 형>
cat_title : 19. main 함수의 인자, 텅 빈 void 형
next_page : 98
publish_date : 2010-08-02
--------------


이번 강좌에서는

* `void` 형의 함수, `void` 형의 포인터에 대한 이해

* `main` 함수의 인자에 대한 이해 (argc, argv)

* 포인터 배열

![씹어먹는 C 언어](/img/ChewingClogo.png)


안녕하세요 여러분. 그동안 잘 지내셨는지요? 책 만드는 것도 어느 정도 진척이 되었고 `Latex` 도 어느정도 능숙하게 다룰 줄 알아서 꽤 괜찮게 만들 수 는 있었는데 표지가 문제네요. 혹시 '씹어먹는 C 언어' 를 위한 멋진 표지를 만드실 분을 찾고 있으니 혹시 좋은 아이디어가 있으신 분들은 kev0960@gmail.com 으로 꼭 메일을 보내주시기 바랍니다.

만일 여러분이 다른 곳에서 C 를 배웠더라면 다음과 같은 것을 보셨을 수 도 있습니다.

```cpp-formatted
/* 특별한 hello world */
#include <stdio.h>

void main() { printf("Hello, World! \n"); }
```


성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F1747A5304C4FE429165D46)

일단, 위 소스 코드에서 살펴볼 부분은 두 가지 입니다. 먼저 함수의 정의 부분을 보면

```cpp-formatted
void main()
```


입니다. 우리가 `int main()` 이라 하는 것 처럼 이 역시 'void 형을 리턴하는 `main` 함수' 라고 보시면 되겠습니다. 그런데 `void` 형이 뭔가요? 놀랍게도 이 함수는 `return` 하는 값이 없습니다. 보통 `int main()` 의 경우 마지막에 `return` 0; 와 같이 반드시 정수값을 반환해 주어야 하는데 이 함수는 리턴하는 값이 없음에도 불구하고 아무런 오류가 뜨지 않습니다.

여기서 바로 `void` 형이 뭔지 알 수 있습니다. `void` 란'아무 형(타입)도 아닌' 이란 뜻으로 생각하시면 됩니다. 즉, 이 함수는 아무런 값도 리턴하지 않습니다. (오히려 값을 리턴하게 되면 오류가 나게 됩니다) 실제로 영어에서도 'void' 라는 단어의 의미는 '텅빈, 공허한' 이란 뜻입니다.

이렇게 `void` 형 함수는 아무것도 리턴하지 않으므로 다음과 같은 문장은 모두 틀린 셈입니다.

```cpp-formatted
void a();
int main() {
  int i;
  i = a();

  return 0;
}

void a() {}
```


즉 함수 `a` 가 리턴하는 값이 없으므로 `main` 함수의 변수 `i` 의 값에 `a` 의 리턴값을 대입할 수 없습니다. 이 모두 오류로 처리됩니다.

`void` 형 변수는 많은 곳에서 사용 됩니다. 주로, '리턴을 할 필요가 없는 함수' 들의 경우가 대부분이죠. 예를 들어서 두 변수의 값을 교환하는 함수를 생각해봅시다. 아마 여러분은 여태까지 다음과 같이 함수를 만들었을 것입니다.

```cpp-formatted
int swap(int *a, int *b) {
  int temp;

  temp = *a;
  *a = *b;
  *b = temp;

  return 0;
}
```

하지만 `swap` 함수는 리턴할 필요가 전혀 없죠. 단순히 두 수의 값만 바꾸면 끝인데 뭐하러 귀찮게 리턴을 하냐 말이죠. 오히려 불필요한 `return` 0; 를 수행할 시간 동안 다른 작업을 하는 것이 훨씬 효율적이라 생각됩니다. 이렇게 `return` 문이 불필요한 경우 `void` 함수를 사용하면

```cpp-formatted
void swap(int *a, int *b) {
  int temp;

  temp = *a;
  *a = *b;
  *b = temp;
}
```


로 깔끔하게 만들 수 있습니다.
이렇게 굳이 리턴을 할 필요가 없는 곳에서 `void` 함수를 이용하는 것이 효율적이라 볼 수 있습니다.



###  void 형 변수




```cpp-formatted
/* void 형 변수?? */
#include <stdio.h>
int main() {
  void a;

  a = 3;

  return 0;
}
```


성공적으로 컴파일 하였다면

```warning
error C2182: 'a' : 'void' 형식을 잘못 사용했습니다.
```


와 같은 오류 메세지를 보게 됩니다. 우리가 위에서 `void` 형 함수에 대해 살펴 보았습니다. 그렇다면 `void` 형의 변수도 정의할 수 있을 것 같은데 사실 이는 오류 입니다. 컴파일러가

```cpp-formatted
int a;
```


라는 문장을 보게 된다면 컴파일러는 '아, `int` 형의 변수 `a` 를 선언하는 구나. 메모리 상에 미리 4 바이트의 공간을 마련해 놓아야지' 라고 생각할 것입니다. 그런데

```cpp-formatted
void a;
```


를 보게 된다면, '응? 이 변수의 타입은 뭐지?' 라고 생각하게 되죠. 다시 말해 이 변수를 위해서 메모리 상에 얼마나 많은 공간을 설정해 놓아야 하는지 모르게 되는 셈입니다. (참고로 컴파일 때 모든 변수들의 메모리 상의 위치가 결정 되어야 합니다) 따라서 이와 같은 형식은 틀리게 된 셈이죠.

그렇다면 이것은 가능할까요?

```cpp-formatted
/* void 형을 가리키는 포인터 */
#include <stdio.h>
int main() {
  void* a;

  return 0;
}
```


성공적으로 컴파일 해 본다면 아무런 오류가 뜨지 않는 다는 것을 알 수 있습니다. 왜 그럴까요? 일단, `void *a;` 의 경우 위에서 지적한 문제는 없다는 것을 알 수 있습니다. 왜냐하면 앞에서 `void` a; 의 경우 `a` 의 크기를 정할 수 없기 때문에 메모리 상에 `a` 를 위해 얼마나 많은 공간을 설정해 놓아야 하는지 모르지만, `void *a` 의 경우 '포인터' 이기 때문에 100% 메모리 상에 `int` 의 크기, 즉 4 바이트 만큼을 지정하게 됩니다. (앞에서 부터 강조해 왔던 이야기 이지만 모든 포인터의 크기는 4 바이트로 동일합니다) 즉, `a` 에는 어떠한 지점의 메모리의 주소 값이 들어가게 되는 것이지요.

그렇다면 `void* a` 포인터는 `void` 형의 변수의 메모리 주소를 가지게 될까요? 물론, 논리를 따지고 보면 맞지만 `void` 형 변수라는 것은 존재할 수 없기 때문에 `void` 형 포인터의 존재는 쓸모가 없어 보입니다. 하지만 사실 `void` 는 타입이 없기 때문에 거꾸로 생각해 보면어떠한 형태의 포인터의 값이라도 담을 수 있게 됩니다. 예를 들면

```cpp-formatted
void *a;
double b = 123.3;

a = &b;
```

와 같이 말이죠. 다시 말해 `a` 는 순전히 오직 '주소값의 보관' 역할만 하게 되는 셈입니다.

```cpp-formatted
/* b 의 값을 보려면 */
#include <stdio.h>
int main() {
  void *a;
  double b = 123.3;

  a = &b;

  printf("%lf", *a);
  return 0;
}
```


성공적으로 컴파일 하였다면

```warning
error C2100: 간접 참조가 잘못되었습니다.
```


와 같은 오류를 보게 됩니다. 이 오류가 발생하는 이유 역시 쉽게 알 수 있습니다. 왜냐하면 컴파일러는 `*a` 가 무엇을 말하는지 알 수 없거든요. 여태까지 `*a` 를 해석할 때 컴파일러는 `a` 가 가리키는 것의 타입을 보고 메모리 상에서 `a` 부터 얼마 만큼 읽어들어야 할 지 결정했는데 `void a;` 의 경우 메모리 상에서 얼마만큼 읽어들여야 할 지 모르기 때문입니다. 따라서 이는 다음과 같이 수정되어야 합니다.

```cpp-formatted
#include <stdio.h>
int main() {
  void *a;
  double b = 123.3;

  a = &b;

  printf("%lf", *(double *)a) return 0;
}
```

성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile26.uf.tistory.com%2Fimage%2F13654C1A4C500DBD6D8F6F)

와 같이 잘 출력됨을 알 수 있습니다.

```cpp-formatted
printf("%lf", *(double *)a);
```


우리는 위 문장에서 형변환 을 이용하였습니다. 즉 단순히 주소값 만을 담고 있는 `a` 에게 `(double *)` 를 취함으로써, 컴파일러로 하여금 "이 포인터 `a` 가 담고 있는 주소값은 `double` 을 가리키는 주소값이라 생각해" 라고 말한 것이지요. 따라서 `(double *)a` 부분을 통해 컴파일러는 현재 `a` 가 가리키고 있는 곳의 주소값을 `double` 로 생각하게 되어 8 바이트를 읽어들이게 합니다.

`void` 형 포인터는 단순히 어떤 타입의 포인터의 주소 값도 편리하게 담을 수 있기 때문에 많은 부분에서 활용되고 있습니다. 예를 들어 다음과 같은 역할을 하는 함수를 생각해봅시다

어떠한 특정한 주소값으로 부터 1 바이트 씩 값을 읽어오는 함수

그렇다면 이 함수는에는 인자가 2 개 전달될 텐데, 일단 그 특정한 주소값을 가리키고 있는 포인터와, 얼마나 읽을지 `int` 형 변수 하나를 받아야 겠지요. 그런데, 인자로 전달될 '특정한 주소값을 가리키고 있는 포인터' 의 타입이 제각각 이라는 것이지요. 예를 들어서 `int*` 일 수 도 있고 `double*` 일 수 도 있지요.

따라서 우리는 순전히 주소값 만을 받기 위해서는 `void` 형 포인터를 사용하는 것이 바람직하다고 볼 수 있습니다. 물론 포인터 간의 형변환을 통해서 처리할 수 있지만 어떠한 형태의 포인터 주소값도 가능하다라는 의미를 살리기 위해서는 `void` 형 포인터를 이용하는 것이 바람직합니다.

```cpp-formatted
/* 임의의 주소값 p 로 부터 byte 만큼 읽은 함수*/
#include <stdio.h>
int read_char(void *p, int byte);
int main() {
  int arr[1] = {0x12345678};

  printf("%x \n", arr[0]);
  read_char(arr, 4);
}
int read_char(void *p, int byte) {
  do {
    printf("%x \n", *(char *)p);
    byte--;

  } while (((char *)p)++ && byte);

  return 0;
}
```


성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F1328E9274C5656B5A01A3C)

`read_char` 함수를 살펴봅시다. 무언가 여태까지 해온 것 보다 코딩 실력이 업그레이드 된 것 같은데 찬찬히 살펴 보면

```cpp-formatted
do {
  printf("%x \n", *(char *)p);
  byte--;

} while (((char *)p)++ && byte);
```


먼저 `((char *)p) ++` 의 뜻 부터 생각해봅시다. `(char *)p` 는 '이 `p` 에 들어있는 값을 `char` 형 변수의 주소값이라 생각해!' 라는 의미 이지요. 그런데, 거기에 `++` 을 했으므로 포인터의 덧셈이 행해지는데 컴퓨터는 `p` 를 '`char` 형 변수의 주소값' 이라 생각하고 있으므로 `p` 에 1 을 더하게 되면 주소값이 `char` 의 크기, 즉 1 만큼 늘어납니다.

참고로 `(char *)p ++` 이라 안하고 `((char *)p)++` 이라 한 이유는 우선순위 문제 때문인데, 전자의 경우 `p++` 이 먼저 실행되어 문제가 생기기 때문입니다.

아무튼 이와 같은 방법으로 `p` 의 주소값을 계속 1 씩 증가시키는데, 이 때 `byte` 의 값이 0 이되거나 (`(char *)p)` 의 값이 0 (즉 `NULL` 일 때) `while` 문이 종료됩니다. 제가 `do while` 을 이용한 이유는 만일 동일한 조건문으로 `while` 문을 만들게 된다면 처음에 `((char *)p)++` 이 먼저 실행되기 때문에 `p` 부터 읽지 않고 `p + 1` 부터 읽게되는 불상사가 발생하기 때문에 이를 막기 위해 `do while` 문을 이용했습니다.

```cpp-formatted
printf("%x \n", *(char *)p);
```

는 `p` 가 가리키는 주소값에 위치한 데이터 1 바이트 씩 16 진수로 출력하게 됩니다. 따라서 `read_char` 함수를 호출함을 통해 `int` 형 배열인 `arr` 의 원소를 1 바이트씩 읽게 되는 것이죠. 어떤 사람들은 그 결과가 12 34 56 78 순으로 출력해야 한다고 물을 수 있는데, 이는 '엔디안' 에 대한 개념이 없는 것이기 때문에 [이 강좌](http://itguru.tistory.com/71)를 잠시 보고 오시기 바랍니다.

간단히 말하자면 우리가 쓰는 대부분의 프로세서는 리틀 엔디안 방식으로 저장하기 때문에 낮은 자리수가 낮은 주소값을 가지게 됩니다. 즉, 낮은 자리수인 78 이 낮은 주소값인 앞쪽에 저장되게 되죠. 따라서 12 34 56 78 순이 아닌 78, 56, 34, 12 순으로 저장되는 것이 맞습니다. (그렇게 따지면 87, 65, 43, 21 순으로 나타나야 되지 않냐고 물을 수 있는데 저장의 단위가 바이트 이므로 한 바이트 내에서는 우리가 생각하는 순서대로 저장됩니다. )



###  메인 함수의 인자

```cpp-formatted
/* main 함수의 인자라고?? */
#include <stdio.h>
int main(int argc, char **argv) {
  printf("받은 인자의 개수 : %d \n", argc);
  printf("이 프로그램의 경로 : %s \n", argv[0]);

  return 0;
}
```

성공적으로 컴파일 했다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F19601A1D4C566103A4699E)

아마도 이 강좌를 보고 계신 여러분 중 일부는 위와 같은 메인 함수에 친숙하실 지도 모릅니다.

```cpp-formatted
int main(int argc, char **argv)
```


보시다싶이 `main` 함수가 인자를 받고 있습니다. 이게 도대체 무슨 일인가요. 다른 함수가 인자를 받는 것은 이해가 잘되는데 `main` 함수가 인자를 받다니. 도대체 누가 인자를 넣어 주고 있는 것일까요? 바로 운영체제에서 인자를 알아서 넣어주는 것입니다. 바로 위와 같이요.

일단 `argc` 는 `main` 함수가 받은 인자의 수 입니다. 그리고 `argv` 는 `main` 함수가 받은 각각의 인자들을 나타내죠. 프로그램을 실행하면 기본적으로 아무런 인자들을 넣지 않더라도 위와 같은 정보는 들어가게 됩니다. 즉, `main` 함수는 자신의 실행 경로를 인자로 받게 되죠. 그렇다면 다른 인자들도 넣을 수 있을까요? 한 번 해봅시다.

```cpp-formatted
/* 인자를 가지는 메인 함수 */
#include <stdio.h>
int main(int argc, char **argv) {
  int i;
  printf("받은 인자의 개수 : %d \n", argc);

  for (i = 0; i < argc; i++) {
    printf("이 프로그램이 받은 인자 : %s \n", argv[i]);
  }

  return 0;
}
```


성공적으로 컴파일 했다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F19601A1D4C566103A4699E)

일단 우리는 프로그램을 임의의 개수의 인자를 받아 받은 인자들을 모두 출력하게 하였습니다. 그렇다면 프로그램에 직접 인자를 넣어 봅시다.

윈도우즈 XP 의 경우

시작 -> 실행 -> cmd

윈도우즈 `Vista, 7` 의 경우

시작 -> 하단에 '프로그램 밑 파일 검색' 에 `cmd` 라고 친다.

그렇다면 아래와 같은 모습을 보실 수 있습니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F160928314C56633710E391)

이것은 '명령 프롬포트' 라고 부르는 것인데 기존의 `MS-DOS` 와 유사합니다. (그러나 본질적으로 다릅니다) 우리는 여기서 윈도우즈 처럼 파일을 클릭하여 실행하는 것과는 달리 직접 명령어를 침으로써 파일을 실행시켜야 합니다. 그러기 위해선 우리가 원하는 파일이 어디있는지 알아야겠죠.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F172AA82F4C5663AE0CF8A7)

먼저 위와 같이 화면에 `cd C:\\` 을 씁니다. 이 명령어의 의미는 'C:\' 라는 경로로 들어가라 입니다. 즉 'cd' 의 의미는 지정하는 경로로 들어가게 해주죠. 참고로 여기서도 역시 \ 하나만 치면 다른 의미로 해석되기 때문에 \ 하나를 나타내기 위해서는 \ 를 두번 써야 합니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F110A721C4C56644C8E26B5)

이제 화면에 `dir` 을 쳐봅시다. 'dir' 의 의미는 이 경로에 들어있는 폴더와 파일들을 보여주라는 의미 입니다. 위 사진에서는 사생활보호 차원을 위해 `Program Files` 빼고 이름을 모두 가렸습니다. 이 때, 어떤 것은 왼쪽에 `<DIR>` 이라고 나오고 어떤 것은 없는 것을 볼 수 있는데, `<DIR>` 이란 것은 '폴더' 와 같은 뜻으로 파일이 아니라는 것입니다. 반면에 `<DIR>` 이 없는 것은 파일이 되겠지요. 아마 프로그램을 C 드라이브에 깔았기 때문에 아마 모든 파일은 동일한 경로에 있을 것입니다.

위와 같은 방식으로 우리의 파일을 찾는 일만 남았습니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F155D211D4C566685DB208B)

우리가 원하는 파일은 아마 `C:\Users\Lee\Documents\Visual Studio 2008` 에 있습니다. 이를 `cd` 명령어로 다 치면 됩니다. 이 때, 중간에 띄어쓰기가 있으므로 큰 따옴표로 묶어주어야 합니다. 즉 `cd "C:\\Users\\Lee\Documents\\Visual Studio 2008"` 처럼 말이죠. 그렇지 않고 `cd C:\\Users\\Lee\Documents\\Visual Studio 2008` 로 쓴다면 컴퓨터는 `cd C:\\Users\\Lee\Documents\\Visual` 로 인식합니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F1667FD1D4C566686838374)

이제 `Project` 폴더로 들어가보겠습니다. 단순히 `cd Projects` 라고 치면 됩니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F1104D31A4C5666FFAD95D0)

오. 저의 프로젝트인 'teach' 가 보이네요. 여러분과 저와의 프로젝트 이름이 다를 수 있으니 각기 맞는 프로젝트로 들어가시면 됩니다. 여기서도 물론 폴더 이름에 띄어쓰기가 있다면 큰따옴표로 묶어주는 것을 잊지 마세요.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F1678121B4C5667816BA805)

이제, 파일들을 쭉 보면 `Debug` 라는 폴더와 `teach` 라는 폴더가 있는데, `teach` 폴더에는 우리의 소스 코드가, `Debug` 폴더에는 만들어진 실행 파일이 있습니다. 그렇다면 우리는 어디로 가야 할까요? 네, `Debug` 로 갑시다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F1949391B4C5667D801C548)

우와 그렇다면 위와 같이 `teach.exe` 를 보실 수 있습니다. 이제 `teach.exe` 를 침으로써 위 프로그램을 실행할 수 있습니다.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F1639E21B4C566825263E53)

우왕. 잘 실행되는 군요. 일단 신기한 점은 이 프로그램이 받은 인자가 더이상 그 프로그램의 경로가 들어가지 않고 `teach.exe` 가 들어갔습니다. 맞습니다. 우리가 `teach.exe` 를 침으로써 실행한 순간 이 프로그램의 첫번째 인자는 `teach.exe` 가 됩니다. 만일 우리가 이 프로그램을 `"C:\\Users\\Lee\\Documents\\Visual Studio 2008\\Projects\\teach\\Debug\\teach.exe"` 라고 쳐서 실행하였다면 인자가 `C:\\Users\\Lee\\Documents\\Visual Studio 2008\\Projects\\teach\\Debug\\teach.exe` 가 되겠지요.

그렇다면 다른 인자들을 넣어봅시다. 이는 간단합니다. 프로그램 이름 뒤에 다른 것들을 써주면 되죠. 예를 들어


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F1621C0324C566A1F1C450F)

`teach.exe abc def` 라고 쓰게 된다면 `teach.exe` 가 첫번째 인자, `abc` 가 두번째 인자, `def` 가 세번재 인자가 되고 받은 인자의 수는 3 이 되지요. 어때요. 쉽지요?

그런데 여태까지 배운 내용을 잘 숙지하신 분이라면 다음과 같은 질문을 하실 수 있습니다.

`main` 함수의 두번째 인자 말이에요, `char **` 인데 제 기억에 이차원 배열을 전달하기 위해서는 `char (*argv)[5]` 와 같이 반드시 크기를 명시해 주어야 하는데 여기서는 단순히 `char**` 로 해놓고 어떻게 그리 잘 작동하는지요?

그 이유는 간단합니다. `char**` 은 `(char *)` 형 배열을 가리키는 포인터 이지요. 즉, 포인터의 배열 입니다. (배열 포인터가 절대로 아닙니다) `int arr[4]` 라는 배열을 가리키는 포인터가 `int *` 형인 것 (여기서는 `arr` 이겠네요) 처럼 `char *arr[5];` 를 가리키는 포인터의 형은 `char**` 이 되겠지요.

즉, 다음과 같은 꼴이 되겠지요.


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile26.uf.tistory.com%2Fimage%2F162720344C566E5670E92B)

즉 `argv` 는 포인터들의 배열을 가리키고 있고, 그 포인터 배열에서의 각각의 원소, 즉 포인터들은 인자로 전달된 문자열들을 가리키고 있습니다. 이 때, 이 문자열들은 메모리의 다른 공간에 보관되어 있겠죠.

따라서 우리는 `argv[i]` 를 통해 특정한 인자의 문자열에 저장된 주소값을 나타낼 수 있게 됩니다.

그럼 이상으로 이번 강좌를 마치도록 하겠습니다. 이번 강좌는 다음에 배울 동적 메모리 할당에 밑바탕이 되는 정보 이니 절대로 잊지 마시기 바랍니다.

### 생각해 보기

#### 문제 1

메인함수의 인자를 활용한 계산기를 만들어보세요. 예를 들어서

```info
calc.exe 5 + 10
```

을 치면 15 가 나오게 하면 되지요.

이 때, `5, +, 10` 은 모두 다른 인자로 봐야하겠죠. 기초적인 단계 이므로 연산자는 하나만 써도 된다고 합시다.참고로 인자는 모두 문자열 형태로 오기 때문에 문자열로 된 수를 `int` 형으로 바꾸는 작업이 필요할 것입니다.

##@ chewing-c-end