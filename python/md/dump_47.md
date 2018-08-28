----------------
title : C 언어 레퍼런스 - putchar 함수
--------------



```warning
아직 C 언어와 친숙하지 않다면, 씹어먹는 C 언어 강좌를 보는 것이 어떻까요?
```

putchar



```info
#include <stdio.h> // C++ 에서는 <cstdio>int putchar ( int character );
```


표준 출력(stdout) 에 문자를 쓴다.
표준 출력에서 현재 위치 표시자가 가리키는 곳에 문자를 쓴 뒤, 위치 표시자를 다음 위치로 전진시킨다.
putchar 함수는 putc(character, stdout) 과 동일하다. 



###  인자




character

표준 출력에 쓸 문자. 이 때 문자는 int 형태로 형변환되어 전달된다.



###  리턴값




오류가 하나도 없다면 표준 출력에 쓰여진 문자가 반환된다.
만일 오류가 발생한다면 EOF 가 반환되고 오류 표시자가 설정된다. 



###  실행 예제




```cpp
/* 화면에 'p' 를 출력한다 */#include <stdio.h>int main (){    char ch = 'p';    putchar (ch);    return 0;}
```

실행 결과


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile3.uf.tistory.com%2Fimage%2F16415F144B6AB65213766E)

```cpp
/* 화면에 알파벳 A 부터 Z 까지 출력한다.이 예제는 http://www.cplusplus.com/reference/clibrary/cstdio/putchar/에서 가져왔습니다. */#include <stdio.h>int main (){    char c;    for (c = 'A' ; c <= 'Z' ; c++) {        putchar (c);    }    return 0;}
```

실행 결과


![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F1304D4134B6AB693652E08)




###  연관된 함수





* putc
  :  스트림에 문자를 쓴다.

* fputc
 :  스트림에 문자를 쓴다.

* getchar
  :  표준 입력(stdin) 에서 문자를 받는다.







공감sns신고
저작자표시

'C Reference > stdio.h (cstdio)' 카테고리의 다른 글C 언어 레퍼런스 - ungetc 함수(0)
2010.02.04C 언어 레퍼런스 - puts 함수(0)
2010.02.04C 언어 레퍼런스 - putchar 함수(0)
2010.02.04C 언어 레퍼런스 - putc 함수(0)
2010.02.04C 언어 레퍼런스 - gets 함수(3)
2010.02.03C 언어 레퍼런스 - getchar 함수(7)
2010.02.03
