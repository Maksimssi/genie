# 온라인 중고 서점 Genie)

* * *

## 📚목차
>
>###   - [프로젝트 개요](#프로젝트-개요)
>###   - [Stacks](#Stacks)
>###   - [ERD](#ERD)
>###   - [주요 기능](#주요-기능)

* * *
## 프로젝트 개요  

>팀원들과 개발 관련 서적에 대한 이야기를 나누던중 <br>
>온라인 서점인 알라딘을 사용하며 불편했던 점을 개선하고자 프로젝트의 주제로 선정하게되었습니다.<br>
>
>사용자는 도서 검색, 구매 및 중고 도서 판매가 가능합니다.<br>
>관리자는 사용자 관리, 등록된 게시글 및 도서의 관리가 가능합니다.
>
>Spring, mybatis를 사용해 CRUD를 구현하고 기본적인 REST API를 구현하였습니다.<br>
>사용자의 편의를 위해 python-flask를 활용한 챗봇 시스템을 구현하였습니다.

>### 개발 기간 및 인원
>24.02.05 ~ 24.03.22<br>
>백엔드 4명
* * *
## Stacks
<div align=center> 
  <img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <br> 
  <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
  <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> 
  <br>
  <img src="https://img.shields.io/badge/oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white">
  <img src="https://img.shields.io/badge/apache tomcat-F8DC75?style=for-the-badge&logo=apachetomcat&logoColor=white">
</div>

* * *

## ERD
![GENIE_ERD](https://github.com/Maksimssi/genie/assets/142511332/0db3dfcb-c55e-4702-ae28-77c3bddf08ee)

## 주요 기능
### 요약

|공통|사용자|관리자|
|---|---|---|
|-회원가입,로그인<br> -상품 목록 및 상세 페이지 조회|-찜하기,장바구니 저장<br> -게시판 문의하기<br> -상품 리뷰|-등록 상품 관리<br> -사용자 관리<br> -주문 상태 관리|

## 공통 기능
### 결제
- 토스 페이먼츠 Core API를 연동하여 간편 결제 기능 구현 및 결제 위젯 이용
### 챗봇
- 사용자가 키워드를 입력하면 키워드와 관련된 가장 유사한 답변 출력.
  - sklearn-cosine_similarity를 활용, 코사인 유사도를 계산하여 답변 정확도 향상
  - CORS 모듈을 사용하여 Spring 서버와 연동 

최근본상품



* * *
