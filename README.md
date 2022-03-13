<img src ="https://user-images.githubusercontent.com/90089275/158053748-d2aa6770-7bb9-4ad2-a1e4-606143467ec6.png" width="200" height="300">

<br><br>

---
# Target site
<img src = "https://user-images.githubusercontent.com/90089275/158053540-dbe10e54-bdf5-40a6-8a10-2f8730f4abda.png" width="1000" height="500">

* ## 사이트 소개  
    [Site Link](https://kukka.kr)
    
    꽃을 일상에서 가볍게 즐기는 핀란드의 문화를 한국에 전파하는 것이 목표 

    우리는 한국에도 멋진 ‘꽃 브랜드’가 생길 수 있다고 믿고 행동하는 사람들이 모인 곳  

* ## 사이트 선정 이유
    * 깔끔한 UI
    * 이커머스의 기본 기능인 로그인, 회원가입, 상품 조회, 옵션 선택, 장바구니, 주문 기능을 모두 담고 있음

<br><br>

---
# 초기기획 & ERD

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

---
# 개발기간 및 팀원

* ## 개발기간  
    2022.02.28 ~ 2022.03.10  

* ## 개발인원 및 파트

    * Front-end  
        * 신윤숙 - Login, Order
        * 전슬기 - Product List, Product Detail
        * 김준영 - Sign Up, Cart 
        
    * Back-end   
        * 김기현 - SignUp, Product List API, Order API
        * 이지원 - Cart API
        * 박건규 - SignIn, Product Detail API, Order API
<br><br>

---
# 적용 기술 및 구현 기능

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
        - 정규 표현식을 통한 이메일아이디 및 비밀번호 유효성 검사
        - 비밀번호 암호화 및 JWT 발급
        - request.header에 담긴 token을 통해 로그인 여부를 검사
    * 상품 리스트 페이지
        - 판매 상품의 분류에 따라 filtering
        - 사용자가 원하는 기준에 따라 sorting
    * 상품 상세 페이지
        - 상품 상세페이지에 필요한 데이터를 products와 product_size, size 테이블에서 필터링 하여 엔드 포인트로 전달
        - 필요한 옵션을 선택하여 장바구니로 저장할 수 있도록 구현
    * 장바구니
        - 장바구니 상품 추가, 조회, 수량 수정, 선택 삭제 기능 구현
    * 주문
        - 장바구니에서 넘겨받은 정보를 넘겨받아 구매
        - 일련의 과정에 원자성을 부여하기 위해 transaction 사용
        - 구매 한 상품은 장바구니에서 삭제
<br><br>

---
# API 기능정의서
기술 예정

<br><br>

---
# 시연 영상
![ezgif com-gif-maker](https://user-images.githubusercontent.com/60570733/158055641-023b0d1c-9604-4f4e-8749-1d4cc4bc8d53.gif)

![로그인](https://user-images.githubusercontent.com/90089275/158054617-ecaac1da-f80c-4217-add2-42f94693e431.gif)
![상품상세](https://user-images.githubusercontent.com/90089275/158054619-54713ed7-3836-4d73-b9d0-f639dc61df29.gif)
![장바구니](https://user-images.githubusercontent.com/90089275/158054623-0376486c-cbda-428b-ac5b-29befe9cc2d0.gif)
![주문결제](https://user-images.githubusercontent.com/90089275/158054624-86307905-960a-4ed3-8c49-44bc23b51ec8.gif)


<br><br>
---
# Reference
* 이 프로젝트는 [꾸까](https://kukka.kr) 사이트를 참조하여 학습목적으로 만들었습니다.
* 실수수준의 프로젝트이지만 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다

![Footer](https://capsule-render.vercel.app/api?type=waving&color=ffcc51&height=100&section=footer)
