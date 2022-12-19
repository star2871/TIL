# 크롤링(crawling) 이란?
- ## Web상에 존재하는 Contents를 수집하는 작업 (프로그래밍으로 자동화 가능)
  - ### HTML 페이지를 가져와서, HTML/CSS등을 파싱하고, 필요한 데이터만 추출하는 기법
  - ### Open API(Rest API)를 제공하는 서비스에 Open API를 호출해서, 받은 데이터 중 필요한 데이터만 추출하는 기법
  - ### Selenium등 브라우저를 프로그래밍으로 조작해서, 필요한 데이터만 추출하는 기법


# 크롤링(crawling)과 스크래핑(scraping)의 차이
- ## 웹 크롤링 - 웹 크롤러(자동화 봇)가 일정 규칙으로 웹페이지를 브라우징 하는 것
- ## 웹 스크래핑 - 웹 사이트 상에서 원하는 정보를 추출하는 기술


# 파싱(Parsing)이란?
- ## 파싱(Parsing)은 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보로 가공하는 것을 말하는 것이다. 다이아몬드가 많이 나오는 위치로 이동을 일단 한 후에 돌을 많이 캔다음에 다이아몬드만 쏙쏙 뽑아서 보석으로 가공하는 과정하고 비슷하다고 보면 된다.


# Open API(Rest API)란?
- ## API: Application Programming Interface의 약자로, 특정 프로그램을 만들기 위해 제공되는 모듈(함수 등)을 의미
- ## Open API: 공개 API라고도 불리우며, 누구나 사용할 수 있도록 공개된 API (주로 Rest API 기술을 많이 사용함)
- ## Rest API: Representational State Transfer API의 약자로, HTTP프로토콜을 통해 서버 제공 기능을 사용할 수 있는 함수를 의미
  - ### 일반적으로 XML, JSON의 형태로 응답을 전달(원하는 데이터 추출이 수월)


# JSON 이란?
- ## JavaScript Object Notation 줄임말
- ## JSON은 서버와 클라이언트 또는 컴퓨터/프로그램 사이에 데이터를 주고 받을 때 사용하는 데이터 포멧
- ## 키와 값을 괄호와 세미콜론과 같이 간단한 기호로 구성하여 표현할 수 있고, 언어나 운영체제에 구애받지 않기 때문에 많이 사용됨
- ## 특히 웹/앱 환경에서 Rest API를 사용하여, 서버와 클라이언트 사이에 데이터를 주고 받을때 많이 사용
- ## JSON 포멧 예
  ## { "id":"01", "language": "Java", "edition": "third", "author": "Herbert Schildt" }
 