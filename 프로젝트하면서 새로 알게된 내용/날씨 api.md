# OpenWeather API
## Weather API

# 1. OpenWeather 회원가입
- ## 회원가입 후 내 이름에서 My API keys를 클릭하면 나의 API key를 볼 수 있다.

# 2. API 선택
- ## 현재 날씨를 받을 수 있는 Current weather data를 선택한다.
- ## Current weather data 호출 방식 중 도시 이름으로 API call은 아래와 같다.
> ### api.openweathermap.org/data/2.5/weather?q={도시이름}&appid={API key}

# 3. 데이터 호출해보기
![(/images_otyvs1109_post_85bd5efc-e74e-4062-a89e-66a5de99def8_Untitled.png)](https://github.com/star2871/TIL/blob/master/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%ED%95%98%EB%A9%B4%EC%84%9C%20%EC%83%88%EB%A1%9C%20%EC%95%8C%EA%B2%8C%EB%90%9C%20%EB%82%B4%EC%9A%A9/images_otyvs1109_post_85bd5efc-e74e-4062-a89e-66a5de99def8_Untitled.png)

# 4. 코드 작성
  - ## index.html
  ```
  <!DOCTYPE html>
  <html>
  <head>
      <title>현재 날씨는?</title>
      <script src="main.js">
      </script>
  </head>
  <body>
      
  </body>
  </html>
  ```

  - ## main.js
  ```
  <!DOCTYPE html>
  <html>
  <head>
      <title>현재 날씨는?</title>
      <script src="main.js">
      </script>
  </head>
  <body>
      
  </body>
  </html>
  main.js
  const getJSON = function(url, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      const status = xhr.status;
      if(status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
  };

  getJSON('http://api.openweathermap.org/data/2.5/weather?q=seoul&appid=1eb1d18602c0e2dde562cdc2005a4495&units=metric',
  function(err, data) {
    if(err !== null) {
      alert('예상치 못한 오류 발생.' + err);
    } else {
      alert(`현재
        온도는 ${data.main.temp}°
        풍속은 ${data.wind.speed}m/s
        습도는 ${data.main.humidity}%
  입니다.
  오늘의
        최고기온은 ${data.main.temp_max}°
        최저기온은 ${data.main.temp_min}°
  입니다.`)
    }
  });
  ```
  - ## 결과창
  ![/images_otyvs1109_post_25553726-c7ba-47b4-af92-5c6382de2d9c_Untitled%201.png](https://github.com/star2871/TIL/blob/master/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%ED%95%98%EB%A9%B4%EC%84%9C%20%EC%83%88%EB%A1%9C%20%EC%95%8C%EA%B2%8C%EB%90%9C%20%EB%82%B4%EC%9A%A9/images_otyvs1109_post_25553726-c7ba-47b4-af92-5c6382de2d9c_Untitled%201.png))

# 5. 페이지 향상
```
getJSON('([http://api.openweathermap.org/data/2.5/weather?q=seoul&appid=1eb1d18602c0e2dde562cdc2005a4495&units=metric](http://api.openweathermap.org/data/2.5/weather?q=seoul&appid=1eb1d18602c0e2dde562cdc2005a4495&units=metric))',
function(err, data) {
if(err !== null) {
alert('예상치 못한 오류 발생.' + err);
} else {
loadWeather(data);
}
});

function loadWeather(data) {
let location = document.querySelector('.location');
let currentTime = document.querySelector('.current-time');
let currentTemp = document.querySelector('.current-temp');
let feelsLike = document.querySelector('.feels-like');
let minTemp = document.querySelector('.min-temp');
let maxTemp = document.querySelector('.max-temp');
let icon = document.querySelector('.icon');
let weatherIcon = data.weather[0].icon;

let date = new Date();
let month = date.getMonth() + 1;
let day = date.getDate();
let hours = date.getHours();
let minutes = date.getMinutes();

location.append([data.name](http://data.name/));
currentTemp.append(`${data.main.temp}°`);
feelsLike.append(`${data.main.feels_like}°`);
maxTemp.append(`최고: ${data.main.temp_max}°`);
minTemp.append(`최저: ${data.main.temp_min}°`);
icon.innerHTML = `<img src='<http://openweathermap.org/img/wn/${weatherIcon}.png>'>`;

currentTime.append(`${month}월 ${day}일 ${hours}:${minutes}`);

}
```
# 날씨 예보 api
```
<title>날씨</title>

<script type = "text/javascript" src="js/jquery-3.3.1.min.js"></script>

<script src = "http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

 

</head>

<body>

    <h2>기상 요건 준비</h2>

    <hr>

    <script type="text/javascript">

$(document).ready(function(){//바로 읽어 들임

    

    $.ajax({

        

        url:"http://api.openweathermap.org/data/2.5/forecast?lat=35.17944&lon=129.07556&appid=680fa4640e3a07aa6def97577ad7e05c",//lat, lon 지리적 좌표

        

        dataType:"json",//밑의 데이터를 사용하는 글자

        success:function(city){//성공했을때 호출되는 함수

            console.log(city); 

            city.name;

            $.each(city.list, function(key) {//위의 url을 기준으로 도시를 읽어 들이고..

 

                // 오늘 날짜 구하는 코딩

                var now = new Date();//오늘 날짜 데이트 함수로 호출

                var year= now.getFullYear();

                var mon = (now.getMonth()+1)>9 ? ''+(now.getMonth()+1) : '0'+(now.getMonth()+1);

                var day = now.getDate()>9 ? ''+now.getDate() : '0'+now.getDate();

                var today = year + '-' + mon + '-' + day;

                var week = new Array('일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일');    // 요일

                // api에서 받는 날짜   

                var date = city.list[key].dt_txt.substring(0,10)

                var time = city.list[key].dt_txt.substring(11,13)

                var yoil = new Date(date).getDay();    // 받아 오는 날짜의 요일 일-0 월-1 화-2....

                var todayLabel = week[yoil];

                // 최고온도 절대 온도로 받아 옴으로

                var max=(Math.round(city.list[key].main.temp_max) - 273)+"˚C";

                // 날씨

                var weath = city.list[key].weather[0].description;

                

                if(date === today) {

 

                    if(time==='12'){

                    if (weath === 'sky is clear') {//맑음

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'few clouds'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'scattered clouds'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'broken clouds'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'overcast clouds'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'shower rain'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'light rain'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'moderate rain'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'Rain'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'Thunderstorm'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'snow'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    } else if(weath === 'mist'){

                        $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                    }

                    }

                } else {

 

                    if(time==='12'){

                        if (weath === 'sky is clear') {

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'few clouds'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'scattered clouds'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'broken clouds'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'overcast clouds'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'shower rain'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'light rain'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'moderate rain'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'Rain'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'Thunderstorm'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'snow'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        } else if(weath === 'mist'){

                            $("#weather").append(date + "의 날씨는 " + weath + " 최고 온도는 " + max+"<br/>");

                        }

                    }   

                }

            });

        }

    });

});
```