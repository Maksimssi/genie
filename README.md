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

>CRUD 기능을 포함한 REST API를 설계하고 구현하였습니다.<br>
>이를 통해 REST API 작동 방식을 이해하고 관련된 기술과 활용 능력을 습득했습니다.
>

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


### 토스 페이먼츠 코어 API
- ■ 상품 결제 기능 구현
### 챗봇
- 사용자가 키워드를 입력하면 키워드와 관련된 가장 유사한 답변 출력.
  - konlpy 패키지로 키워드 형태소 분석
  - sklearn를 활용, 코사인 유사도를 계산하여 답변 정확도 향상
  - CORS 모듈을 사용하여 Spring 서버와 연동

### 최근본상품
 - 도서 상세페이지 접속시 쿠키를 생성하여 모든 페이지에서 최근 본 상품을 도서 이미지로 제공



* * *
