----------------
title : C++ 레퍼런스 - ios::eof 함수
cat_title :  ios::eof
ref_title : eof
publish_date : 2011-10-23
--------------



```warning
이 레퍼런스의 모든 내용은 [http://www.cplusplus.com/reference/iostream/](http://www.cplusplus.com/reference/iostream/) 의 내용을 기초로 하여, Microsoft 의 MSDN 과 Bjarne Stroustrup 의 책 <<The C++ Programming Language>> 를 참고로 하여 만들어졌습니다. 이는 또한 저의 개인적인 C++ 능력 향상과 ' [저의 모토인 지식 전파](http://itguru.tistory.com/notice/107)'를 위해 모든 이들에게 공개하도록 하겠습니다.
```

```info
아직 C++ 에 친숙하지 않다면 [씹어먹는 C++ 강좌](http://itguru.tistory.com/135)는 어때요?
```

#@ ios::eof

```info
bool eof ( ) const;
```


`eofbit` 이 설정되었는지 확인한다.

이 함수는 스트림의 `eofbit` 오류 상태 플래그가 이전의 입출력 작업으로 인해 설정되었을 때 `true` 를 리턴한다. `eofbit` 플래그는 입력 작업 중 **파일 끝(End Of File)** 에 도달하였을 때 설정되는 플래그 이다.



###  인자




없다



###  리턴값




스트림의 오류 상태 플래그 `eofbit` 이 설정되었을 때 `true` 를 리턴한다. `eofbit` 는 입력 작업 중 **파일 끝(End Of File)** 에 도달하였을 때 설정된다. 그 외의 경우 `false` 를 리턴한다.



###  템플릿 멤버 정의




```cpp-formatted
(basic_ios<charT, traits>)bool eof() const;
```




###  연관된 함수

*  [ios::fail](http://itguru.tistory.com/165)  :  `failbit` 이나 `badbit` 이 설정되어 있는지 확인한다.
*  [ios::bad](http://itguru.tistory.com/166)  :  `badbit` 이 설정되어 있는지 확인한다.
*  [ios::good](http://itguru.tistory.com/164):  스트림에 어떠한 오류 플래그도 설정되지 않았는지 확인한다.
*  [ios::rdstate](http://itguru.tistory.com/171)  :  오류 상태 플래그를 얻는다.
*  [ios::clear](http://itguru.tistory.com/180)  :  오류 상태 플래그를 설정한다.