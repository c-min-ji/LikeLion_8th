# HTTP, JSON, API 
* HTTP 
    * 의미
        * **H**yper **T**ext **T**ransfer **P**rotocol

        * 참조를 통해 한 문서에서 관련된 문서들로 넘나들며 원하는 정보를 얻을 수 있게 해주는 텍스트 : Hyper Text
        
        * 인터넷을 통해서 정보를 주고받을 때 지켜야하는 규칙 : Transfer Protocol
    <hr>
    
    * 구성
        * request & response
    <hr>

    * 요청 메소드
    
        * **GET** 
            * URL에 표시된 리소스를 가져오기
        * **POST**
            * body에 정보를 담아 서버에 입력
        * **PUT**
            * URL에 표시된 리소스와 바꿔치기
        * **PATCH**
            * PUT과 다르게 일부만 수정
        * **DELETE**
            * URL에 표시된 특정 리소스를 삭제
<hr>

* JSON
    * 의미
        * **J**ava **S**cript **O**bject **N**otation
    <hr>

    * 형식
        * key : value
        * ex) "name": "minji" / "lecture" : 2
    > 데이터 교환할 때, JSON 형식을 자주 사용한다. <br>이전엔 XML 사용했다
    <hr>

    * 특징
        * 기존 XML보다 **가벼움**
        * **많은 프로그래밍 언어** 지원
        * 전송 시: 직렬화 과정을 거침
            * 직렬화 : 스트링 형식(연속적인 데이터 형식)으로 만듦
        * 수신 시: 역질렬화 과정 거침
            * 역직렬화 : 스트링 형식이 된 자료를 오브젝트형식(원래 객체 형식)으로 만듦
        <hr>
        
        * 참고 사이트
            * https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
<hr>

* API
    * 의미 
        * **A**pplication **P**rogramming **I**nterface
            * 서비스들이 제공해주는 데이터들에 접근하고 사용할 수 있도록 도와주는 도구 : Programming Interface
            * 리모컨 같은 존재.....!
    <hr>

    * 종류
        * SOAP
            * **S**imple **O**bject **A**ccess **P**rotocol
        * REST
            * **Re**presentational **S**tate **T**ransfer
            > REST는 하나의 아키텍쳐<br>
            소프트웨어 아키텍쳐 **:** 소프트 웨어를 설계하는 **지침**과 **원칙**
            * 구성요소
                * 자원 : GET/**likelion/member/8th/list** <br> PATCH/**likelion/member/8th/최민지**
                * 행위 : **GET**/likelion/member/8th/list <br> **PATCH**/likelion/member/8th/최민지
                * 표현 : {<br>"members : ["최멋사", ... , "하멋사"]<br>}
        * GraphQL
            * **Graph** **Q**uery **L**anguage