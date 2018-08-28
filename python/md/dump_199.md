----------------
title : 모든 컴퓨터 과학자가 알아야 할 부동 소수점의 모든 것(What Every Computer Scientists Should Know About Floating Point Arithmetic)
--------------




```warning

오픈북 프로젝트는 인터넷 상의 양질의 컴퓨터 문서를 번역하여 우리 말로 공급하는 프로젝트 입니다. 번역된 문서들은 인터넷 상으로 어떠한 제한 조건 없이 배포되고 있으며, 다만 원 번역자의 허락 없는 무단 수정을 금합니다. 

현재 까지 번역된 문서들의 리스트는 여기에서 확인하시면 됩니다.
```






이번에 번역된 문서는 '모든 컴퓨터 과학자가 알아야 할 부동 소수점의 모든 것(What Every Computer Scientists Should Know About Floating Point Arithmetic)' 으로, 제목 그대로 컴퓨터를 공부하는 사람이라면 적어도 한 번은 읽어야 하는 부동 소수점 분야의 대부분의 내용을 망라하고 있는 문서입니다. 부동 소수점(floating point) 은 우리가 정말 많이 코딩하고 사용하는 것이지만 (C 의 float, double) 사실 이 자료형이 컴퓨터 내부에서 어떻게 처리되고 있는지 자세히 알고 있는 사람은 정말 드뭅니다. 물론 간단한 프로그래밍을 위해서 그 자세한 내용까지 모두 알라는 이야기는 아니지만, 적어도 부동 소수점을 사용하는 큰 프로젝트를 개발한다면, 대략적인 부동 소수점 연산의 원리 정도는 알고 있어야지 효율적인 프로그래밍을 할 수 있습니다. 


이 문서는 크게 세 장으로 나뉘어 있는데, 첫 번째 장에서는 부동소수점에서 가장 중요한 부분인 반올림과, 오차를 계산하는 방법에 대해 알아봅니다. 그리고 두 번째 장에서는 IEEE 부동 소수점 표준에 대해 알아볼 것이고, 마지막 장에서는 이러한 부동 소수점에 관련된 정보를 시스템 적 측면에서 알아볼 것입니다. 


이 문서의 주요 키워드들은 다음과 같습니다 : 비정규화 수 (Denormalized number), 예외 (Exception), 부동 소수점 (Floating-point), 부동 소수점 표준 (Floating-point standard), 점진적 언더플로우(Gradual underflow), 보호 숫자 (Guard digit), NaN, 오버플로우 (Overflow), 상대 오차(Relative error), 반올림 오차 (Rounding error), 반올림 모드 (Rounding mode), Ulps, 언더 플로우 (Underflow)


아마 이 문서를 한 번 정도만 꼼꼼하게 정독하시면, 여러분이 프로그래밍을 하면서 필요한 부동 소수점 관련 지식은 거의 얻을 수 있을것입니다. 


오탈자나, 틀린 내용은 댓글로 달아주시거나, kev0960@gmail.com 으로 보내주시면 감사하겠습니다. 

```cpp

파일 다운로드는 아래 pdf 파일을 받으시면 됩니다. 전체 페이지 수는 60 페이지 가량 됩니다. 

![](http://)
 모든 컴퓨터 과학자가 알아야 할 부동 소수점의 모든것.pdf

```





공감1sns신고
저작자표시

'Open Book Project' 카테고리의 다른 글C++ 11 자주 질문되는 것들 모음 (C++ 11 FAQs - Bjarne Stroustup)(4)
2013.10.02모든 컴퓨터 과학자가 알아야 할 부동 소수점의 모든 것(What Every Computer Scientists Should Know About Floating Point Arithmetic)(12)
2013.08.04오픈북 프로젝트 - 양질의 컴퓨터 문서 공급 프로젝트(25)
2013.08.04
