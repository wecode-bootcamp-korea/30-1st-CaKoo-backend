# cakoo 프로젝트
<img width="234" alt="스크린샷 2022-03-13 오후 7 58 05" src="https://user-images.githubusercontent.com/60570733/158056356-f913f84b-a0c9-4094-9c0b-e6b23c2d6faa.png">
케이쿠는 꾸까를 모티브 해 케이크를 판매하는 이커머스 사이트로 구매하기까지의 로직에 집중하여 클론코딩을 진행하였습니다. 원하는 케이크 조건 검색, 케이크 리스트 조회, 케이스 상세 페이지, 상품 장바구니 넣기, 수량 선택, 주문까지 하나의 플로우를 구현했습니다.
<br><br>

### 🚀 개발 인원 및 기간
* 개발 기간 : 2022/2/28 ~ 2022/3/11 (2주간)
* 프론트엔드 3명, 백엔드 3명
    * Back-end   
        * 김기현 - Modeling, SignUp, Product List API, Order API
        * 이지원 - Modeling, Cart API
        * 박건규 - Modeling, SignIn, Product Detail API, Order API
    * Front-end  
        * 신윤숙 - Login, Order
        * 전슬기 - Product List, Product Detail
        * 김준영 - Sign Up, Cart 
     * <a href="https://github.com/wecode-bootcamp-korea/30-1st-CaKoo-frontend">프론트 github 링크</a>
<br><br>


# 📍 데모 영상

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/60570733/158057150-f3502d34-5bee-4b4b-a78a-baccb133f661.gif)


<br><br>


# 🌷 Target site
<img src = "https://user-images.githubusercontent.com/90089275/158053540-dbe10e54-bdf5-40a6-8a10-2f8730f4abda.png" width="1000" height="400">

* ## 사이트 소개  
    [Site Link](https://kukka.kr)
    
    꽃을 일상에서 가볍게 즐기는 핀란드의 문화를 한국에 전파하는 것이 목표 

    우리는 한국에도 멋진 ‘꽃 브랜드’가 생길 수 있다고 믿고 행동하는 사람들이 모인 곳  

* ## 사이트 선정 이유
    * 깔끔한 UI
    * 이커머스의 기본 기능인 로그인, 회원가입, 상품 조회, 옵션 선택, 장바구니, 주문 기능을 모두 담고 있음

<br><br>


# 💡 초기기획 & ERD

## ERD
![image](https://user-images.githubusercontent.com/90089275/158053700-521e9dce-0720-49c7-933a-1c2781cae0a7.png)

## User flow
<img src="https://user-images.githubusercontent.com/90089275/158054162-33f65fd5-e4ca-4948-ae62-22c90769e04f.png">


## 초기기획 및 구현 목표
* 짧은 기간동안 기능구현에 집중해야하므로 사이트의 디자인과 기획만 클론
* 개발은 초기세팅부터 전부 직접 구현
* 사이트 카테고리 중 '꽃다발'만 구현
* 필수 구현 사항을 회원가입, 로그인, 상품 조회, 장바구니, 주문기능으로 설정 
* 한 상품에 여러 옵션(사이즈)이 적용될 수 있게 기획

<br><br>



# 📝 적용 기술 및 구현 기능

* ## 기술 스택
    * ### Front-end  
        <a href="#"><img src="https://img.shields.io/badge/HTML-DD4B25?style=plastic&logo=html&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/SASS-254BDD?style=plastic&logo=sass&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/javascript-EFD81D?style=plastic&logo=javascript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/React-68D5F3?style=plastic&logo=react&logoColor=white"/></a>
    * ### Back-end  
        <a href="#"><img src="https://img.shields.io/badge/python-3873A9?style=plastic&logo=python&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Django-0B4B33?style=plastic&logo=django&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/MySQL-005E85?style=plastic&logo=mysql&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/bcrypt-525252?style=plastic&logo=bcrypt&logoColor=white"/></a>
     <a href="#"><img src="https://img.shields.io/badge/postman-F76934?style=plastic&logo=postman&logoColor=white"/></a>
    * ### Common  
        <a href="#"><img src="https://img.shields.io/badge/git-E84E32?style=plastic&logo=git&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/RESTful API-415296?style=plastic&logoColor=white"/></a>
    * ### Communication  
        <a href="#"><img src="https://img.shields.io/badge/github-1B1E23?style=plastic&logo=github&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Slack-D91D57?style=plastic&logo=slack&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Trello-2580F7?style=plastic&logo=trello&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Notion-F7F7F7?style=plastic&logo=notion&logoColor=black"/></a>
* ## 구현기능
    * 회원가입 / 로그인
        - 정규 표현식을 통한 이메일, 아이디 및 비밀번호 유효성 검사
        - 비밀번호 암호화 및 JWT 발급
        - request.header에 담긴 token을 통해 로그인 여부를 검사
    * 상품 리스트 페이지
        - Q를 활용해 판매 상품의 분류에 따른 filtering 적용
        - 가격, 생산 순에 따른 sorting 적용
        - pagination
    * 상품 상세 페이지
        - 상품 상세페이지에 필요한 데이터를 products와 product_size, size 테이블에서 필터링 하여 엔드 포인트로 전달
        - 필요한 옵션을 선택하여 장바구니로 저장할 수 있도록 구현
    * 장바구니
        - 장바구니 상품 추가, 조회, 수량 수정, 선택 삭제 기능 구현
    * 주문
        - 장바구니에서 넘겨받은 정보를 넘겨받아 구매
        - 일련의 과정에 원자성을 부여하기 위해 transaction 사용
        - 주문 후 주문내역을 받을 수 있는 로직 구현
        - 구매 한 상품은 장바구니에서 삭제
<br><br>


## API 문서화
<img width="1676" alt="스크린샷 2022-03-13 오후 8 11 19" src="https://user-images.githubusercontent.com/60570733/158056769-5434eb35-772b-40e2-9a61-5edb6731089e.png">

* 포스트맨을 이용해 API 문서화를 진행했습니다.
* 이번 프로젝트에서 쿼리파라미터(size, price, created, offset, limit 등)로 많은 값들을 받아야했기 때문에 API 문서화가 굉장히 중요했습니다.
* 프론트엔드와 소통 시 문서를 통해 1차적으로 커뮤니케이션 비용을 줄일 수 있었습니다.
<br><br>

## Trello
<img width="1669" alt="스크린샷 2022-03-13 오후 8 17 03" src="https://user-images.githubusercontent.com/60570733/158056941-78f7eece-2557-41c5-a1e3-f6b0407b535c.png">

* 트렐로를 이용해 모든 업무들을 세분화 시켜 하나의 티켓으로 만들었습니다.
* 팀원들과 공유해야할 내용은 공지 탭을 통해 단일화하였습니다.
* 전체 프로세스를 네 가지 카테고리로 나눠서 각각의 티켓을 과정에 따라 하나씩 이동 시키며 프로젝트의 모든 일정과 업무를 관리했습니다.
* 각자 데일리 스탠드업 미팅 로그를 작성하고 10~20분내로 짧게 진행상황 및 블로커를 점검했습니다.
* 스프린트 주기를 지켜 한 스프린트가 끝나고 회고미팅을 해 발전방향을 모색하였습니다.

<br>

# Reference
* 이 프로젝트는 [꾸까](https://kukka.kr) 사이트를 참조하여 학습목적으로 만들었습니다.
* 실수수준의 프로젝트이지만 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다

![Footer](https://capsule-render.vercel.app/api?type=waving&color=ffcc51&height=100&section=footer)


