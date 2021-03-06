----------------
title : 씹어먹는 C++ - <1 - 2. 첫 C++ 프로그램 분석하기>
cat_title: 1 - 2. 첫 C++ 프로그램 분석하기
next_page : 138
publish_date : 2011-03-06
--------------


이번 강좌에서는

* 첫번째 C++ 프로그램 분석

* 이름공간(namespace) 에 대한 이해


![](/img/ChewingCpplogo.png)


안녕하세요 여러분~ 씹어먹는 C++ 두번째 강좌 입니다. 지난번에는 아마도 여러분 인생 최초의 C++ 프로그램을 만들어 보았을 텐데요, 이번 강좌에서는 소스 코드를 따라가면서 분석을 하는 시간을 갖도록 하겠습니다.

사실, 지금 제 강좌를 보고 계시는 분들 중에서는 막 C 언어 공부를 끝내고 오신 분들도 많으실 텐데요, 무언가 초심자의 마음으로 돌아간 것 같지 않으세요? C 언어에서 막 어려운 프로그래밍 하다가 C++ 오니 다시 맨 밑바닥 부터 화면에 출력하는 것을 하니 답답한 마음이 들 것도 같네요.. 하지만 이것도 잠시라고 생각하세요. 곧 놀라운 C++ 의 세계가 펼쳐질 것입니다.

```cpp-formatted
#include <iostream>
using namespace std;

int main() {
  cout << "Hello, World!!" << endl;
  return 0;
}
```


성공적으로 컴파일 하였다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F1526FF484D7B572829CC38)

와 같이 나옵니다.

  위 코드가 바로 지난 강좌에서 사용하였던 코드 입니다. 일단 C 언어와 비슷한 점들 부터 찾아보도록 합시다. 일단 맨 위에

```cpp-formatted
#include <iostream>
```


 을 보면 '아하! `iostream` 이라는 헤더파일을 `include` 하고 있구나!' 라는 생각이 머리속에 번뜩이셔야 합니다. 그렇지 않다면 C 언어를 다시 공부하도록 하세요 ㅎ ([이 강좌를 보시면 됩니다](http://itguru.tistory.com/87))

`iostream` 헤더 파일은 C++ 에서 표준 입출력에 필요한 것들을 포함하고 있습니다. 예를 들면 아래에서 사용되는 `cout` 이나 `endl` 과 같은 것들을 말이지요. C 언어에서의 `stdio.h` 와 비슷하다고 보시면 됩니다. (그리고 C 와 하나 다른 점은 헤더 파일 이름 뒤에 `.h` 가 붙지 않습니다!)

그 다음 줄의 `using ...` 을 보면 잘 모르겠네요.일단 패스~그 아래를 보게 되면 다시 어디서 많이 보던 것이 나왔죠?

```cpp-formatted
int main()
```


네. `main` 함수를 정의하는 부분 입니다. 그리고 그 함수의 몸체를 보면

```cpp-formatted
cout << "Hello, World!!" << endl;
return 0;
```


와 같은 내용이 있네요. 화면에 대충 출력된 것을 보아 `cout` 은 화면에 무언가 출력시켜주는 것 같은데, `printf` 와 다르게 사용된 것을 보니 함수 같지는 않네요. 그리고 화면에 출력된 것을 대충 보면 "계속하려면 아무 키나 누르세요" 가 한 줄 개행되어서 나온 것을 보니 `endl` 은 한 줄 엔터를 쳐서 나타내라는 표시 같습니다.

그리고 마찬가지로 `main` 함수에서도 `return` 을 해주고요. 이렇게 대략 살펴보면 기존의 C 언어와 크게 다른 점은 없는 것 같습니다.

하지만 미스테리로 남아있던 부분부터 살펴보도록 합시다.

```cpp-formatted
using namespace std;
```


위 문장을 직역해보면 '`std` 라는 이름 공간(namespace) 를 사용하겠다' 라는 의미가 됩니다. 그렇다면 이름 공간이란 것이 정확히 무엇일까요? 이름 공간은 말그대로 특정한 공간에 이름을 붙여준 것입니다. 예를 들어서

```cpp-formatted
#include "header1.h"
#include "header2.h"

int main() { function(); }
```


와 같은 표현을 사용했다고 합시다. 그런데 문제는 `header1.h` 에도 `function` 이 정의되어 있고, `header2.h` 에도 이름만 똑같이 다른 일을 하는 `function` 이 정의되어 있는 것입니다. 보통 C 언어에서는 이러한 문제를 해결하기 위해 우리에게 주어진 선택권은 오직 하나, 함수의 이름을 바꾸는 것 밖에 없었지만 C++ 에서는 이름 공간을 도입한 덕분에 이 문제를 유연하게 해결할 수 있었습니다. 바로 `namespace` 를 사용하는 것이지요.

```cpp-formatted
// header1.h 의 내용
namespace header1 {
int function();
}
```


```cpp-formatted
// header2.h 의 내용
namespace header2 {
int function();
}
```


위 둘은 각각 다른 `header` 들의 내용 입니다. 각각의 함수들은 다른 `namespace` 에 존재합니다. 즉, `header1` 에 있는 `function` 의 경우 'header1.h 에 `header1` 라는 이름 공간에 살고 있는 function' 이 되고, `header2` 에 있는 `function` 의 경우 'header2.h 에 `header2` 라는 이름 공간에 살고 있는 function' 이 되는 것이지요. 즉 기존의 C 에서는 'header1.h 에 살고 있는 function' 과 'header2.h 에 살고있는 function' 으로 밖에 나눌 수 없었지만 C++ 에서는 좀더 세부적으로 분류할 수 있게 됩니다. 따라서 실제로 `main` 함수에서 사용할 때는


```cpp-formatted
#include "header1.h"
#include "header2.h"

int main() {
  header1::function();  // header1 이란 이름 공간에 있는 function 을 호출
}
```


과 같이 사용하게 됩니다. 하지만 만일 위 같은 `function` 을 여러번 반복적으로 호출하게 되는 경우 어떨까요. 앞에 `header1::` 을 붙이기가 상당히 귀찮게 됩니다. 그래서 아래와 같이 '나는 앞으로 `header1` 이란 이름 공간에 들어있는 것들만 쓸거다!' 라고 선언할 수 있습니다.

```cpp-formatted
#include "header1.h"
#include "header2.h"
using namespace header1;
int main() {
  function();  // header1 에 있는 함수를 호출
}
```

물론 그렇다고 해서 `header2` 에 있는 함수를 못 사용하는 것은 아니고 다음과 같이 지정해서 써주면 됩니다.

```cpp-formatted
#include "header1.h"
#include "header2.h"
using namespace header1;
int main() {
  header2::function();  // header2 에 있는 함수를 호출
  function();           // header1 에 있는 함수를 호출
}
```


그렇다면 다시 원래 예제를 살펴보도록 합시다.

```cpp-formatted
using namespace std;

int main() {
  cout << "Hello, World!!" << endl;
  return 0;
}
```


여기서 `cout` 과 `endl` 은 모두 `iostream` 헤더파일의 `std` 라는 이름 공간에 정의되어 있는 것들입니다. 따라서 만일 `using namespace std;` 를 붙여주지 않았더라면

```cpp-formatted
int main() {
  std::cout << "Hello, World!!" << std::endl;
  return 0;
}
```


로 꽤 귀찮게 써주야 했었을 것입니다.



그렇다면 `cout` 은 무엇일까요? 정확히 무엇인지 말하자면 `ostream` 클래스의 객체로 표준 출력(C 언어에서의 `stdout` 에 대응됩니다) 을 담당하고 있습니다. 무슨 말인지 모르겠다고요? 괜찮습니다. 이 것이 정확히 무슨 의미인지는 나중 강좌에서 알아보도록 하겠고, 그냥 다음과 같이 쓴다는 것만 알아두시면 됩니다.

```info
cout << 출력할 것 << 출력할 것 << ... << 출력할 것;
```


그리고 `endl` 은 화면에 출력해주는 '함수' 입니다. 놀라셨지요? 하지만 그냥

```cpp-formatted
cout << endl;
```



이라 쓰면 화면에 엔터를 하나 출력해주는 것으로 기억하시면 됩니다. 물론 `endl` 에 대해서도 나중에 다루어 보도록 하겠습니다 :)

### 생각 해보기

#### 문제 1

화면에 출력되는 것들을 바꾸어보자.

#### 문제 2

아래 문장은 화면에 어떻게 출력될까요?

```cpp-formatted
cout << "hi" << endl
     << "my name is "
     << "Psi" << endl;
```

##@ chewing-cpp-end