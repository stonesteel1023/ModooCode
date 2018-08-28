----------------
title : C++ 레퍼런스 - ios_base::imbue
--------------



```warning
이 레퍼런스의 모든 내용은 http://www.cplusplus.com/reference/iostream/
 의 내용을 기초로 하여, Microsoft 의 MSDN 과 Bjarne Stroustrup 의 책 <<The C++ 
Programming Language>> 를 참고로 하여 만들어졌습니다. 이는 또한 저의 개인적인 C++ 능력 향상과 '저의 모토인 지식 전파' 를 위해 모든 이들에게 공개하도록 하겠습니다.
```

```info
아직 C++ 에 친숙하지 않다면 씹어먹는 C++ 강좌는 어때요?
```


ios_base::imbue




```cpp
locale imbue ( const locale& loc );
```


로케일을 설정(imbue) 한다.
loc 를 스트림의 새로운 로케일(locale) 객체로 사용하여, 로케일과 관련있는 작업에 이를 사용한다. 

imbue 함수 종료 직전에 imbue_event 가 발생되며 register_callback 함수를 통해 등록되었던 함수들이 모두 호출되게 된다. 





###  인자




loc

  스트림의 새롭게 설정될 로케일 객체이다.




###  리턴값




  함수 호출 이전 상태의 로케일 객체



###  실행 예제




```cpp
/*이 예제는http://www.cplusplus.com/reference/iostream/ios_base/imbue/에서 가져왔습니다.*/#include <iostream>
#include <locale>
using namespace std;
int main()
{
    locale mylocale("french");      // 로케일 객체를 '프랑스' 로 설정한다.
    cout.imbue( mylocale );   // 이를 cout 로케일로 설정한다.
    cout << (double) 3.14159 << endl; //프랑스에서는 . 대신 , 를 사용하므로 3,14159 로 표시된다. 
    return 0;
}
```

실행 결과

![](http://img1.daumcdn.net/thumb/R1920x0/?fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F13095D574E4E10412DED75)



###  연관된 것들




* ios_base::getloc
 : 현재 로케일을 알아온다.






공감sns신고
저작자표시

'C++ Reference > IOstream' 카테고리의 다른 글C++ 레퍼런스 - ios_base::xalloc 함수(0)
2011.10.22C++ 레퍼런스 - ios_base::getloc 함수(1)
2011.08.20C++ 레퍼런스 - ios_base::imbue(0)
2011.08.20C++ 레퍼런스 - ios_base::register_callback 함수(0)
2011.08.20C++ 레퍼런스 - ios_base::precision 함수(0)
2011.08.19C++ 레퍼런스 - ios_base::usetf 함수(0)
2011.08.19
