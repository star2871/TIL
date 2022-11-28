# 페이지에 버튼을 만든다.
```
<span class="sociallink ml-1">
  <a href="javascript:sendLinkFacebook()" title="페이스북으로 공유">
    <img src="{% static 'images/facebook.png' %}" width=36 alt="Facebook">
  </a>
</span>
<span class="sociallink ml-1">
  <a href="javascript:sendLinkTwitter()" title="트위터로 공유">
    <img src="{% static 'images/twitter.png' %}" width=36 alt="Twitter">
  </a>
</span>
<span class="sociallink ml-1">
  <a href="javascript:sendLinkNaver()" title="네이버로 공유">
    <img src="{% static 'images/naver.png' %}" width=36 alt="Naver">
  </a>
</span>
<span class="sociallink ml-1">
  <a href="javascript:sendLinkKakao()" id="kakao-link-btn" title="카카오톡으로 공유">
    <img src="{% static 'images/kakaotalk.png' %}" width=36 alt="Kakaotalk">
  </a>
</span>
```

## 1. Facebook
```
function sendLinkFacebook(){
    var facebook_share_url = "https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_url }}";
    window.open(facebook_share_url,
                'Share on Facebook',
                'scrollbars=no, width=500, height=500');
}    
```
### `Facebook` 은 `https://www.facebook.com/sharer/sharer.php?u=공유할` `URL` 을 이용하면 간단하게 공유할 수 있다. 단순히 링크만 걸어도 공유에는 문제가 없지만, 전체 화면으로 창이 뜨면 모양이 예쁘지 않기 때문에 window.open() 을 이용해서 새 창에 띄워 주었다.

### 위의
```
  {{ request.build_absolute_url }}
```
### 는 Django template에서 현 page의 경로를 받아 오는 방법이다. 참고로 root 경로 이후의 경로만 표시하려는 경우
```
  { request.path }}
```
### 를 사용할 수 있다.

### 페이스북은 공유하려는 페이지에 `open graph tag`이 있으면 해당 내용을 읽어서 미리 보기를 만들어 주므로, 페이지의 `<head>` 안에 이를 넣어 주면 좋다. `Open graph tag`의 자세한 내용은 위의 링크에 들어가보면 나와 있는데, `<meta> tag` 를 이용해서 아래의 내용을 적어 주면 된다.

```
  <meta property="og:url"           content="https://www.your-domain.com/your-page.html" />
  <meta property="og:type"          content="website" />
  <meta property="og:title"         content="Your Website Title" />
  <meta property="og:description"   content="Your description" />
  <meta property="og:image"         content="https://www.your-domain.com/path/image.jpg" />
```

## 2. Twitter
```
function sendLinkTwitter(){
    var twitter_share_text="{{ post.title }}";
    var twitter_share_url="{{ request.build_absolute_uri }}";
    window.open("https://twitter.com/share?text="+twitter_share_text+"&url="+twitter_share_url,
                'Share on Twitter',
                'scrollbars=no, width=500, height=500');
}
```
### Twitter는 보낼때 기본 text와 URL을 같이 지정해줄 수 있다. https://twitter.com/share 경로에 파라미터로 text 와 url 을 적어 주면 기본 tweet 창에 미리 입력된 상태로 공유 창이 뜨게 된다.

## 3. Naver
```
function sendLinkNaver(){
    var raw_url = "{{ request.build_absolute_uri }}";
    var raw_title = "{{ post.title }}"
    var naver_root_url = "http://share.naver.com/web/shareView.nhn?url="
    var naver_share_url = naver_root_url+encodeURI(raw_url)+"&title="+encodeURI(raw_title);
    window.open(naver_share_url,
                'Share on Naver',
                'scrollbars=no, width=500, height=500');    
}
```
### 네이버 역시 기본적인 방법은 같은데, 네이버는 URL을 encoding 해 주어야 한다. Encoding 하지 않고 그냥 raw URL로 링크하는 경우 제목이 깨지는 등의 문제가 발생한다. 자바스크립트 내장 함수인 encodeURI()로 인코딩한 주소를 링크해주면 된다.

## 4. Kakaotalk
### 다른 방법으로 해야 되서 나중에 다시 정리하기