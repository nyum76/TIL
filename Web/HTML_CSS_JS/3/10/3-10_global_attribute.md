# 글로벌 속성
a 태그에서 링크의 경로를 지정하는 href 속성은 글로벌 속성이 아니다.


태그 종류 상관 없이 사용할 수 있는 글로벌 속성을 ㅇㅏㄹr 보자.

## class

요소에 클래스명 지정

클래스명
- CSS 에서 클래스 선택자로 활용
- 같은 클래스명은 여러 요소가 중복해서 가질 수 있음

```html
<p class="red-color"></p>
```

## id

요소에 아이디 지정시 사용

아이디 : CSS에서 아이디 선택자로 활용 ( 중복 X )
```html
<h1 id="title"></h1>
```

## style

CSS 코드를 인라인으로 작성시 사용
```html

```

## title

요소에 추가 정보를 넣을 때 사용

🖱️ title 속성에 넣은 값은 요소에 마우스 올렸을 때 툴팁으로 표시됨
```html
<p><span title="World Wide Web Consortium">W3C</span>는 국제 웹 표준 개발 기구입니다.</p>
```

## lang
요소에 사용한 텍슽의 언어 코드 지정
```html
<html lang="ko">
```

## hidden

요소를 화면에서 감춤
```html

```
## data-*

사용자 커스텀 속성
```html
<p data-name="spiderMan" data-hero="true"></p>
```