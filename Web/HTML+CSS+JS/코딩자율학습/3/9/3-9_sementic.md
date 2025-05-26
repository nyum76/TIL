# 시멘틱 태그
의미있는 웹 페이지 설계
시맨틱 태그의 종류 (예시)
<div>
  <table>
    <colgroup span="2" style="width:200px"></colgroup>
    <thead>
      <tr style="height:50px">
        <th colspan="2">header / nav </th>
      </tr>
    </thead>
    <tfoot>
      <tr style="height:50px">
        <td colspan="2">footer</td>
      </tr>
    </tfoot>
    <tbody>
      <tr style="height:50px">
        <td>section</td>
        <td rowspan="2">aside</td>
      </tr>
      <tr style="height:50px">
        <td>article</td>
      </tr>
    </tbody>
  </table>
</div>

## header 태그
헤더 영역
- 웹사이트 최상단 or 좌측 위치
- 로고, 검색, 메뉴 등 포함
```html
<header>
  헤더 구성 요소
</header>
```

## nav 태그
navigation
- 웹 페이지에서 내부의 다른 영역이나 외부 연결하는 링크 영역을 구분
- header 영역에 포함되어 있음


```html
<nav></nav>
```

## section 태그
웹 페이지에서 **논리적으로 관련 있는 내용 영역** 구분
- 일반적으로 내용의 제목을 나타내기위해 **hn 태그를 포함**


```html
<section></section>
```

## article 태그
웹 페이지에서 **독립적인 영역을 구분**할 때 사용

예시 - 네이버 홈피 로그인 영역
```html
<article></article>
```

## aside 태그

웹 페이지 안에서 주력 내용이지만 독립적인 내용으로 보기 어려워 article 태그나 section 태그로 영역을 구분할 수 없을 때 사용

```html
<aside></aside>
```

## footer 태그

footer 영역
- 웹 페이지의 최하단
- 저작권 정보, 연락처, 사이트 맵 등의 요소 포함


## main 태그
웹 페이지의 주요 내용 지정시 사용
- 반복해서 등장하는 요소 포함 X
- article, aside, footer, header, nav 태그 하위에 포함 X