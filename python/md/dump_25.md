----------------
title : 씹어먹는 C 언어 - <12 - 3. 포인터는 영희이다! (포인터)>
cat_title : 12 - 3. 포인터는 영희이다! (포인터)
next_page : 26
publish_date : 2009-11-26
--------------


이번 강좌에서는

* `1` 차원 배열을 가리키는 포인 1 차원 배열을 가리키는 포인터

* `2` 차원 배열을 가리키는 포인터 (배열 포인터 2 차원 배열을 가리키는 포인터 (배열 포인터)

* 포인터 배열

* 더블 포인터 (**)

![씹어먹는 C 언어](/img/ChewingClogo.png)

안녕하세요 여러분~! 이전 강좌는 잘 보시고 계시는지요? 아마도 이번 강좌가 최대의 난관일 듯 하네요. 이번 강좌를 잘 이해하냐, 이해 못하냐에 따라서 C 언어가 쉽다/어렵다가 완전히 좌우됩니다. 그러니 지금 졸린 사람들은 잠을 자고 쌩쌩할 때 오시길 바랍니다. (아마도 이 부분이 C 언어에서 가장 어려울 부분이 될 듯 하네요.. 저도 최대한 쉽게 설명하기 위해 노력하겠습니다^^)

  잠깐 지난 시간에 배웠던 것을 머리속으로 상기시켜봅시다. 일단,

* 배열은 포인터와 밀접한 관련이 있다

* 1 차원 배열의 이름은 첫 번째 원소를 가리킨다. 즉, `int arr[3];` 이라는 배열이 있다면 `arr` 와 `&arr[0]` 은 같다. 그런데, `arr[0]` 이 `int` 형이므로 `arr` 은 `int*`  형 이다. (왜냐하면 `int` 형을 가리키는 포인터는 `int*` 이니까 1 차원 배열의 이름은 첫 번째 원소를 가리킨다.
즉, `int arr[3];` 이라는 배열이 있다면 `arr` 와 `&arr[0]` 은 같다. 그런데, `arr[0]` 이 `int` 형이므로 `arr` 은 `int*`  형 이다. (왜냐하면 `int` 형을 가리키는 포인터는 `int*` 이니까)

이 두 가지 사실을 머리속에 잘 들어 있겠지요. 만일 위 두 문장을 읽으면서 조금이라도 의구심이 드는 사람은 바로 뒤로가기를 눌러서 이전 강좌를 보시기 바랍니다.



###  1 차원 배열 가리키기


일단, 강의의 시작은 간단한 것으로 해보겠습니다. 이전해도 말했듯이 (벌써 몇 번째 반복하고 있는지는 모르겠지만 그 만큼 중요하니까) `int arr[10];` 이라는 배열을 만든다면 `arr` 이 `arr[0]` 을 가리킨다고 했습니다. 그렇다면 다른 `int*` 포인터가 이 배열을 가리킬 수 있지 않을까요? 한 번 프로그램을 짜봅시다.

```cpp-formatted
#include <stdio.h>
int main() {
  int arr[3] = {1, 2, 3};
  int *parr;

  parr = arr;
  /* parr = &arr[0]; 도 동일하다! */

  printf("arr[1] : %d \n", arr[1]);
  printf("parr[1] : %d \n", parr[1]);
  return 0;
}
```

성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F1436CE234B01106EBFC31E)

 일단, 중점적으로 볼 부분은 아래와 같습니다.

```cpp-formatted
parr = arr;
```

바로 `arr` 에 저장되어 있는 값을 `parr` 에 대입하는 부분이지요. 앞에서 말했듯이 `arr` 은 `int` 를 가리키는 포인터 입니다. 이 때, `arr` 에 저장된 값, 즉 배열의 첫 번째 원소의 주소를 `parr` 에 대입하고 있습니다. 다시 말해 위 문장은 주석에도 잘 나와 있듯이 아래와 같은 문장이 됩니다.

```cpp-formatted
parr = &arr[0]
```

따라서, `parr` 을 통해서 `arr` 을 이용했을 때와 동일하게 배열의 원소에 마음껏 접근할 수 있게 되는 것이 됩니다. 위 모습을 한 번 그림으로 나타내보면 (아마도 여러분들은 지금 수준이라면 머리속으로 다 그릴 수 있어야 할 것입니다)


![arr[0 은 arr 과 parr 모두가 가리키게 됩니다. ](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F194C49214B01139B70E9DA)
참고적으로 한 방의 크기는 그림의 단순화를 위해 4 바이트로 하였습니다.
```cpp-formatted
/* 포인터 이용하기 */
#include <stdio.h>
int main() {
  int arr[10] = {100, 98, 97, 95, 89, 76, 92, 96, 100, 99};

  int* parr = arr;
  int sum = 0;

  while (parr - arr <= 9) {
    sum += (*parr);
    parr++;
  }

  printf("내 시험 점수 평균 : %d \n", sum / 10);
  return 0;
}
```

  성공적으로 컴파일 하면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F200B06044B0D44AD6D6FAD)

  일단, 포인터를 이용한 간단한 예제를 다루어보겠습니다.

```cpp-formatted
int* parr = arr;
```

먼저, `int` 형 1 차원 배열을 가리킬 수 있는 `int*` 포인터를 정의하였습니다. 그리고, 이 `parr` 은 배열 `arr` 을 가리키게 됩니다.

```cpp-formatted
while (parr - arr <= 9) {
  sum += (*parr);
  parr++;
}
```

그 다음 `while` 문을 살펴봅시다. `while` 문을 오래전에 배워서 기억이 안난다면 다시 뒤로 돌아가세요! 이 `while` 문은 `parr - arr` 이 9 이하일 동안 돌아가게 됩니다. `sum` 에 `parr` 이 가리키는 원소의 값을 더했습니다. `+=` 연산자의 의미는 아시죠? `sum +=` (*parr); 문장은 `sum = sum + *parr` 와 같다는 것 알고 계시지요?

```cpp-formatted
parr++;
```

`parr` 을 1 증가시켰습니다. 이전 강좌에서도 이야기 하였지만 포인터 연산에서 1 증가시킨다면, `parr` 에 저장된 주소값에 1 이 더해지는 것이 아니라 `1 *` (포인터가 가리키는 타입의 크기) 가 더해진다는 것이지요. 즉, `int` 형 포인터 이므로 4 가 더해지므로, 결과적으로 배열의 그 다음 원소를 가리킬 수 있게 됩니다. 암튼, 위 작업을 반복하면 `arr` 배열의 모든 원소들의 합을 구하게 됩니다. `while` 문에서 9 이하일 동안만 반복하는 이유는, `parr - arr >= 10` 이 된다면 `parr[10` 이상의 값] 을 접근하게 되므로 오류를 뿜게 됩니다.

여기서 궁금한 것이 없나요? 우리가 왜 굳이 `parr` 을 따로 선언하였을까요? 우리는 `arr` 이 `arr[0]` 을 가리킨다는 사실을 알고 있으므로 `arr` 을 증가시켜서 `*(arr)` 으로 접근해도 되지 않을까요? 한 번, `arr` 의 값을 변경할 수 있는지 없는지 살펴봅시다.

```cpp-formatted
/* 배열명 */
#include <stdio.h>
int main() {
  int arr[10] = {100, 98, 97, 95, 89, 76, 92, 96, 100, 99};

  arr++;  // 오류!! 배열 이름은 const
  return 0;
}
```


  컴파일 해보면

```warning
error C2105: '++'에 l-value가 필요합니다.
```

와 같은 오류를 만나게 됩니다. 이 말은 `arr` 이 상수이므로 연산할 수 없다는 말이 됩니다. 배열이름이 상수라고요? 맞습니다. 물론 `*arr =` 10; 과 같이 `arr[0]` 의 값은 바꿀 수 있지만 `arr++` 와 같은 연산(즉, `arr` 이 다른 것을 가리키는 것)은 허용되지 않는 것을 보아서 `const` 키워드가 어느쪽에 붙은 포인터인지 짐작할 수 있을 것 입니다. 즉, 배열의 이름은

```info
  (뭐시기 뭐시기) *const (배열 이름)
```

과 같은 형태임을 알 수 있습니다. 결과적으로 배열의 이름은 죽어다 깨어나도 언제나 배열의 첫번째 원소를 가리키게 됩니다. 배열의 이름이 결코 다른 값들을 가리킬 수 없도록 C 에서 제한을 두는 이유는, 제 생각에 프로그래머가 실수로 배열의 이름이 가리키는 값을 잘못 바꿔서 배열을 '아무도 가리키지 않는 메모리 상의 미아'가 됨을 막으려고 한 것이 아닐까요?



###  포인터의 포인터


똑똑한 분들이라면 이러한 것들에 대해서도 생각해 보신 적이 있을 것입니다. 물론, 안하셔도 상관 없고요.. 저의 경우 포인터 처음 배울 때 그것 마저 이해하기도 힘들어서 한참 버벅거렸습니다 :) 아무튼. 지금 머리속으로 예상하시는 대로 포인터의 포인터는 다음과 같이 정의합니다.

```cpp-formatted
int **p;
```

위는 '`int` 를 가리키는 포인터를 가리키는 포인터' 라고 할 수 있습니다. 쉽게 머리에 와닿지 않죠? 당연합니다. 이전 강좌의 내용도 어려워 죽겠는데 위 내용까지 머리속에 쑤셔 넣으려면 얼마나 힘들겠어요? 그래서, 한 번 예제를 봅시다.

```cpp-formatted
/* 포인터의 포인터 */
#include <stdio.h>
int main() {
  int a;
  int *pa;
  int **ppa;

  pa = &a;
  ppa = &pa;

  a = 3;

  printf("a : %d // *pa : %d // **ppa : %d \n", a, *pa, **ppa);
  printf("&a : %d // pa : %d // *ppa : %d \n", &a, pa, *ppa);
  printf("&pa : %d // ppa : %d \n", &pa, ppa);

  return 0;
}
```

성공적으로 컴파일 했다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F1607F7224AFEB33C8FEA44)
여러분의 결과는 약간 다를 수 있습니다. 다만, 같은 행에 있는 값들이 모두 같음을 주목하세요


일단 위에 보시다 싶이 같은 행에 있는 값들은 모두 같습니다. 사실, 위 예제는 그리 어려운 것이 아닙니다. 포인터에 제대로 이해만 했다면 말이죠. 일단 `ppa` 는 `int*` 를 가리키는 포인터 이기 때문에

```cpp-formatted
ppa = &pa;
```

와 같이 이전의 포인터에서 했던 것 처럼 똑같이 해주면 됩니다. `ppa` 에는 `pa` 의 주소값이 들어가게 되죠.

```cpp-formatted
printf("&pa : %d // ppa : %d \n", &pa, ppa);
```

따라서 우리는 위의 문장이 같은 값을 출력함을 알 수 있습니다. 위의 실행한 결과를 보아도 둘다 1636564 를 출력했잖아요.

```cpp-formatted
printf("&a : %d // pa : %d // *ppa : %d \n", &a, pa, *ppa);
```

그리고 이제 아래에서 두 번째 문장을 봐 봅시다. `pa` 가 `a` 를 가리키고 있으므로 `pa` 에는 `a` 의 주소값이 들어갑니다. 따라서, `&a` 와 `pa` 는 같은 값이 되겠지요. 그러면 `*ppa` 는 어떨까요? `ppa` 가 `pa` 를 가리키고 있으므로 `*ppa` 를 하면 `pa` 를 지칭하는 것이 됩니다. 따라서 역시 `pa` 의 값, 즉 `&a` 의 값이 출력되게 됩니다.

```cpp-formatted
printf("a : %d // *pa : %d // **ppa : %d \n", a, *pa, **ppa);
```

마지막으로 위의 문장을 살펴 봅시다. `pa` 가 `a` 를 가리키고 있으므로 `*pa` 를 하면 `a` 를 지칭하는 것이 되어 `a` 의 값이 출력됩니다. 그렇다면 `**ppa` 는 어떨까요? 이를 다시 써 보면 `*(*ppa)` 가 되는데, `*ppa` 는 `pa` 를 지칭하는 것이기 때문에 `*pa` 가 되서, 결국 `a` 를 지칭하는 것이 됩니다. 따라서, 역시 `a` 의 값이 출력되겠지요. 어때요? 간단하죠?

위 관계를 그림으로 그리면 다음과 같습니다.


![a 의 주소값을 pa 가, pa 의 주소값을 ppa 가 가지고 있습니다. ](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F161550244AFEB8B93D7FD2)



###  2 차원 배열의 `[]` 연산자

2 차원 배열의 `[]` 연산자에 대해선 제가 지난번 강좌에서 '생각 해보기' 문제로 내었던 것 같은데, 생각해보셨는지요? 일단 이전의 기억을 더듬에서 다음과 같은 배열이 컴퓨터 메모리 상에 어떻게 표현되는지 생각 해보도록 합시다.

```cpp-formatted
int a[2][3];
```

물론, 이 배열은 2 차원 배열이므로 평면위에 표시된다고 생각할 수 도 있지만, 컴퓨터 메모리 구조는 1 차원 적이기 때문에 1 차원으로 바꿔서 생각해봅시다. 되었나요? 그렇다면, 제가 그림을 보여드리죠.

![a 는 a[0 을 가리키며, a[0 은 a[0[0 을 가리킵니다. a[1 은 a[1[0 을 가리킵니다. ](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F1358091D4AFF6236726DC3)
실제로 프로그램을 짜서 실행해 보면 메모리 상에 위와 같이 나타남을 알 수 있습니다. 한 번 해보세요~
  일단, 위 그림에서 왼쪽에 메모리 상의 배열의 모습이 표현된 것은 여러분이 쉽게 이해하실 수 있스리라 믿습니다. 다만, 제가 설명해야 할 부분은 오른쪽에 큼지막하게 화살표로 가리키고 있는 부분이지요. 먼저 아래의 예제를 봅시다.

```cpp-formatted
/* 정말로? */
#include <stdio.h>
int main() {
  int arr[2][3];

  printf("arr[0] : %p \n", arr[0]);
  printf("&arr[0][0] : %p \n", &arr[0][0]);

  printf("arr[1] : %p \n", arr[1]);
  printf("&arr[1][0] : %p \n", &arr[1][0]);

  return 0;
}
```

성공적으로 컴파일 했다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F157473054B001795ACC9C7)
표현된 주소값은 여러분과 다를 수 있습니다.

`arr[0]` 에 저장되어 있는 값이 `arr[0][0]` 의 주소값과 같고, `arr[1]` 에 저장되어 있는 값이 `arr[1][0]` 의 주소값과 같습니다. 이것을 통해 알 수 있는 사실은..? 아마도 다 알겠지만, `arr[0]` 은 `arr[0][0]` 을 가리키는 포인터 이고, `arr[1]` 은 `arr[1][0]` 을 가리키는 포인터라는 뜻이 되겠지요. 이 때, `arr[0][0]` 의 형이 `int` 이므로 `arr[0]` 은 `int*` 형이 되겠고, 마찬가지로 `arr[1]` 도 `int*` 형이 되겠지요.

```cpp-formatted
/* a? */
#include <stdio.h>
int main() {
  int arr[2][3];

  printf("&arr[0] : %p \n", &arr[0]);
  printf("arr : %p \n", arr);

  return 0;
}
```

성공적으로 컴파일 했다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F124BE80F4B01072C8ED626)
출력 결과가 여러분의 출력결과와 다를 수 있지만 값이 같음을 주목하세요

이번에는 `arr[0]` 의 주소값과 `arr` 에 저장된 값이 같군요.. 근데요, 이러한 결과는 어디서 본 것 같지 않으세요? 

맞아요. 실제로 우리가 만들었던 1 차원 `int` 배열에서도 배열의 이름이 배열의 첫 번째 원소를 가리키고 있었습니다. 그런데 위 2차원 배열의 경우에도 `arr` 이 `arr[0]` 을 가리키고 있으므로 동일하다고 볼 수 있습니다. 그렇다면, `arr[0]` 이 `int*` 형 이므로 `arr[0]` 을 가리키는 `arr` 은 `int**` 형 일까요?  아마 여러분 머리속엔 지금 이러한 생각이 떠오를 것입니다.

"당연하지.. 그걸 말이라 묻냐? 니가 위에서 설명했잖아. `int*` 를 가리키는 포인터는 `int**` 이라고 "

  그런데 생각을 해보세요. 그렇게 당연하다면 제가 질문을 했겠습니까? (^^) 답변은 "아니오" 입니다.

아마 여러분은 '내가 위에서 뭘 배웠지?' 라는 생각이 들면서 혼돈에 빠질 것입니다. 당연하지요.. 제가 이야기를 안한 부분이니까요. 저도 처음에 이 부분을 배웠을 땐 이전까지 배웠던 사실이 쓰나미 처럼 밀려나가고 머리속에 하애지는 현상을 겪었습니다. 아무튼.. 왜 그런지 설명해보죠.



###  포인터의 형(type) 을 결정짓는 두 가지 요소


먼저 포인터의 형을 결정하는 두 가지 요소에 대해 이야기 하기 전에, 위에서 배열의 이름이 왜 `int**` 형이 될 수 없는지에 대해 먼저 이야기 해봅시다. 만일 `int**` 형이 될 수 있다면 맨 위에서 했던 것 처럼 `int**` 포인터가 배열의 이름을 가리킨다면 배열의 원소에 자유롭게 접근할 수 있어야만 할 것입니다.

```cpp-formatted
/* 과연 될까? */
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int **parr;

  parr = arr;

  printf("arr[1][1] : %d \n", arr[1][1]);
  printf("parr[1][1] : %d \n", parr[1][1]);

  return 0;
}
```

  그런데 컴파일 시에 아래와 같은 경고가 기분을 나쁘게 하네요.

```warning
 warning C4047: '=' : 'int **'의 간접 참조 수준이 'int (*)[3]'과(와) 다릅니다.
```

  아무튼, 무시하고 실행해봅시다.




![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F150B40264B0BA3124C7215)

헉! 예전에 보았던 친근한 오류가 뜹니다. 무슨 뜻일까요? 예전에 배열에 대해 공부하였을 때 (11-1 강) '초기화 되지 않은 값' 에 대해서 이야기한 적이 있었을 것입니다. 이 때, `int arr[3];` 이라 했는데 `arr[10] = 2;` 와 같이 허가되지 않은 공간에 접근하기만 해도 위와 같은 오류가 발생한다고 했습니다.

위 예제의 경우도 마찬가지 입니다. `parr[1][1]` 에서 이상한 메모리 공간의 값에 접근하였기에 발생한 일이지요. 그렇다면 왜? 왜? 이상한 공간에 접근하였을까요?

먼저, 일차원 배열에서 배열의 형과, 시작 주소값을 안다고 칠 때, `n` 번째 원소의 시작 주소값을 알아내는 공식을 생각해봅시다. 만일 이 배열의 형을 `int` 로 가정하고, 시작 주소를 `x` 라고 할 때, (참고적으로 다 아시겠지만 `int` 는 4 바이트 `n` 번째 원소에 접근한다면 (`x + 4 * (n - 1)` 로 나타낼 수 있죠)


와 같이 나타낼 수 있습니다. 왜냐구요? 아마, 여러분들이 스스로 생각해보세요 :)

이번에는 이차원 배열을 나타내봅시다. 이 이차원 배열이 `int arr[a][b];` 라고 선언되었다면 (여기서 `a` 와 `b` 는 당연히 정수겠죠) 아래와 같이 2차원 평면에 놓여 있다고 생각할 수 있습니다.

![arr[0[0, arr[0[1 .... arr[a-1[b-1 까지 쭈르륵 나열된 모습](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F1547A2204B0BA8833543A1)
참고적으로 행은 '가로' 이고, 열은 '세로' 입니다.
  메모리는 선형(1차원) 이므로 절대로 위와 같이 배열될 일은 없겠지요. 위 이차원 배열을 메모리에 나타내기 위해서는 각 행 부터 읽어주면 됩니다. 즉, 위 배열은 아래와 같이 메모리에 배열됩니다.


![물론 메모리 상에서는 실제로 선형으로 존재한다는 것 아시죠!](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F1445F9204B0BABC63D97B6)
사실 위에서도 비슷한 그림이 나오지만 또 그린 이유는 머리에 완전히 박아 두라는 의미 입니다.  즉, `arr[0][0]` 부터 `arr[0][1] .... arr[a-1][b-1]` 순으로 저장되게 되지요. 그렇다면 위 배열의 시작주소를 `x` 라 하고, `int` 형 배열이고, `arr[c][d]` 라는 원소에 접근한다고 칩시다. 그렇다면 이 원소의 주소값은 어떻게 계산될까요?

일단, 위 원소는 `(c+1)` 번째 행의 `(d+1)` 번째 열에 위치해 있다고 생각할 수 있습니다. (예를 들어서 `arr[0][2]` 는 1 번째 행의 3 번째 열에 위치해 있다) 그러면, 먼저 `(c+1)` 행의 시작 주소를 계산해봅시다. 간단히 생각해보아도 `x + c * b * 4` 라는 사실을 알 수 있습니다. 왜냐하면 4 를 곱해준 것은 `int` 이기 때문이고, `(c+1)` 행 앞에 `c` 개의 행들이 있는데, 각 행들의 길이가 `b` 이기 때문이죠.

그리고 이 원소가 `(d+1)` 번째에 있다는 사실을 적용하면 (`(c+1)` 행 시작주소) `+ d * 4` 라고 계산될 수 있습니다. 결과적으로 (`x + 4 * b * *c + 4 * d`가 됩니다)


가 됩니다. 참고적으로 이야기 하자면, 수학에서 곱하기 기호가 매우 자주 등장하므로 생각하는 경향이 있는데, 저도 매번 곱하기 기호를 쓰기 불편하므로 생략하도록 하겠습니다. 위 식은 아래의 식과 동일합니다. (`x + 4bc + 4d` 로 간추립니다)

주목할 점은 식에 `b` 가 들어간다는 것입니다. (1 차원 배열에서는 배열의 크기에 관한 정보가 없어도 배열의 원소에 접근할 수 있었는데 말이 1 차원 배열에서는 배열의 크기에 관한 정보가 없어도 배열의 원소에 접근할 수 있었는데 말이죠)

다시 말해, 처음 배열 `arr[a][b]` 를 정의했을 때의 `b` 가 원소의 주소값을 계산하기 위해 필요하다는 것입니다. 우리는 이전의 예제에서 `int**` 로 배열의 이름을 나타낼 수 있다고 생각하였습니다. 하지만 이렇게 선언된 `parr` 으로 컴퓨터가 `parr[1][1]` 원소를 참조하려고 하면 컴퓨터는 `b` 값을 알 수 없기 때문에 제대로된 연산을 수행할 수 없게됩니다.

따라서, 이차원 배열을 가리키는 포인터는 반드시 `b` 값에 대한 정보를 포함하고 있어야 합니다.

결론적으로 포인터 형을 결정하는 것은 다음 두 가지로 요약할 수 있습니다.

1. 가리키는 것에 대한 정보 (예를 들어, `int*` 이면 `int` 를 가리킨다, `char**` 이면 `char*` 을 가리킨다 등등)
2. 1 증가시 커지는 크기 (2 차원 배열에서는 `b * (형의 크기)` 를 의미한다 1 증가시 커지는 크기 (2 차원 배열에서는 `b * (형의 크기)` 를 의미한다)

여기서 1 증가시 커지는 크기가 2 차원 배열에서는 `b * (형의 크기)` 를 의미하는지 궁금한 사람들이 있을 것입니다. 한 번 해봅시다.

```cpp-formatted
/* 1 증가하면 ? */
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};

  printf("arr : %p , arr + 1 : %p \n", arr, arr + 1);

  return 0;
}
```

  성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F142601254B0BD75502819F)

16 진수의 연산과 친숙하지 않더라도 `0x2CF7D8 - 0x2CF7CC` (참고로 예전에도 이야기 했듯이 제 강좌에서 16 진수로 나타내었다는 사실을 명시하기 위해 앞에 `0x` 를 붙인다고 했습니다.) 를 계산해 보면 `0xC` 가 나옵니다. `0xC ,` 즉 십진수로 12 입니다. 근데, 위 배열의 `b` 값은 3 이고 `int` 의 크기는 4 바이트 이므로, `3 * 4 = 12` 가 딱 맞게 되는 것이지요.

왜 그럴까요? 사실, 그 이유는 단순합니다. 거의 맨 위의 그림을 보면 이차원 배열에서 `a` 가 `a[0]` 을 가리키고 있는 그림을 볼 수 있습니다. 만일 1 차원 배열 `b[3]` 이 있을 때 `b + 1` 을 하면 `b[1]` 을 가리키잖아요? 2 차원 배열도 동일하게 `a` 가 1 증가하면 `a[1]` 을 가리키게 됩니다. 다시 말해 두 번째 행의 시작 주소값을 가리키는 포인터를 가리키게 된다는 것이지요.

```cpp-formatted
/* 드디어! 배우는 배열의 포인터 */
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int(*parr)[3];  // 괄호를 꼭 붙이세요

  parr = arr;  // parr 이 arr 을 가리키게 한다.

  printf("parr[1][2] : %d , arr[1][2] : %d \n", parr[1][2], arr[1][2]);

  return 0;
}
```

  성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile27.uf.tistory.com%2Fimage%2F203B851E4B0BDA9D453538)

드디어, 2 차원 배열을 가리키는 포인터에 대해 이야기 하겠습니다. 1 차원 배열을 가리키는 포인터는 간단합니다. (아마 아시겠죠?) 그런데, 2 차원 배열을 가리키는 포인터는 배열의 크기에 관한 정보가 있어야 한다고 했습니다. 2 차원 배열을 가리키는 포인터는 아래와 같이 써주면 됩니다.

```info
  (배열의 형) ( *(포인터 이름) )[2 차원 배열의 열 개수] ;
```

이렇게 포인터를 정의하였을 때 앞서 이야기한 포인터의 조건을 잘 만족하는지 보도록 합시다. 일단, (배열의 형) 을 통해서 원소의 크기에 대한 정보를 알 수 있습니다. 즉, 가리키는 것에 대한 정보를 알 수 있게 됩니다. (조건 1 만족). 또한, `[2` 차원 배열의 열 개수] 를 통해서 1 증가시 커지는 크기도 알게 됩니다. 바로 배열의 형 크기 - 예를 들어 `int` 는 `4, char` 은 `1 * (2 차원 배열의 열 개수)` 만큼 커지게 됩니다.

```cpp-formatted
int (*parr)[3];
```

위와 같이 정의한 포인터 `parr` 을 해석해 보면, `int` 형 이차원 배열을 가리키는데, 그 배열의 열의 개수가 3 개 이군요! 라는 사실을 알 수 있습니다 (정확히 말하면, `int*` 를 가리키는데, 1 증가시 3 이 커진다 라는 의미입니다)

  주의할 점은 괄호로 꼭 묶어주어야 한다는 것입니다. 만일 괄호로 묶지 않는다면 다른 결과가 나오니 주의하세요.

```cpp-formatted
/* 배열 포인터 */
#include <stdio.h>
int main() {
  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int brr[10][3];
  int crr[2][5];

  int(*parr)[3];

  parr = arr;  // O.K
  parr = brr;  // O.K
  parr = crr;  // 오류!!!!

  return 0;
}
```

  앞서, 2 차원 배열에서 원소의 주소값을 계산하는 식을 기억하시는지요? 

$$ x + 4bc + 4d $$

여기서 보아야 할 점은 `a` 의 값이 필요 없다는 것입니다. 다시말해, `b` 값만 알고 있다면 `a` 값과 무관하게 원소에 접근할 수 있다는 것이지요. 위 예제에서도 보시다 싶이, `parr` 이 `arr[2][3]` 과 `brr[10][3]` 을 가리킬 수 있습니다.

왜냐하면 `b` 값, 즉 열의 개수가 동일한 이차원 배열이기 때문이죠. 반면에 `carr` 은 `arr` 과 `b` 값, 즉 3 과 5 가 다르기 때문에 `parr` 에 `crr` 을 대입하면 오류가 생깁니다. 만일 `crr` 을 `parr` 에 대입했다고 쳐도, 컴퓨터는 `parr` 을 이용하여 `carr` 을 참조할 때, 열의 개수가 3 인 배열로 생각하기 때문에 이상한 결과가 나타납니다.



###  포인터 배열

포인터 배열, 말그대로 '포인터들의 배열' 입니다. 위에서 설명한 배열 포인터는 '배열을 가리키는 포인터' 였죠. 두 용어가 상당히 헷갈리는데, 그냥 '언제나 진짜는 뒷부분' 이라고 생각하시면 됩니다. 즉, 포인터 배열은 정말로 배열이고, 배열 포인터는 정말로 포인터 였죠.

```cpp-formatted
/* 포인터배열*/
#include <stdio.h>
int main() {
  int *arr[3];
  int a = 1, b = 2, c = 3;
  arr[0] = &a;
  arr[1] = &b;
  arr[2] = &c;

  printf("a : %d, *arr[0] : %d \n", a, *arr[0]);
  printf("b : %d, *arr[1] : %d \n", b, *arr[1]);
  printf("b : %d, *arr[2] : %d \n", c, *arr[2]);

  printf("&a : %d, arr[0] : %d \n", &a, arr[0]);
  return 0;
}
```

  성공적으로 컴파일 한다면


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile21.uf.tistory.com%2Fimage%2F175932204B0D4005339EDE)
마지막 출력결과는 여러분과 상이할 수 있으나 두 값이 같음을 주목하세요
  일단, `arr` 배열의 정의 부분을 봐봅시다.

```cpp-formatted
int *arr[3];
```

  위 정의가 마음에 와닿나요? 사실, 저는 처음에 배울 때 별로 와닿지 않았습니다. 사실, 이전에도 말했듯이 위 정의는 아래의 정의와 동일합니다.

```cpp-formatted
int* arr[3];
```

이제, 이해가 되시는지요? 우리가 배열의 형을 `int, char` 등등으로 하듯이, 배열의 형을 역시 `int*` 으로도 할 수 있습니다. 다시말해, 배열의 각각의 원소는 '`int` 를 가리키는 포인터' 형으로 선언된 것입니다. 따라서, `int` 배열에서 각각의 원소를 `int` 형 변수로 취급했던 것처럼 `int*` 배열에서 각각의 원소를 포인터로 취급할 수 있습니다. 마치, 아래처럼 말이지요.

```cpp-formatted
arr[0] = &a;
arr[1] = &b;
arr[2] = &c;
```

  각각의 원소는 각각 `int` 형 변수 `a,b,c` 를 가리키게 됩니다.이를 그림으로 표현하면 아래와 같습니다.


![arr[0 에는 a 의 주소값, arr[1 에는 b 의 주소값, arr[2 에는 c 의 주소값](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F121495024B0D491240D174)

`arr[0]` 에는 변수 `a` 의 주소가, `arr[1]` 에는 변수 `b` 의 주소, `arr[2]` 에는 변수 `c` 의 주소가 각각 들어가게 됩니다. 이는 마지막 `printf` 문장에서도 출력된 결과로 확인 할 수 있습니다.

사실, 포인터 배열에 관한 내용은 짧게 끝냈습니다. 하지만, C 언어에서 상당히 중요하게 다루어지는 개념입니다. 아직 여러분이 그 부분에 대해 이야기할 단계가 되지 않았다고 보아, 기본적인 개념만 알려 드린 것입니다. 꼭 잊지 마시길 바랍니다.

자. 이제 배열을 향한 대장정이 끝이 났습니다. 여기까지 부담없이 이해하셨다면 여러분은 C 언어의 성지를 넘게 된 것입니다! 사실, 여러분은 이 포인터를 무려 3 강의를 연달아 들으면서 '도대체 이걸 왜하냐?' 라는 생각이 머리속에 끝없이 멤돌았을 것입니다. 물론, 앞에서도 이야기 했지만 포인터는 다음 단계에서 배울 내용에 필수적인 존재입니다. 사실, 지금은 아무짝에도 쓸모 없는 것 같지만...

여기까지 스크롤을 내리면서도 마음 한 구석에 응어리가 있는 분들은 과감하게 포인터 강좌를 처음부터 읽어 보세요. 저의 경우 포인터만 책 수십권을 찾아보고 인터넷에서 수십개의 자료를 찾아가며 익혔습니다. 그래도 궁금한 내용들은 꼬오옥 댓글을 달아주세요. 저는 정말 아무리 이상하고 괴상한 질문도 환영하니.. 꼭 궁금한 내용을 물어봐주세요 :)

### 생각 해 볼 문제

#### 문제 1

3 차원 배열의, 배열이름과 동일한 포인터는 어떻게 정의될 것인가? (난이도 : 中 3 차원 배열의, 배열이름과 동일한 포인터는 어떻게 정의될 것인가? (난이도 : 中)
(참조 :  2 차원 배열에선 `int (*arr)[4];` 와 같은 꼴이었다)

#### 문제 2

포인터 간의 형변환은 무엇을 의미하는가? 그리고, C 언어에서 포인터 간의 형변환이 위험한 것인가? (난이도 : 中)
(참고적으로, 포인터간의 형 변환은 아직 이야기 한 적이 없으나 한 번 시도는 해보세요)

##@ chewing-c-end