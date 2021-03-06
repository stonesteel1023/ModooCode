----------------
title : C 언어 레퍼런스 - sscanf 함수
cat_title :  sscanf
publish_date : 2011-01-03
--------------


#@ sscanf

```info
#include <stdio.h> // C++ 에서는 <cstdio>

int sscanf ( const char * str, const char * format, ...);
```


문자열에서 형식화 된 데이터를 읽어온다.
`str` 에서 데이터를 형식 문자열(format)에서 지정하는 바에 따라 읽어와 그 데이터를 뒤에 부수적인 인자들이 가리키는 메모리 공간에 저장하게 된다. 이 때, 데이터가 저장되는 방식 역시 형식 문자열에 의해 결정된다.



###  인자


`str`

C 문자열로 `sscanf` 함수가 데이터를 얻어올 문자열이다 C 문자열로 `sscanf` 함수가 데이터를 얻어올 문자열이다.

`format`

C 문자열로 다음의 것들을 포함하고 있다 C 문자열로 다음의 것들을 포함하고 있다.

* 공백 문자 (Whitespace character 이라 부르며, 개행 문자(\n), 탭 문자, 띄어쓰기(' ') 를 일컫는다) : `fscanf` 함수는 비-공백 문자를 읽어들이기 전까지 읽혀지는 모든 공백 문자들을 무시한다.

* 비-공백 문자 (Non whitespcae character), 단 `%` 를 제외한다 : 공백 문자가 아니거나 형식 지정자에 포함되지 않는 것들은 함수로 하여금 다음 문자를 스트림에서 읽어 들이고 이와 이 비-공백 문자와 비교하여 같다면 버리고 다음 문자와 형식으로 진행한다. 만일 다르다면 함수가 종료되고, 스트림에서 읽혀지지 않은 다른 문자들은 모두 남아있게 된다.

* 형식 지정자 : 이는 `%` 로 지정되는 것들로 스트림에서 어떠한 형식으로 데이터를 읽어오고, 또 각각의 형식 지정자에 대응되는 인자에 어떠한 형식으로 저장할 지에 대해 결정한다. 형식 지정자는 아래와 같은 꼴로 생겼다.


```info
%[*][폭(width)][한정자(modifiers)]타입(type)
```

|종류|설명|
|----|----|
|`*`| 데이터를 `stdin` 에서 받아들이지만 무시된다. 물론, 이에 대응되는 인자에는 받아들인 데이터가 저장되지 않고 이 인자는 다음 형식 태그에 대응된다. 예를 들어 `scanf("%*d%d", i,j);` 의 경우 먼저 수를 입력하더라도 `%*d` 형식이므로 무시 된다. 그 다음 수를 입력하면 `%d` 형식 태그가 `j` 가 아닌 `i` 에 대응되어 `i` 에 그 다음 입력한 수가 들어가게 된다. 이 때 `j` 에는 아무런 값도 들어가지 않는다.|
|폭|`stdin` 에서 읽어들일 최대 문자 수를 지정한다. 예를 들어 `scanf("%10s", str);` 로 했을 경우 `stdin` 에서 최대 10 문자를 읽어와 `str` 에 저장한다. 이 때 주의할 점은 `str` 에는 `NULL` 문자가 들어갈 수 있는 충분한 공간이 남아 있어야 한다.|
|한정자|입력받는 데이터의 크기를 지정한다. `int, unsigned int, float` 형에 대해 입력받는 데이터의 크기를 설정할 수 있다. `h` 의 경우 `short int` (`d, i, n` 의 경우) 혹은 `unsigned short int` (`o, u, x` 일 경우). `l` 의 경우 `long int` (`d, i, n` 의 경우) 혹은 `unsigned long int` (`o, u, x` 일 경우), 혹은 `double` (`e, f, g` 일 경우). 마지막으로 `L` 의 경우 `long double` (`e, f, g` 일 경우) 에 사용할 수 있다.|
|타입|데이터를 어떠한 형식으로 혹은 어떠한 값만을 읽어들어야 할 지에 대해 지정해준다. 아래 표를 참고.|

#### sscanf 함수의 타입 지정자들

|타입|대응되는 입력 방식|대응되는 인자의 형태|
|`c`|단일 문자: 하나의 문자를 읽어들인다. 만일 폭에 1 이 아닌 값으로 지정되어 있다면 (기본값은 1) 함수는 폭 만큼의 문자를 읽어들인 후 이에 대응하는 인자가 가리키는 메모리 공간에 저장한다. 이 때 마지막에는 널 문자를 붙이지 않는다.|`char *`|
|`d`|십진법으로 표현된 정수: 말그대로 십진법으로 쓰인 정수로, `+` 나 `-` 기호로 시작할 수도 있다.|`int *`|
|`e, E, f, g, G`|부동 소수점: 소수점을 포함하고 있는 소수(decimal number) 로 `+` 나 `-` 기호로 시작할 수도 있으며, `e` 나 `E` 문자(10 의 지수를 나타내기 위해)를 포함할 수 도 있다. -732.103, 12e-4, +123.10 은 모두 올바른 입력이다.| `float *`|
|`o`|8진법으로 표현된 정수|`int *`|
|`s`|문자열: 공백문자를 찾을 때 까지 문자들을 읽어들인다.|`char *`|
|`u`|부호가 없는 십진법으로 표현된 정수|`unsigned int *`|
|`x, X`|16진법으로 표현된 정수|`int *`|

#### 부수적 인자

형식 문자열의 정의된 순서대로 각 형식 지정자는 이에 대응하는 인자가 가리키는 메모리 공간에 데이터를 집어넣는다. 이 때, 부수적 인자들은 모두 포인터의 형태 (주소값) 여야 한다. 예를 들어서 `i` 라는 변수에 값을 대입하려면 인자로 `&i` 를 전달해야 한다. 절대로 `i` 를 전달하면 안된다.

예를 들면 다음과 같다.

```cpp-formatted
char str[30] = "word";
char c;

sscanf(str, "%c", &c);
```




###  sscanf 함수를 이용해서 문자열을 수로 바꾸기


보통 우리는 문자열을 수로 바꿀 때 `atoi` 함수를 사용하지만, `sscanf` 함수를 통해서도 동일한 작업을 수행할 수 있습니다.

```cpp-formatted
#include <stdio.h>
int main() {
  char str[30] = "1234";
  int i;

  sscanf(str, "%d", &i);

  printf("Number from : '%s' \n", str);
  printf("number : %d \n", i);

  return 0;
}
```

실행 결과


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile4.uf.tistory.com%2Fimage%2F2019520D4B8290B942A3FF)

위와 같이 `str` 에서 `sscanf` 함수로 `%d` 형식, 즉 정수 형식으로 수를 읽어오면 이 값을 `i` 에 저장하게 된다.

위 함수의 장점은 `%d` 뿐만이 아니라 `%o` 나 `%f, %x` 등이 가능하기 때문에 팔진수나 부동소수점 수, 16 진수 들도 모두 동일한 방법으로 입력받을 수 있다. 반면에 `atoi` 계열 함수들은 `atoi, atof` 등 세분화 되어 있기 때문에 불편한 면이 있다.


###  리턴값


입력 성공 시에 이 함수는 읽어들인 것의 개수를 리턴한다. 물론, 0 이 리턴될 수 도 있다. (이 경우에는 `str` 에서 `format` 에서 지정한 형식과 일치하는 데이터가 없어서 아무것도 읽어들이지 않은 경우 발생한다. 아래의 `EOF` 가 리턴되는 경우와 조금 다르다)

만일 어떠한 데이터도 성공적으로 읽기 전에 입력이 실패한다면 `EOF` 가 리턴된다.



###  실행 예제



```cpp-formatted
/*sentence 로 부터 Rudolph 와 12 라는 수를 sscanf 함수를 이용해 추출한다.이
 * 예제는 http://www.cplusplus.com/reference/clibrary/cstdio/sscanf/에서
 * 가져왔습니다. */
#include <stdio.h>
int main() {
  char sentence[] = "Rudolph is 12 years old";
  char str[20];
  int i;
  sscanf(sentence, "%s %*s %d", str, &i);
  printf("%s -> %d\n", str, i);
  return 0;
}
```


실행 결과


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile8.uf.tistory.com%2Fimage%2F166187534D209A7F15737F)




###  연관된 함수





*  [scanf](http://itguru.tistory.com/36)  :  표준입력(stdin) 으로 부터 데이터를 형식에 맞추어 읽어온다.

*  [sprintf](http://itguru.tistory.com/66)  :  문자열에 데이터를 형식에 맞추어 쓴다.